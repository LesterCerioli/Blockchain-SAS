from flask import Blueprint, request, jsonify
from app.services.blockchain_service import blockchain_service
from app.repositories.elasticsearch import index_block

api_bp = Blueprint("api", __name__)

@api_bp.route("/add_block", methods=["POST"])
def add_block():
    data = request.json.get("data", "")
    if not data:
        return jsonify({"error": "Data is required"}), 400

    block = blockchain_service.add_block(data)
    index_block(block)  # Store the block in Elasticsearch
    return jsonify({"message": "Block added", "block": block.__dict__})

@api_bp.route("/get_chain", methods=["GET"])
def get_chain():
    chain = [
        {
            "id": block.id,
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "hash": block.hash
        } for block in blockchain_service.get_chain()
    ]
    return jsonify({"chain": chain}) 
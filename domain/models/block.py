import hashlib
import time
import uuid

class Block:
    def __init__(self, index: int, timestamp: float, data: str, previous_hash: str):
        self.id = str(uuid.uuid4())  # Unique identifier
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"<Block index={self.index}, id={self.id}, hash={self.hash}>"

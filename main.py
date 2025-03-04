

from app.services.blockchain_service import BlockchainService
from app.services.token_service import TokenService
from app.repositories.elasticsearch import ElasticsearchRepository


# Initialize FastAPI app
app = FastAPI(title="Blockchain-SAS API", description="API for Blockchain and Token Management")

# Initialize services
blockchain_service = BlockchainService()
token_service = TokenService()
elasticsearch_repo = ElasticsearchRepository()

# Include routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Blockchain-SAS API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

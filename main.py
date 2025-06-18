from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from core.allocation_engine import allocate_portfolio
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin. Replace "*" with specific origins if needed.
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.).
    allow_headers=["*"],  # Allow all headers.
)

class PortfolioRequest(BaseModel):
    risk_level: str
    amount: float
    use_api: bool

@app.post("/generate")
async def generate_portfolio(request: PortfolioRequest):
    """
    Generate portfolio allocations based on user inputs.
    """
    try:
        logger.info(f"Request received: {request}")
        portfolio = allocate_portfolio(request.risk_level, request.amount, request.use_api)
        return portfolio
    except ValueError as ve:
        logger.error(f"Client error: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.allocation_engine import allocate_portfolio

router = APIRouter()

class PortfolioRequest(BaseModel):
    risk_level: str
    amount: float

@router.post("/generate")
async def generate_portfolio(request: PortfolioRequest):
    """
    Generate portfolio allocations based on user inputs.
    """
    try:
        portfolio = allocate_portfolio(request.risk_level, request.amount)
        return portfolio
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
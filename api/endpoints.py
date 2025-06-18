from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from core.allocation_engine import allocate_portfolio
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class PortfolioRequest(BaseModel):
    risk_level: str
    amount: float = Field(gt=0)
    use_api: bool = True

@router.post("/generate")
async def generate_portfolio(request: PortfolioRequest):
    try:
        portfolio = await allocate_portfolio(request.risk_level, request.amount, request.use_api)
        return portfolio
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except EnvironmentError as ee:
        raise HTTPException(status_code=500, detail=str(ee))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

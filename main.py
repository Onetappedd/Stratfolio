from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import logging
from core.allocation_engine import allocate_portfolio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PortfolioRequest(BaseModel):
    risk_level: str
    amount: float = Field(gt=0)
    use_api: bool = True

@app.post("/generate")
async def generate_portfolio(request: PortfolioRequest):
    try:
        logger.info("Request received: %s", request)
        portfolio = await allocate_portfolio(request.risk_level, request.amount, request.use_api)
        return portfolio
    except ValueError as ve:
        logger.error("Client error: %s", ve)
        raise HTTPException(status_code=400, detail=str(ve))
    except EnvironmentError as ee:
        logger.error("Configuration error: %s", ee)
        raise HTTPException(status_code=500, detail=str(ee))
    except Exception as e:
        logger.error("Server error: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

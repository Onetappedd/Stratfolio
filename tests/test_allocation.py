import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.allocation_engine import allocate_portfolio

@pytest.mark.asyncio
async def test_allocate_portfolio_static():
    result = await allocate_portfolio("Moderate", 1000, use_api=False)
    assert result["cash"] == 100.0
    assert len(result["stocks"]) == 3
    assert len(result["bonds"]) == 2

@pytest.mark.asyncio
async def test_allocate_portfolio_invalid_amount():
    with pytest.raises(ValueError):
        await allocate_portfolio("Moderate", -1, use_api=False)

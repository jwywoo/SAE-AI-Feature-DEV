from fastapi import APIRouter

from stock.schemas import StockGenerationRequestDto, StockGenerationResponseDto
from stock.service import stock_generation_service

router = APIRouter()

@router.post("/ai/stock/generation", response_model=StockGenerationResponseDto)
def stock_generation_router(request: StockGenerationRequestDto):
    return stock_generation_service(request)
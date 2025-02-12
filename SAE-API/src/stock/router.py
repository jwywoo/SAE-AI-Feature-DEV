from fastapi import APIRouter, Depends, status
from stock.schemas import StockGenerationRequestDto, StockGenerationResponseDto
from stock.service import stock_generation_service

router = APIRouter()


@router.post(
    "/ai/stock/generation",
    response_model=StockGenerationResponseDto,
    status_code=status.HTTP_201_CREATED
)
async def stock_generation_router(request: StockGenerationRequestDto):
    return await stock_generation_service(request)

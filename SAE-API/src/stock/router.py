from http.client import HTTPException
from fastapi import APIRouter, Depends, status
from stock.schemas import StockGenerationRequestDto, StockGenerationResponseDto
from stock.service import stock_generation_service, test_case_collector_service

router = APIRouter()


@router.post(
    "/ai/stock/generation",
    response_model=StockGenerationResponseDto,
    status_code=status.HTTP_201_CREATED
)
async def stock_generation_router(request: StockGenerationRequestDto):
    return await stock_generation_service(request)


@router.post("/ai/stock/test", status_code=status.HTTP_201_CREATED)
async def test_case_collector_router(request: StockGenerationRequestDto):
    if await test_case_collector_service(request):
        return {"message": "Test case saved successfully."}
    raise HTTPException(status_code=500, detail="Failed to save test case.")
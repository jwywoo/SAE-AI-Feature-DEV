from pydantic import BaseModel, Field


class StockGenerationRequestDto(BaseModel):
    title: str = Field(..., min_length=1)
    url: str = Field(..., min_length=5, max_length=2083)
    content: str = Field(..., min_length=1)


class StockDto(BaseModel):
    stock_name: str = Field(..., min_length=1, max_length=255)
    ticker_symbol: str = Field(..., min_length=1, max_length=20)
    market_name: str = Field(..., min_length=1, max_length=255)


class StockGenerationResponseDto(BaseModel):
    status: int
    generated_stocks: list[StockDto] = Field(default_factory=list)

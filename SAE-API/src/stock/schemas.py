from pydantic import BaseModel


class StockGenerationRequestDto(BaseModel):
    title: str
    url: str
    content: str


class StockGenerationResponseDto(BaseModel):
    stock_name: str
    ticker_symbol: str
    market_name: str

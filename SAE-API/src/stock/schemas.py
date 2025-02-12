from pydantic import BaseModel


class StockGenerationRequestDto(BaseModel):
    title: str
    url: str
    content: str


class StockDto(BaseModel):
    stock_name: str
    ticker_symbol: str
    market_name: str

class StockGenerationResponseDto(BaseModel):
    status : int
    generated_stocks : list[StockDto]
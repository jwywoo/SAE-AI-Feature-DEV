from stock.schemas import StockGenerationRequestDto, StockGenerationResponseDto


def stock_generation_service(request: StockGenerationRequestDto):
    return StockGenerationResponseDto(
        stock_name=request.title,
        ticker_symbol=request.url,
        market_name=request.content
    )

from stock.methods.preprocessing_methods import text_cleaning

from stock.schemas import StockGenerationRequestDto, StockGenerationResponseDto

SEP = "[SEP]"


def stock_generation_service(request: StockGenerationRequestDto):
    page_data = "Title: " + request.title + SEP \
        + "URL" + request.url + SEP \
        + "Page Information :" + text_cleaning(request.content)

    # Generation
    return StockGenerationResponseDto(
        stock_name="",
        ticker_symbol="",
        market_name=""
    )

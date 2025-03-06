from stock.methods.preprocessing_method import text_cleaning
from stock.methods.generation_method import stock_generation, stock_response_gen
from stock.methods.test_case_method import test_case_save

from stock.schemas import StockGenerationRequestDto

from stock.prompts.generation_prompt import GenerationPrompt


SEP = "[SEP]"


async def stock_generation_service(request: StockGenerationRequestDto):
    cleaned_content = text_cleaning(request.content) 
    page_data = f"Title: {request.title} {SEP} URL: {request.url} {SEP} Page Information: {cleaned_content}"

    # Generation
    # System Prompt
    generation_prompt = GenerationPrompt
    system_prompt = generation_prompt.stock_gen_system_prompt.value

    generated_stocks = await stock_generation(page_data, system_prompt)
    responseDto = await stock_response_gen(generated_result=generated_stocks)

    return responseDto

async def test_case_collector_service(request: StockGenerationRequestDto) -> bool:
    cleaned_content = text_cleaning(request.content)
    return test_case_save(request.title, request.url, cleaned_content)

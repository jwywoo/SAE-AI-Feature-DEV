from stock.methods.preprocessing_method import text_cleaning
from stock.methods.generation_method import stock_generation, stock_response_gen

from stock.schemas import StockGenerationRequestDto

from stock.prompts.generation_prompt import GenerationPrompt


SEP = "[SEP]"


def stock_generation_service(request: StockGenerationRequestDto):
    page_data = "Title: " + request.title + SEP \
        + "URL" + request.url + SEP \
        + "Page Information :" + text_cleaning(request.content)

    # Generation
    # System Prompt
    generation_prompt = GenerationPrompt
    system_prompt = generation_prompt.stock_gen_system_prompt.value

    generated_stocks = stock_generation(page_data, system_prompt)
    responseDto = stock_response_gen(generated_result=generated_stocks)

    return responseDto

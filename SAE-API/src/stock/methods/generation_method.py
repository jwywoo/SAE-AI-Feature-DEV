import json

from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from stock.schemas import StockGenerationResponseDto, StockDto


def stock_generation(input, system_prompt):
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_prompt),
            ('human', '{input}'),
        ]
    )
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.0
    )
    chain = final_prompt | llm | StrOutputParser()
    return json.loads(chain.invoke({"input": input}))[0]


def stock_response_gen(generated_result):
    generation_status = generated_result["status"]
    stocks = generated_result["stocks"]
    if (not generation_status):
        return StockGenerationResponseDto(
            status=0,
            generated_stocks=[]
        )
    
    generated_stocks = []
    for i in range(len(stocks)):
        generated_stocks.append(
            StockDto(
                stock_name=stocks[i]["stock_name"],
                ticker_symbol=stocks[i]["ticker_symbol"],
                market_name=stocks[i]["market_name"]
            )
        )
    return StockGenerationResponseDto(
        status=1,
        generated_stocks=generated_stocks
    )
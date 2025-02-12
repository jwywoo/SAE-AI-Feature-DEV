import json

from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from stock.schemas import StockGenerationResponseDto, StockDto


async def stock_generation(input: str, system_prompt: str):
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

    result = await chain.ainvoke({"input": input})
    return json.loads(result)[0]


async def stock_response_gen(generated_result):
    if not generated_result["status"]:
        return StockGenerationResponseDto(status=0, generated_stocks=[])

    generated_stocks = [
        StockDto(**stock) for stock in generated_result["stocks"]
    ]

    return StockGenerationResponseDto(status=1, generated_stocks=generated_stocks)

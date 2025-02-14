# SAE-AI-Feature-DEV

## Goal & Purpose

- KOR: '온 세상이 주식이야'(이하 온세주)의 AI 위한 개발 저장소
  - Chrome Extension에서의 정보와 가장 유사한 주식 종목 생성 및 반환
- ENG: AI API Dev repository for 'Stocks Are Everywhere'
  - Returning most relevant stocks based on data from the chrome extension

## Directory Structure

```bash
SAE-Chrome-Dev/
├── SAE-AI
├── SAE-API 
└── SAE-Data
```

## [SAE-Data](https://github.com/jwywoo/SAE-AI-Feature-DEV/tree/main/SAE-Data)

### As is

- Preprocessing Techniques
  - Text Cleaning

### To be

- LLM as Data Preprocessor

## [SAE-AI](https://github.com/jwywoo/SAE-AI-Feature-DEV/tree/main/SAE-AI)

### As is

- ChatPromptTemplate

### To be

- Advanced RAG
- Multi Agent System

## [SAE-API](https://github.com/jwywoo/SAE-AI-Feature-DEV/tree/main/SAE-API/src)

### As is

- MVP FastAPI

### To be

- Async + uvicorn
- Pydantic
- kafka
- websocket: for realtime stock price

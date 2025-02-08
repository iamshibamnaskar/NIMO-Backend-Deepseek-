from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from ollama import chat

app = FastAPI()

# Allow all origins for now (you can specify a list of allowed origins later)
origins = [
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

async def generate_stream(message: str):
    """Streams the response from Ollama chat in real-time."""
    stream = chat(
        model='deepseek-r1:1.5b',
        messages=[{'role': 'user', 'content': f'{message}'}],
        stream=True,
    )

    for chunk in stream:
        text = chunk['message']['content']
        yield text.encode("utf-8")

@app.post("/query")
async def query(request: Request):
    """Handles the POST request and streams the response."""
    data = await request.json()
    message = data.get("message")
    
    return StreamingResponse(generate_stream(message), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

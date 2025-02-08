from ollama import chat

stream = chat(
    model='deepseek-r1:1.5b',
    messages=[{'role': 'user', 'content': 'Why is the sky blue? write point wise'}],
    stream=True,
)

for chunk in stream:
    text = chunk['message']['content']
    print(text)

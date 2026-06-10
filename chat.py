from ollama import chat

response = chat(
    model="BerlinAI:v1",
    messages=[
        {
            "role": "user", 
            "content": "Apakah kamu tahu politik?", 
        }
    ],
)

print(response.message.content)
from ollama import chat

path = input("nama file gambarmu apa: ")

response = chat(
    model="BerlinAI:v1",
    messages=[
        {
            "role": "user", 
            "content": "ini gambar apa ya?", 
            "images": [path]
        }
    ],
)

print(response.message.content)
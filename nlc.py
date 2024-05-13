from openai import OpenAI

client = OpenAI(base_url="http://localhost:8080/v1", api_key="lm-studio")

print("NATURAL LANGUAGE COMPUTING==>")

messages = [
    {"role": "user", "content": "You can do computing tasks"},
]
question = "Multiply the matrix [[1, 2], [3, 4]] with [[5, 6], [7, 8]]"
messages.append({"role": "user", "content": question})
completion = client.chat.completions.create(
    model="LM Studio Community/Phi-3-mini-4k-instruct-GGUF",
    messages=messages,
    temperature=0.7,
)
print(completion.choices[0].message.content)

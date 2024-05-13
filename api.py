from openai import OpenAI

client = OpenAI(base_url="http://localhost:8080/v1", api_key="lm-studio")

print("API READING ==>")

with open("./test.md") as f:
    wikipedia_page = f.read()

messages = [
    {"role": "user", "content": "When was Albert Einstein born?"},
    {"role": "user", "content": f"Use this- {wikipedia_page}"},
]
completion = client.chat.completions.create(
    model="LM Studio Community/Phi-3-mini-4k-instruct-GGUF",
    messages=messages,
    temperature=0.7,
)
print(completion.choices[0].message.content)

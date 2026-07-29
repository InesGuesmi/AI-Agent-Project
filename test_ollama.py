import requests

url = "http://localhost:11434/api/generate"
data = {"model": "phi3", "prompt": "Hello", "stream": False}
response = requests.post(url, json=data)
resultat = response.json()
print(resultat["response"])


def llm_local(prompt):
    url = "http://localhost:11434/api/generate"


    data = {"model": "phi3", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data)
    return response.json()["response"]
print(
llm_local(
"what's an Agent IA ?"
)
)
print(
llm_local("Explain RAG simply")
)
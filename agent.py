import requests

url="http://127.0.0.1:11434/api/generate"

data={
    "model":"qwen2.5:3b",
    "promote":"你好",
    "stream":False
}

print("正在调用Qwen")

response=requests.post(url,json=data)
result=response.json()

print("Qwen:")
print(result["result"])

import requests


url = "http://127.0.0.1:11434/api/generate"

print("=========================================")
print(" TA Code Assistant (技术美术专属助手) ")
print(" 输入 'exit' 退出对话 ")
print("=========================================")


while True:

    user_input = input("\n你：")

  
    if user_input.lower() in ['exit', 'quit']:
        print("助手：再见！祝你的 TA 之路顺利！")
        break


    data = {
        "model": "qwen2.5:3b",
      
        "prompt": f"你是一个资深的技术美术和游戏开发助手，用通俗的话回答。用户问：{user_input}",
        "stream": False
    }

    print("助手正在思考中...")

 
    try:
        response = requests.post(url, json=data)
        result = response.json()

   
        print(f"助手：{result['response']}")

    except Exception as e:
        print("哎呀，出错了，错误信息是：", e)

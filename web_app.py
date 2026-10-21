import streamlit as st
import requests

st.title("🎨 TA 专属 AI 助手")
st.write("这是属于我的第一个 Web App！")

user_input = st.chat_input("请输入你的问题：")

if user_input:
    st.write(f"👤 **你**：{user_input}")

    # 这里加上网络请求逻辑，去连你的本地 Ollama
    url = "http://127.0.0.1:11434/api/generate"
    data = {
        "model": "qwen2.5:3b",
        "prompt": f"你是一个资深技术美术，请简明扼要地回答：{user_input}",
        "stream": False
    }

    with st.spinner("助手正在疯狂思考中..."):
        try:
            response = requests.post(url, json=data)
            result = response.json()
            st.write(f"🤖 **助手**：{result['response']}")
        except Exception as e:
            st.write(f"🤖 **助手**：哎呀，连不上本地大模型了。报错是：{e}")

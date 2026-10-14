# K-ON
二面实战部分记录

## 自我介绍
软工大一新生

## 任务
### 一、大模型 

#### 模型部署
-问题1：魔搭社区提供的evalscope脚本为pip格式，本人电脑为免安装python无法处理

-解决：通过询问DS得知ensurepip的指令，尝试后还是无法解决所以直接删了重下python

<img width="1861" height="429" alt="微信图片_20261002171014_5_137" src="https://github.com/user-attachments/assets/0dc7b86d-6c2a-4b4c-a58b-f6feffcd53bf" />

-问题2：在pycharm终端处理（更换新解释器，重新敲入脚本），发现evalscope的版本较旧无法与3.14版的python匹配

-解决：下载旧版本的python
<img width="1575" height="1181" alt="微信图片_20261002171017_9_137" src="https://github.com/user-attachments/assets/3cd5c80a-ff2b-4f83-93ec-2e63110154aa" />

-问题3：更换后仍然无法解决，再次寻求DS帮助，得知仍为版本历史遗留问题且evalscope与模型部署并无太大关系

-解决：跳过该步骤，以后学习更多知识了再解决
<img width="1575" height="1181" alt="微信图片_20261002171017_8_137" src="https://github.com/user-attachments/assets/a7acb78b-607e-4869-8e7b-95b5cab1c6ea" />
<img width="1575" height="1181" alt="微信图片_20261002171016_7_137" src="https://github.com/user-attachments/assets/c76ead57-d317-4ea2-9abd-d23b21e8a981" />
<img width="1575" height="1181" alt="微信图片_20261002171015_6_137" src="https://github.com/user-attachments/assets/c1e430aa-2f79-4f2f-8f46-6a52043cde54" />

-了解后选择下载Ollama
<img width="1575" height="1181" alt="微信图片_20261002174514_11_137" src="https://github.com/user-attachments/assets/4a24eb9e-ecc3-48c0-982b-9d8b90a7ecfd" />

-视奸群聊下载了qwen2.5:3b
<img width="1575" height="1181" alt="微信图片_20261002174513_10_137" src="https://github.com/user-attachments/assets/c0f8b65b-d1e7-48ae-941f-bc9f877d2c59" />

-问题4：因为多次失败所以问了qwen是否已经在本地部署了，显示没有

-解决：询问DS发现是训练设定
<img width="1706" height="1279" alt="微信图片_20261002164843_4_137" src="https://github.com/user-attachments/assets/b7e50c6a-06b3-40d2-91f2-23539b73392e" />

-在使用python调用本地api时，触发了Windows环境下的ConnectionError（端口11434连接失败）。我已尝试关闭代理、修改localhost为127.0.0.1等排查方法，仍然无法战胜。后续会在学习中进一步改进。

-已成功找出失败原因，现可直接连接


#### 智能体
-注册coze，并进行初步了解
<img width="2273" height="1286" alt="屏幕截图 2026-10-09 200155" src="https://github.com/user-attachments/assets/81cae846-7dc4-41a9-8ebb-8e6f2793b476" />
<img width="2100" height="1397" alt="屏幕截图 2026-10-09 200654" src="https://github.com/user-attachments/assets/4d5a1257-3d20-46c9-93f8-11bfe8bc16b9" />
-在coze内安装插件并进行调用
<img width="1180" height="1063" alt="屏幕截图 2026-10-12 202403" src="https://github.com/user-attachments/assets/96fb4d14-252c-4812-8f44-92aa4ed93acd" />

-借助ai帮助，完成简易cli智能体，并通过自身需求改进prompt
<img width="2206" height="1406" alt="屏幕截图 2026-10-14 225357" src="https://github.com/user-attachments/assets/e90c5b6b-4d85-47ce-9fa9-6090a674afb9" />



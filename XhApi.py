# -*- coding = utf-8 -*-
"""
# @Time : 2023/7/20 12:37
# @Author : CSDN:FriKlogff
# @File : XhApi.py
# @Software: PyCharm
# @Function: 星火大模型API
"""
import os
os.system("""python -m pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip setuptools
pip install -i https://mirrors.aliyun.com/pypi/simple/ websocket
pip install -i https://mirrors.aliyun.com/pypi/simple/ websocket-client
pip install -i https://mirrors.aliyun.com/pypi/simple/ gradio
pip install -i https://mirrors.aliyun.com/pypi/simple/ sxtwl
""")
import _thread as thread  # 导入线程模块
import base64  # 导入base64编码模块
import datetime  # 导入datetime模块
import hashlib  # 导入hashlib模块
import hmac  # 导入hmac模块
import json  # 导入json模块
from urllib.parse import urlparse  # 从urllib.parse导入urlparse用于url解析
import ssl  # 导入ssl模块
from datetime import datetime  # 从datetime导入datetime类
from time import mktime  # 从time导入mktime用于生成时间戳
from urllib.parse import urlencode  # 从urllib.parse导入urlencode用于编码请求参数
from wsgiref.handlers import format_date_time  # 从wsgiref.handlers导入format_date_time用于格式化时间

import websocket  # 导入websocket模块

response_content = ""


# 请求参数类
class Ws_Param:
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID  # 应用ID
        self.APIKey = APIKey  # API Key
        self.APISecret = APISecret  # API Secret
        self.host = urlparse(gpt_url).netloc  # 从url解析出host
        self.path = urlparse(gpt_url).path  # 从url解析出path
        self.gpt_url = gpt_url  # 完整的url

    # 生成签名和url的方法
    def create_url(self):
        now = datetime.now()  # 当前时间
        date = format_date_time(mktime(now.timetuple()))  # 格式化的时间戳
        # 拼接签名原文
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"
        # 生成签名
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')
        # 生成授权header
        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 生成url参数字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 构造最终url
        url = self.gpt_url + '?' + urlencode(v)
        return url


# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws):
    print("### closed ###")


# 收到websocket连接建立的处理
def on_open(ws):
    thread.start_new_thread(run, (ws,))


# 发送请求的方法
def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, question=ws.question))
    ws.send(data)


# 收到websocket消息的处理
def on_message(ws, message):
    print(message)
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        print(content, end='')
        global response_content
        response_content += content
        if status == 2:
            ws.close()


# 生成请求参数
def gen_params(appid, question):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234"
        },
        "parameter": {
            "chat": {
                "domain": "general",
                "random_threshold": 0.5,
                "max_tokens": 2048,
                "auditing": "default"
            }
        },
        "payload": {
            "message": {
                "text": [
                    {"role": "user", "content": question}
                ]
            }
        }
    }
    return data




def main(appid, api_key, api_secret, gpt_url, question):
    wsParam = Ws_Param(appid, api_key, api_secret, gpt_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    return response_content

import requests
url = "http://httpbin.org/get"
params = {   # 根据需要添加请求参数
    "name1": "value1",
    "name2": "value2"
}
headers = {   # 根据需要加入头部信息
    "User-agent": ".....",
    "Spam": "Eggs"
}
cookies={}
resp = requests.get(url=url, params=params, headers=headers) # GET 请求
# resp = requests.post(url=url, params=params,headers=headers, cookies=cookies) # POST 请求
print(resp.status_code)  #  状态码
print(resp.text)       # 返回的文本
print(resp.encoding)  # 编码
print(resp.ok)       # 返回bool值，状态码小于400就返回True，否则False
print(resp.json())    # 返回的数据以json形式显示

# 文件上传
files = {"file": ("data.csv", open("data.csv", "rb"))}
resp = requests.post(url, files=files)
print(resp.status_code)
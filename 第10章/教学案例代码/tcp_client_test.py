from socket import socket, AF_INET, SOCK_STREAM

if __name__ == "__main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 9995))

    while True:
        in_str = input("输入数据：")
        if not in_str:
            break
        s.send(bytes(in_str, "utf-8"))
        print("来自服务器消息：%s" % str(s.recv(4096), "utf-8"))


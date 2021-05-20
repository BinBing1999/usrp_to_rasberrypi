import socket
import numpy as np

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.3.1",1534))  #绑定服务器的ip和端口，先设计好自己的i皮地址、、rasberry:"nothing inside"

s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 40960)
recv_buff = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
print(f'修改后接收缓冲区大小：{recv_buff}')
print('\n')
while(1):
    data=s.recv(2048)  #、、一次接收2048字节
    f = open("test.txt", "a", encoding='utf-8')
    print(data)
    texte=str(data,encoding="utf-8")
    print(texte)
    f.write(texte)
    f.write('\n')
    f.close()
s.close()

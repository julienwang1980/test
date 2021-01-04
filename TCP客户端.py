import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    # 1. AF_INET: 表示ipv4
    # 2. SOCK_STREAM: tcp传输协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务端应用程序建立连接
    tcp_client_socket.connect(('10.135.20.169', 9090))
    # 代码执行到此，说明连接建立成功
    # 准备发送的数据
    send_data = '你好服务端，我是客户端小黑！'.encode('gbk')
    # 发送数据
    tcp_client_socket.send(send_data)
    # 接收数据，这次接收的数据最大字节数是1024
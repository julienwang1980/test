import socket
import threading
import framework
import logging
import sys

# 在程序入口模块，设置logging日志的配置信息，只配置一次，整个程序都可以使用，好比单例
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s",
                    filename="log.txt",
                    filemode="a")


# 定义Web服务器类
class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务器套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用，程序退出端口立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(('', port))
        # 设置监听
        tcp_server_socket.listen(128)
        # 保存创建成功的服务器套接字
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端的请求
    @staticmethod
    def handle_client_request(new_socket):
        # 代码执行到此，说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print('关闭浏览器了')
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_client_content = recv_client_data.decode('utf-8')
        print(recv_client_content)
        # 根据指定字符串进行分割，最大分割次数指定2
        request_list = recv_client_content.split(' ', maxsplit=2)

        # 获取请求资源
        request_path = request_list[1]
        print(request_path)

        # 判断请求的是不是根目录，如果条件成立，指定首页数据返回
        if request_path == '/':
            request_path = '/index.html'

        # 判断是否是动态资源请求，以后把后缀是.html的请求任务是动态资源请求
        if request_path.endswith(".html"):
            """动态资源请求"""
            logging.info("动态资源请求地址：" + request_path)
            # 动态资源请求找web框架进行处理，需要把请求参数给web框架
            # 准备给web框架的参数信息，都要放到字典里面
            env = {
                "request_path": request_path,
                # 传入请求头信息，额外的参数可以在字典里面再进行添加
            }
            # 使用框架处理动态资源请求
            # 1. web框架需要把处理结果返回给web服务器
            # 2. web服务器负责把返回的结果封装成响应报文发送给浏览器
            status, headers, response_body = framework.handle_request(env)
            print(status, headers, response_body)
            # 响应行
            response_line = "HTTP/1.1 %s\r\n" %status
            # 响应头
            response_header = ""
            for header in headers:
                response_header += "%s: %s\r\n" %header

            # 响应报文
            response_data = (response_line +
                             response_header +
                             "\r\n" +
                             response_body).encode("utf-8")

            # 发送响应报文数据给浏览器
            new_socket.send(response_data)
            # 关闭连接
            new_socket.close()

        else:
            """静态资源请求"""
            logging.info("静态资源请求地址：" + request_path)
            try:
                # 动态打开指定文件
                with open('static' + request_path, 'rb') as file:
                    # 读取文件数据
                    file_data = file.read()
            except Exception as e:
                # 请求资源不存在，返回404数据
                # 响应行
                response_line = 'HTTP/1.1 404 Not Found\r\n'
                # 响应头
                response_header = 'Server: PWS1.0\r\n'
                # 响应体
                with open('static/error.html', 'rb') as file:
                    file_data = file.read()
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header +'\r\n').encode('utf-8') + response_body
                # 发送数据
                new_socket.send(response_data)
            else:
                # 响应行
                response_line = 'HTTP/1.1 200 OK \r\n'
                # 响应头
                response_header = 'Server: PWS1.0\r\n'
                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body
                # 发送数据
                new_socket.send(response_data)
            finally:
                # 关闭服务与客户端的套接字
                new_socket.close()

    # 启动Web服务器进行工作
    def start(self):
        while True:
            # 等待接收客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            # 当客户端和服务器连接后，创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程执行对应的任务
            sub_thread.start()


# 程序入口函数
def main():
    print(sys.argv)
    # 判断命令行参数是否等于2
    if len(sys.argv) != 2:
        print('执行命令如下：python3 xxx.py 8000')
        logging.warning("在终端启动程序参数的个数不等于2！")
        return

    # 判读字符串是否都是数字组成
    if not sys.argv[1].isdigit():
        print('执行命令如下：python3 xxx.py 8000')
        logging.warning("在终端启动程序参数的类型不是数字字符串！")
        return

    # 获取终端命令行参数
    port = int(sys.argv[1])
    # 创建Web服务器对象
    web_server = HttpWebServer(port)
    # 启动Web服务器进行工作
    web_server.start()

if __name__ == '__main__':
    main()

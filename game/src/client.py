
   #     alculator 为 Match
# 此处修改 ttypes 路径 以及 User 类
from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    # 调试语句
    user = User(1, 'yxc', 1500)
    client.add_user(user, "") 

    # Close!
    transport.close()

# 调用 main 函数
if __name__ == "__main__":
    main()



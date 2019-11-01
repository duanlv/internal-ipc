from util import check_exit, encrypt, decrypt
import sys, time, socket

class Client:
    def __init__(self, host='127.0.0.1', port='8080'):
        self.seq_no = 0
        self.host = host
        self.port = port
        #@TODO

    # connect
    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.host, self.port)

    # send request
    def send_request(self, cmd, params):
        #@TODO: serialize data into string
        #self.connect()
        self.client.send(msg)
        self.seq_no = self.seq_no + 1

    # get response
    def get_response(self):
        response = self.client.recv(1024)
        #@TODO: deserialize string into data
        #return resp

# For server, consider to use sockserver instead
# class Server:
#      def __init__(self, host='127.0.0.1', port='8080'):
#         self.port = port
#         self.host = ""
#         # establishs connection
#         self.init_conn()
#         # run server
#         self.run()

#     def init_conn(self):
#         try :
#             self.srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         except socket.error, e:
#             print("Error creating server socket: %s" % e)
#             sys.exit(1)

#         try :
#             self.srv.bind((host, port))
#         except socket.error, e :
#             print("Error in binding host and port: %s" %e)

#     def run(self, hdl):
#         while (True):
#             ...



import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

auth = DummyAuthorizer();
auth.add_user("test", '504683', os.getcwd())

handler = FTPHandler
handler.authorizer = auth

server = FTPServer(("127.0.0.1", 3127), handler)
print "server started"
server.serve_forever()
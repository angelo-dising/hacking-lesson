import socket
 
def scan(addr, port):
    #creates a new socket using the given address family. 
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    #setting up the default timeout in seconds for new socket object 
    socket.setdefaulttimeout(1)
 
    #returns 0 if connection succeeds else raises error 
    result = socket_obj.connect_ex((addr,port)) #address and port in the tuple format 
 
    #closes te object 
    socket_obj.close()
 
    return result
 
# lista de puertos a escanear
ports=[21, 22, 25, 80]
 
# bucle por todas las ip del rango 192.168.0.*
for i in range(1,255):
    addr="192.168.0.{}".format(i)
    for port in ports:
        result=scan(addr, port)
        if result==0:
            print(addr, port, "OK")
        else:
            print(addr, port, "Failed")
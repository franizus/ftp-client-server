import socket
import sys
import select


def prompt():
    sys.stdout.write('<Tu> ')
    sys.stdout.flush()


if __name__ == "__main__":
    if(len(sys.argv) < 3) :
        print('Usage : python telnet.py hostname port')
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try :
        s.connect((host, port))
    except :
        print('No se puede conectar')
        sys.exit()

    while 1:
        socket_list = [sys.stdin, s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data.decode('ascii'))
                    prompt()
            else:
                msg = sys.stdin.readline()
                s.send(msg.encode('ascii'))
                prompt()

    s.close()
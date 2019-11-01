import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind(host, port)

    server_socket.listen(2)
    conn, adress = server_socket.accept()
    print('Connection From'+str(adress))

    while True:

        data = conn.recv(1024).decode()
        if not data:

            break

            print('From Connection User'+str(data))
            data = input('->')
            conn.send(data.encode())

            conn.close()

            server_program()


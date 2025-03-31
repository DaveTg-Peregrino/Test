import socket

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket al puerto
server_socket.bind(('127.0.0.1', 55555))

# Escuchar conexiones entrantes
server_socket.listen(1)

print('Servidor escuchando en el puerto 55555...')

while True:
    # Esperar una conexión
    client_socket, client_address = server_socket.accept()
    print(f'Conexión establecida desde {client_address}')

    # Enviar un mensaje al cliente
    client_socket.sendall(b'Hola, cliente!')

    # Cerrar la conexión
    client_socket.close()

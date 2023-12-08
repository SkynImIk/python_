import socket
import threading

def client_thread(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            message = conn.recv(1024).decode()
            if message.lower() == 'quit':
                break
            print(f"Received from {addr}: {message}")
            broadcast(message)
        except ConnectionResetError:
            break
    conn.close()
    clients.remove(conn)
    print(f"Connection with {addr} closed.")

def client_thread(conn, addr):
    print(f"Connected by {addr}")
    
    # Приймання імені користувача
    username = conn.recv(1024).decode()
    print(f"Username: {username}")
    
    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        
        # Надсилання повідомлення всім підключеним клієнтам
        print(f"Received from {username}: {message}")
        broadcast(f"{username}: {message}")
        
        # Запис повідомлення у текстовий файл на сервері
        with open('server_log.txt', 'a') as log_file:
            log_file.write(f"{username}: {message}\n")
    
    conn.close()

def broadcast(message):
    for client in clients:
        client.send(message.encode())


def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except ConnectionResetError:
            clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        print(f"Connection from {addr} established.")

        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    clients = []
    start_server()

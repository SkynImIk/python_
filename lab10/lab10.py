import tkinter as tk
import socket
import threading

def send_message():
    message = entry_field.get()
    chat_box.insert(tk.END, f"{username.get()}: {message}\n")
    entry_field.delete(0, tk.END)
    client_socket.send(message.encode())

def connect_to_server():
    global client_socket, username, username_window
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    username_window = tk.Toplevel(root)
    username_window.title("Enter Username")
    username_label = tk.Label(username_window, text="Enter your username:")
    username_label.pack()
    username = tk.Entry(username_window)
    username.pack()
    submit_button = tk.Button(username_window, text="Submit", command=submit_username)
    submit_button.pack()

def submit_username():
    global username, username_window
    chat_box.insert(tk.END, f"Welcome, {username.get()}!\n")
    username_window.destroy()

# Створення вікна
root = tk.Tk()
root.title("Chat Client")

# Область для відображення чату
chat_box = tk.Text(root, width=40, height=10)
chat_box.pack(padx=10, pady=10)

# Поле введення
entry_field = tk.Entry(root, width=30)
entry_field.pack(padx=10, pady=10)

# Кнопка для надсилання повідомлення
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Логіка підключення до сервера
connect_to_server()

root.mainloop()

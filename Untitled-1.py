import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

print(get_ip_address())

import socket

def get_computer_name():
    return socket.gethostname()

print(get_computer_name())

import getpass

def get_username():
    username = getpass.getuser()
    return username

print(get_username())

print("По всем вопросам, просьба обращаться: Отдел поддержки пользователей\n")
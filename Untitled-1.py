import socket

def get_ip_address():                                 #Вывод ip-адреса компьютера
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

print("Ваш IP-адрес:" + get_ip_address())

import socket

def get_computer_name():                              #Вывод имени компьютера  
    return socket.gethostname()

print("Имя Вашего компьютера:" + get_computer_name())

import getpass

def get_username():                                    #Вывод имени залогированного пользователя
    username = getpass.getuser()
    return username

print("Имя пользователя:" + get_username())

print("По всем вопросам, просьба обращаться: Отдел поддержки пользователей")    #Вывод контактной информации
print("Тел.: 55555; +7(8617) 602555")
print("email: 55555@ncsp.com")
print("https://help.ncsp.com")
print("Портал Новороссийского Морского Торгового Порта: https://www.webportal.ncsp.com")
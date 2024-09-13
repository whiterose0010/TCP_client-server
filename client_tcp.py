import socket

target_host = 'www.kahaba.net'
target_port = 80

# membuat sebuah objek socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# terhubung dengan klien
client.connect((target_host, target_port))

# mengirim data
client.send(b"GET / HTTP/1.1\r\nHost: kahaba.net\r\n\r\n")

# menerima data
response = client.recv(4096)

print(response.decode())
client.close()
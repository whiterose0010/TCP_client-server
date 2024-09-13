import socket

target_host = '192.168.87.150'
target_port = 9998

# membuat sebuah objek socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# terhubung dengan klien
client.connect((target_host, target_port))

# mengirim data dengan tipe data Byte
client.send(b"....") 

# menerima data
response = client.recv(4096)

print(response.decode())
client.close()
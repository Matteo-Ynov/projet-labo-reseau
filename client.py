import socket
from threading import Thread

emu = input("n64, gamecube, ds ? ")
ip_dict = {
   "n64": "192.168.117.132",
   "gamecube": "192.168.117.133",
   "ds": "192.168.117.128"
}

command_dict = {
   "gamecube": "flatpak run org.DolphinEmu.dolphin-emu -e /home/matteo/Documents/Gamecube/Super\ Smash\ Bros\ Melee.iso",
   "ds": "desmume /home/matteo/Documents/DS/Pokemon\ Diamond.nds",
   "n64": "m64py /home/matteo/Documents/N64/Super\ Mario\ 64.n64"
}


SERVER_HOST = ip_dict[emu]
SERVER_PORT = 5002
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

to_send = command_dict[emu]
s.send(to_send.encode())
s.close()


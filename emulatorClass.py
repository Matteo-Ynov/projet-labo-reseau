class Emulator:
    def __init__(self) -> None:

        self.ip_dict = {
            "n64": "192.168.117.132",
            "gamecube": "192.168.117.133",
            "ds": "192.168.117.128",
        }


        self.command_dict = {
            "gamecube": "flatpak run org.DolphinEmu.dolphin-emu -e /home/matteo/Documents/games/",
            "ds": "desmume /home/matteo/Documents/games/",
            "n64": "m64py /home/matteo/Documents/games/",
        }

        self.game_dict = {
            "gamecube": {
                "name": "",
            },
            "ds": {
                "Chinatown Wars": "Grand\ Theft\ Auto\ -\ Chinatown\ Wars.nds",
                "Mario Kart": "Mario\ Kart.nds",
                "Bowser's Inside Story": "Mario\ &\ Luigi\ -\ Bowser's\ Inside\ Story.nds",
                "Mario Party": "Mario\ Party.nds",
                "New Super Mario Bros": "New\ Super\ Mario\ Bros.nds",
                "Pokemon Diamond": "Pokemon\ Diamond.nds",
                "Pokemon HeartGold": "Pokemon\ HeartGold.nds",
                "Pokemon Platinum": "Pokemon\ Platinum.nds",
                "Pokemon SoulSilver": "Pokemon\ SoulSilver.nds",
                "Pokemon White": "Pokemon\ White.nds",
                "Super Mario 64": "Super\ Mario\ 64.nds",
                "Phantom Hourglass": "The\ Legend\ of\ Zelda,\ Phantom\ Hourglass.nds",
                "Spirit Tracks": "The\ Legend\ of\ Zelda,\ Spirit\ Tracks.nds",
            },
            "n64": {
                "name": "",
            },
        }

    def build_launch_command(self, emu, name):
        return f"{self.command_dict[emu]}{self.game_dict[emu][name]}"


# try:
#     emu = self.game
#     SERVER_HOST = emulator.ip_dict[emu]
#     SERVER_PORT = 5003
#     s = socket.socket()
#     print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
#     s.connect((SERVER_HOST, SERVER_PORT))
#     print("[+] Connected.")

#     def listen_for_messages():
#         while True:
#             message = s.recv(1024).decode()
#             print("\n" + message)

#     t = Thread(target=listen_for_messages)
#     t.daemon = True
#     t.start()

#     to_send = emulator.build_launch_command(emu, "Mario Kart")
#     s.send(to_send.encode())
#     s.close()
# except:
#     pass
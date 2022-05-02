import time
import requests
import json
import websockets, asyncio
import socket
import winsound
import re
import threading
import random as rnd


class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


def beeep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 5000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    requests.post('https://api.mynotifier.app',
                  {"apiKey": 'ea77bfbe-d789-441c-886e-22e8f0d4143b', "message": "hozoooooor",
                   "description": "get on nigga",
                   "type": "info"})


th = threading.Thread(target=beeep)


async def sendAlive(websocket):
    while True:
        await websocket.send("imalive")


regex = r"\*[\d]+"
# 3606 ---> ssc2
# 195 ---> movahed
cc = ["s", "user", "join",
      {"origin": "vc.sharif.edu", "app_id": 396717, "room_id": 195, "server_id": 1, "customer_id": 1,
       "username": "",
       "password": "",
       "nickname": "هومان کشوری",
       "platform": {"version": "12.5.6", "os": 0, "browser": 0}}
      ]
ob = json.dumps(cc)

obb = ob.encode()


async def responseFunc(uri):
    ntf = True
    tries = 5
    async with websockets.connect(uri) as websocket:
        # await asyncio.sleep(0.003)
        websocket.send("imalive")
        await websocket.send(ob)
        # threading.Thread(target=sendAlive(websocket)).start()
        while True:
            # await asyncio.sleep(0.001)
            await websocket.send("imalive")
            obj = await websocket.recv()
            # await asyncio.sleep(0.003)
            # if type(obj) != list:
            if obj != 'imalive':
                obj = json.loads(obj)
                obj = obj[-1]
                if obj.get('text'):
                    print(obj.get('text'))
                    if re.match(regex, obj.get('text')):
                        tries -= 1
                        if ntf and tries == 0:
                            await websocket.send(
                                json.dumps(["s", "chat", "message-new", {"id": 1000757596, "text": "*99105667کشوری"}]))
                            beeep()
                            return
                            ntf = False
                print(obj)
            # else:
            #     print(obj)


url = "wss://vc.sharif.edu/server"
asyncio.get_event_loop().run_until_complete(responseFunc(url))

# for matchNum, match in enumerate(matches, start=1):
#     print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
#                                                                         end=match.end(), match=match.group()))

# # echo-client.py
#
# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(obb)
#     data = s.recv(1024)
#
# print(f"Received {data!r}")

import websocket
import keyboard
import json
import time

# Variables
running = True

# Connect to WebSocket server
ws = websocket.WebSocket()
ws.connect("ws://192.168.4.1:8765")
print("Connected to WebSocket...!")
time.sleep(1)
print("Now Running...")

while(running):
    if keyboard.is_pressed("w") and keyboard.is_pressed("d"):
        ws.send('{A:"false", K:["70","70"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
        ws.send('{A:"false", K:["70","-70"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
        ws.send('{A:"false", K:["-70","70"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("s") and keyboard.is_pressed("a"):
        ws.send('{A:"false", K:["-70","-70"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("w"):
        ws.send('{A:"false", K:["0","70"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("d"):
        ws.send('{A:"false", K:["70","0"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("s"):
        ws.send('{A:"false", K:["0","-70"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("a"):
        ws.send('{A:"false", K:["-70","0"]}')
        time.sleep(0.1)
    elif keyboard.is_pressed("f"):
        print("Exiting!")
        ws.close()
        break
    else:
        ws.send('{A:"false", K:["0","0"]}')
        time.sleep(0.1)

# # Ask the user for some input and transmit it
# # str = 'A:1'
# ws.send('{A:"false", K:["70","0"]}')

# time.sleep(5)
# ws.send('{A:"false", K:["0","0"]}')
# time.sleep(5)

# ws.send('{A:"false", K:["70","0"]}')
# result = ws.recv()
# print("Received: " + result)
# time.sleep(5)
# # # Gracefully close WebSocket connection
# ws.close()
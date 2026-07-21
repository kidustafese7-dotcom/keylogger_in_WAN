# Keylogger and Webhook Server

This repository contains two main scripts:

1. **Keylogger**: Captures keyboard input and sends logs to a specified webhook URL periodically.
2. **HTTP Server**: Receives logs sent by the keylogger, decodes, displays, and saves them to a file.

---

## 1. Keylogger Script

### Description
This script listens for keyboard events and buffers the keystrokes. Every 10 seconds, it sends the accumulated logs to a specified webhook URL via HTTP POST request.

### Usage
- Replace the `WEBHOOK_URL` variable with your webhook or server URL.
- Ensure port forwarding is correctly set up if running behind NAT or firewall.
- Run the script with Python 3:
```bash
python keylogger.py
      Code Overview

Uses pynput to monitor key presses.
Uses requests to send logs over the internet.
Implements threading to handle log sending asynchronously.
Buffers keystrokes and sends them at regular intervals.


2. HTTP Server Script
Description
This server listens on port 6060 for incoming POST requests containing logs. It decodes URL-encoded data, displays it on the terminal, and appends it to a file named server_logs.txt.
Usage

Run the server script:


          
            
            
          
          python server.py
      
Ensure port 6060 is open and port forwarding is set up if necessary.

Code Overview

Uses http.server for handling HTTP requests.
Processes POST data, decodes URL-encoded content.
Prints logs to console.
Saves logs to server_logs.txt.


Notes

Use responsibly and ethically.
Ensure proper permissions and legal compliance before deploying or using such scripts.
These scripts are intended for educational or authorized testing purposes only.


License
This project is for educational purposes only. Use responsibly.

Contact
For questions or support, contact [Your Name/Email].

Disclaimer: This code can be used maliciously. I do not endorse illegal activities. Use it responsibly and ethically.

          
            
            
          
          

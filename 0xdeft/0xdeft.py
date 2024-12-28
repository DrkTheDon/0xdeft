#!/usr/bin/env python3

# Global imports
import os
import sys
import random
import time
import traceback # Erorr Message
import platform
from pystyle import Colors

## Global Defines
author = "0xbhoru"
error_ans = "\n---> Please write the issue code in https://github.com/DrkTheDon/0xdeft/issues <---\n"


def init(): ## Init script, check if OS is Linux or other. If !Linux then quit.
    try:
        if os.name == 'nt':
            print("\n you are using Windows OS please, switch to a Debain/Linux OS for 0xdeft to work.")
            time.sleep(1.5)
            os.system('cls')
            quit()
        else:
            os.system("clear")
            print(f"\nFOUND OS: {platform.platform(terse=True)}")
            time.sleep(1.5)
            os.system("clear")
    except Exception:
        traceback.print_exc()
        print(error_ans)
        quit()

def clearcmd():
    os.system("clear")


def art(): # Self explanatory
    print("""
   __             __             ___  __      
 /'__`\          /\ \          /'___\/\ \__   
/\ \/\ \  __  _  \_\ \     __ /\ \__/\ \ ,_\  
\ \ \ \ \/\ \/'\ /'_` \  /'__`\ \ ,__\\ \ \/  
 \ \ \_\ \/>  <//\ \L\ \/\  __/\ \ \_/ \ \ \_ 
  \ \____//\_/\_\ \___,_\ \____\\ \_\   \ \__\  
   \/___/ \//\/_/\/__,_ /\/____/ \/_/    \/__/
                                              
                                              
""", Colors.red_to_blue) ## FIX PYSTYLE BUG !!!
    


def main():
    init()
    art()


main()

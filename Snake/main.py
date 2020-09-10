'''
TERMINAL SNAKE

    STRUCTURE:

        main.py 
            imports modules, set necessary classes and trigger run events
        
        kbpoller.py 
            listens and return keyboard input by user

        graphics.py
            sets scene and elements in position and render

        elements.py
            objects and their behaviour

    REQUIREMENTS:

        os, time, queue, threading, random, sys, termios, attexit, select

            Windows:
                msvcrt

'''
import kbpoller
import threading
import time

def run():
    threading.Thread(target=kbpoller.listen, daemon=True).start()
    while True:
        print(kbpoller.key)
        time.sleep(2)


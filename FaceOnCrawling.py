#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  FaceOnCrawling.py
#  
#  Copyright 2019 rob <rob@Elementary-OS>
#  

import urllib.request as urllib2
import urllib.error
from colorama import Fore, Back, Style
import os, time, sys, argparse

#texto animado
textanim = "..."
#abre o aquivo de texto
f=open("link.txt","r")
#coloca o texto do arquivo na variavel $link
link=f.read()
#fecha o arquivo
f.close()

#cria a instancia para os argumentos
parser = argparse.ArgumentParser(description='@ FaceOnCrawling by Rob @')
#cria o argumento url
parser.add_argument('-u',"--url", required=False, help= Fore.YELLOW+"[=]Escreva o link do perfil a ser verificado.", default="")
#adiciona os argumentos na variavel args
args = parser.parse_args()

# cria função base
def crawveify(reston,crawveify):
    #tentar:
    try:
        print(Fore.YELLOW+"[~] Localizando perfil e verificando", end="")
        #inicia o texto animado
        for letra in textanim:
            print(".", end = '', flush = True)
            time.sleep(0.3)
        
        #se o link estiver vazio e o argumento url tambem:
        if link ==  "" and args.url == "":
            #Imprime que está a faltar link
            print(Fore.RED+"\n[-] Vocẽ não colocou nenhum link. :0")
            #fecha o programa
            sys.exit(0)
        #se a variavel link estiver vazia mas o argumento conter algo:
        elif link == "" and args.url != "":
            # faz a requisição web usando o link do argumento
            res = urllib2.urlopen(args.url)
        # se o argumento estiver vazio mas a variavel link não:
        elif args.url == "" and link != "":
            #faz a requisição web através do link da variavel
            res = urllib2.urlopen(link)
    #se não funcionar:
    except urllib.error.HTTPError as e:
        # e retornar o erro 404 que significa que a pagina não exite:
        if e.code == 404:
            #Imprime que a pagina está desativada ou não existe
            print (Fore.RED + "\n[-] Infelizmente o perfil está desativado, ou o link não existe. T-T")
    #se não funcionar e retornar um erro de internet:
    except urllib.error.URLError:
            #imprime que não foi possivel localizar o link e para fazer uma verificação da internet
            print(Fore.RED+"\n[-] Infelizmente não foi possivel localizar o perfil, verifique sua conexão. :0")
    #se o usuario interromper com CTRL + C
    except KeyboardInterrupt:
        #imprime mensagem de tchau
        print(Fore.RED+"\n[-] Programa Interrompido.")
        print(Fore.GREEN+"[*] Espero ter ajudado, até mais!! :D")
        print(Fore.BLUE+">< FaceOnCrawling by Rob ><")
        # e fecha o script
        sys.exit(0)
    #se não retornar erro:
    else:
        #imprima que o perfil está ativo
        print(Fore.GREEN+"\n[*] Obah! O perfil está ativo!!! :3")
        sys.exit(0)
    #após acabar a função base, chamar a função secundaria do tempo
    reston(crawveify)
        
# função de tempo
# OPCIONAL
def reston(crawveify):
    #tenta:
    try:
        #imprime aguarde
        print(Fore.YELLOW+"[~] Aguardando até a nova verificação", end="")
        #anime o texto
        for letra in textanim:
                print(".", end = '', flush = True)
                time.sleep(0.3)
        # TEMPO ATÉ A NOVA VERIFICAÇÃO EM SEGS. OPCIONAL
        # tempo atual 5 minutos
        time.sleep(300)
        #imprime que o tempo acabou
        print(Fore.GREEN+"\n\n[*] Pronto, reverificando agora, mantenha as esperanças!!! :)")
        #chama a função da verificação novamente
        crawveify(reston,crawveify)
    #se o usuario cancelar com CTRL + D
    except KeyboardInterrupt:
        #imprimir mensagem de tchau
        print(Fore.RED+"\n[-] Programa Interrompido.")
        print(Fore.GREEN+"[*] Espero ter ajudado, até mais!! :D")
        print(Fore.BLUE+">< FaceOnCrawling by Rob ><")
        #fechar o script
        sys.exit(0)

# Starta a função base
crawveify(reston,crawveify)

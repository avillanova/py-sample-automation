import sys
import glob

import os
raiz = os.getcwd()
pastas = []


def setUp():
    getDirs(raiz)
    os.chdir(raiz)
    for pasta in pastas:
        sys.path.append(pasta)
   # print(sys.path)

def getDirs(diretorio):
     os.chdir(diretorio)
     diretorio = diretorio+"\\"
     for item in glob.glob("*"):
        if os.path.isdir(diretorio+item):
            pastas.append(diretorio+item)
            getDirs(diretorio+item)
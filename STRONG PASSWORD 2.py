#!/usr/bin/python3
# Author L. Moreira
#DATE 10/06/2021 : 13H:22
# --------------------------------------Requisitos ----------------------------------------
# -------instalar termcolor--------para obter cores-----------no cprint--------------------
# -------instalar join--------para concatenar elementos do vector--------------------------
import random
import sys
import time
import string
import join

import numpy as np
from termcolor import colored, cprint


cprint('O número minino das caracteres (MAIÚSCULA + minuscula + números + caracteres especiais) são 6: ', 'blue', attrs=['concealed'], file=sys.stderr)
time.sleep(0.03)
max_Ma = int(input('Digite o número máximo para as LETRAS MAIÚSCULAS : '))
max_mi = int(input('Digite o número máximo para as letras minusculas: '))
max_nr = int(input('Digite o número máximo para os números: '))
max_str = int(input('Digite o número máximo para as caracteres especiais '))
total = max_Ma+max_mi+max_str+max_nr


if total < 6:
    cprint("O número minimo dos caracteres tem que ser maior do que 5 !!!", 'red', attrs=['concealed'], file=sys.stderr)
    exit()


else:
    lista1 = list(string.ascii_lowercase)
    lista2 = list(string.ascii_uppercase)
    lista3 = list(string.digits)
    lista4 = list(string.punctuation)

    random_index1 = random.choices(lista1, k=max_Ma)
    random_index2 = random.choices(lista2, k=max_mi)
    random_index3 = random.choices(lista3, k=max_nr)
    random_index4 = random.choices(lista4, k=max_str)
   

    random_indexALL = np.concatenate([random_index1,random_index2,random_index3,random_index4])

    random_indexALLP = random.shuffle(random_indexALL)

cprint("PASSWORD", 'blue', attrs=['concealed'], file=sys.stderr)
cprint("".join(random_indexALL), 'green', attrs=['concealed'], file=sys.stderr)


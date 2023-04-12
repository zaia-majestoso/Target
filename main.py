import os
from collections import deque
import random
import time
import numpy as np


def saida(method):
  for i in files:
    with open("output.txt", "a+") as f:

      f.write(f"\n---{i}---\n\nmetodo: {method}\ncontagem de seleções: {(files[i]['HIT'] + files[i]['MISS'])}\ncache hit: {files[i]['HIT']} vezes\ncache miss: {+files[i]['MISS']}\navarege time to open the file in ns: {(files[i]['AVG_TIME']/(files[i]['HIT'] + files[i]['MISS']))}\n")

      if files[i]['HIT'] > 0:
        f.write(f"cache hit average time in ns: {(files[i]['AVG_TIME_HIT']/(files[i]['HIT']))}\n")
      else:
	      f.write(f"cache hit average time in ns: {(files[i]['AVG_TIME_HIT'])}\n")   
				
      if files[i]['MISS'] > 0:
      	f.write(f"cache miss average time in ns: {(files[i]['AVG_TIME_MISS']/(files[i]['MISS']))}\n")
      else:
        f.write(f"cache hit average time in ns: {(files[i]['AVG_TIME_MISS'])}\n")   
					
dir_path = 'textos'
CACHE_SIZE = 10
cache = deque(maxlen=CACHE_SIZE)
tabelaHash = {}
files = {}
Trinta_Quarenta = []
USERS_1 = ["FRANK", "VINI", "DUARDO"]
USERS_2 = ["CAIKE", "HABBIBS", "LEON S. KENNEDY"]
USERS_3 = ["ANTONIO", "LAU", "RENREN"]

for i in range(30, 41):
  Trinta_Quarenta.append(
    sorted(os.listdir("textos"), key=lambda x: (x.split()[0]))[i])


#MODOS DE SORTEIO
def selecionarandom(function):

  Start = time.time_ns()

  selecionado = random.choice(os.listdir(dir_path))
  t = function(selecionado)[1]

  End = time.time_ns()
  files[selecionado]["AVG_TIME"] += (End - Start)

  if t == 1:
    files[selecionado]["AVG_TIME_HIT"] += (End - Start)
  else:
    files[selecionado]["AVG_TIME_MISS"] += (End - Start)


def selecionar30e40(function):

  Start = time.time_ns()

  choice = random.uniform(1.0, 10.0)

  if choice >= 1.0 and choice <= 3.3:

    selecionado = random.choice(Trinta_Quarenta)

  else:

    selecionado = random.choice(os.listdir(dir_path))

    while selecionado in Trinta_Quarenta:

      selecionado = random.choice(os.listdir(dir_path))

  t = function(selecionado)[1]

  End = time.time_ns()
  files[selecionado]["AVG_TIME"] += (End - Start)

  if t == 1:
    files[selecionado]["AVG_TIME_HIT"] += (End - Start)
  else:
    files[selecionado]["AVG_TIME_MISS"] += (End - Start)


def poisson(function):

  Start = time.time_ns()

  arquivos = os.listdir(dir_path)

  distribuicao_poisson = np.random.poisson(5, len(arquivos))
  distribuicao_poisson = distribuicao_poisson / distribuicao_poisson.sum()

  selecionado = np.random.choice(arquivos, p=distribuicao_poisson)

  t = function(selecionado)[1]
  print(t)

  End = time.time_ns()
  files[selecionado]["AVG_TIME"] += (End - Start)

  if t == 1:
    files[selecionado]["AVG_TIME_HIT"] += (End - Start)
  else:
    files[selecionado]["AVG_TIME_MISS"] += (End - Start)


def usuarioSimulacao(listaUser, user, func):

  if user == 3:
    return print("aaa")

  with open("output.txt", "a") as f:
    f.write(
      f"\n-----------------USUÁRIO: {listaUser[user]}-----------------\n\n-----------------Função:{func.__name__}-----------------\n\n-----------------30% 40%-----------------\n"
    )

  user3040(func)
  saida("30% 40%")
  files.clear()
  user += 1

  with open("output.txt", "a") as f:
    f.write(
      f"\n-----------------USUÁRIO: {listaUser[user]}-----------------\n\n-----------------Função:{func.__name__}-----------------\n\n-----------------Random-----------------\n\n"
    )
  userrd(func)
  saida("Random")
  files.clear()
  user += 1

  with open("output.txt", "a") as f:
    f.write(
      f"\n-----------------USUÁRIO: {listaUser[user]}-----------------\n\n-----------------Função:{func.__name__}-----------------\n\n-----------------Poisson-----------------\n\n"
    )
  userpoisson(func)
  saida("Poisson")
  files.clear()


def userrd(func):
  for i in range(200):
    selecionarandom(func)


def user3040(func):
  for i in range(200):
    selecionar30e40(func)


def userpoisson(func):
  for i in range(200):
    poisson(func)


# METODOS
def lfu(arquivo):

  global tabelaHash

  arqv = os.path.join(dir_path, arquivo)

  if arquivo not in files:
    files[arquivo] = {
      "HIT": 0,
      "MISS": 0,
      "AVG_TIME": 0.0,
      "AVG_TIME_HIT": 0.0,
      "AVG_TIME_MISS": 0.0
    }

  if arquivo in tabelaHash:
    tabelaHash[arquivo]['contador'] += 1
    files[arquivo]["HIT"] += 1
    with open(arqv, "r") as f:
      conteudo = f.read()
    return conteudo, 1

  else:
    with open(arqv, "r") as f:
      conteudo = f.read()

    if len(tabelaHash) >= CACHE_SIZE:

      min_use = min(tabelaHash, key=lambda x: tabelaHash[x]['contador'])

      del tabelaHash[min_use]

    files[arquivo]["MISS"] += 1

    tabelaHash[arquivo] = {'contador': 0, 'CONTEÚDO': conteudo}

    tabelaHash = dict(
      sorted(tabelaHash.items(), key=lambda x: x[1]['contador']))

    return conteudo, 0


def fifo(arquivo):

  if arquivo not in files:
    files[arquivo] = {
      "HIT": 0,
      "MISS": 0,
      "AVG_TIME": 0.0,
      "AVG_TIME_HIT": 0.0,
      "AVG_TIME_MISS": 0.0
    }

  for cacheFile in cache:

    if cacheFile["FILE NAME"] == arquivo:

      files[arquivo]["HIT"] += 1

      return cacheFile["FILE CONTENTS"], 1
  else:
    arqv = os.path.join(dir_path, arquivo)
    files[arquivo]["MISS"] += 1

    if len(cache) >= CACHE_SIZE:

      cache.pop()

    with open(arqv, "r") as f:
      file_contents = f.read()

    cache.appendleft({'FILE NAME': arquivo, 'FILE CONTENTS': file_contents})

    return file_contents, 0


def lru(arqv):
  if arqv not in files:
    files[arqv] = {
      "HIT": 0,
      "MISS": 0,
      "AVG_TIME": 0.0,
      "AVG_TIME_HIT": 0.0,
      "AVG_TIME_MISS": 0.0
    }

  for cached_file in cache:
    if cached_file["FILE NAME"] == arqv:
      files[arqv]["HIT"] += 1
      cache.remove(cached_file)
      cache.appendleft(cached_file)

      return cached_file['FILE CONTENTS'], 1

  arquivo = os.path.join(dir_path, arqv)
  files[arqv]["MISS"] += 1

  with open(arquivo, "r") as f:
    file_contents = f.read()

  if len(cache) >= CACHE_SIZE:

    cache.pop()

  cache.appendleft({'FILE NAME': arquivo, 'FILE CONTENTS': file_contents})

  return file_contents, 0


while True:
  option = int(input("-1: Simulação, 0: Sair, 1: Ler Arquivo: "))

  if option == 1:

    selecionado = input("digite o número do arquivo: ")

    print(fifo("arquivo_" + selecionado + ".txt")[0])

  elif option == -1:

    for i in range(3):

      user = 0
      tabelaHash.clear()
      cache.clear()

      if i == 0:
        n = usuarioSimulacao(USERS_1, user, fifo)

      elif i == 1:
        usuarioSimulacao(USERS_2, user, lru)

      elif i == 2:
        usuarioSimulacao(USERS_3, user, lfu)

  elif option == 0:
    break

  else:
    print(files)
    print("Digite Novamente")

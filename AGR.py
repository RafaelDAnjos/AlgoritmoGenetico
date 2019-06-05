import random
import matplotlib.pyplot as plt

limSup = 10
limInf = -10
populacao = []
dominio = [limInf,limSup]
tamcrom = 10
tampop = int(input("Entre com o tamanho da população: "))
numgera = int(input("Insira o numero de gerações: "))

def main():


    populacao = Gerapop(tampop,tamcrom)
    avaliados = Avaliar(populacao)
    elite = Melhor(avaliados)

    for i in range(numgera):
        populacao,elite =Torneio(populacao,elite)
        taxa = random.uniform(0,1)
        if taxa<=0.6:
            populacao,elite = Crossover(populacao,elite)
        print(populacao)







    return 0
def Crossover(populacao,elite):
    filhos = []
    alfa = 0.5
    beta = random.uniform((-1*alfa),(1+alfa))
    while len(filhos)<len(populacao):
        p1 = random.choice(populacao)
        p2 = random.choice(populacao)
        son = p1+beta*(p2-p1)
        filhos.append(son)

    return filhos,elite

def Torneio(populacao,elite):
    avaliados = Avaliar(populacao)
    selecionados =[]
    while len(selecionados)<tampop:
        cand1 = random.choice(avaliados)
        cand2 = random.choice(avaliados)
        if cand1[1]>cand2[1]:
            selecionados.append(cand2[0])
        else:
            selecionados.append(cand1[0])
    avaliados = Avaliar(selecionados)
    elitelocal = Melhor(avaliados)
    if(elite[1]>elitelocal[1]):
        elite = elitelocal

    return selecionados,elite

def Elitismo(selecionados,elite):
    avaliados = Avaliar(selecionados)
    melhor,indice = Melhor(avaliados)
    if elite[1]<avaliados[len(avaliados)-1][1]:
        selecionados[indice] = elite[0]
    if elite[1]>melhor[1]:
        elite = melhor
    return selecionados,elite

def RetornaIndice(a,selecionados):
    for i in range(len(selecionados)):
        if a == selecionados[i]:
            return i
def Melhor(populacao):
    melhor = populacao[0]

    indice = 0
    for i in range(len(populacao)):
        if melhor[1]> populacao[i][1]:
            melhor = populacao[0]
            indice = i
    return melhor,indice
def Avaliar(populacao):
    avaliados  = []
    for i in range(len(populacao)):
        apt = populacao[i]**2 -3*populacao[i] + 4
        avaliados.append([populacao[i],apt])
    return avaliados
def Gerapop(tampop,tamcromo):
    lst = []
    for i in range(tampop):
        ind = ""
        for j in range(tamcromo):
            bit = str(random.randint(0,1))
            ind = ind+bit
        lst.append(Normalizar(ind))
    return lst
def Normalizar(cromo):
    num = converterb_d(cromo)
    x = dominio[0] +((dominio[1]-dominio[0])*((num)/((2**tamcrom)-1)))
    return x
def converterb_d(n):
    decimal = 0
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
       if n[i] == "1":
           decimal = decimal + 2 ** i
    return decimal
main()
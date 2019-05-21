import random
import matplotlib.pyplot as plt

limSup = int(input("Insira o limite Superior do domínio: "))
limInf = int(input("Insira o limite Inferior do domínio: "))

tamcrom = int(input("Insira o tamanho do cromossomo: "))
tampop = int(input("Insira o tamanho da população: "))
numGeracoes = int(input("Insira o numero de gerações: "))
dominio = [limInf, limSup]
def main():
    populacao = []
    avaliados = []
    selecionados = []
    geracao = []
    MatrizResultado = []


    GerarPopulacao(populacao)

    for i in range(numGeracoes):
        avaliados = AvaliarPop(populacao)

        selecionados = Torneio(avaliados, tampop)

        taxamut =0.6
        if(random.uniform(0,1)<=taxamut):
            selecionados = Crossover(selecionados)
        populacao = Mutacao(selecionados)
        avaliados = AvaliarPop(populacao)
        MatrizResultado.append(avaliados)

    Imprimegraf(MatrizResultado)
    print(MatrizResultado)



    return 0

def Imprimegraf(matriz):
    lista = []

    for i in range(len(matriz)):
        melhor = matriz[i][0]
        for j in range(len(matriz[0])):
            if melhor[1]>matriz[i][j][1]:
                melhor = matriz[i][j]
        lista.append(Normalizar(melhor[0]))
    print(lista)        



    plt.plot(lista)
    plt.show()

def converterd_b(n):
    binario = ""
    if (n == 0):
        binario = '00000'
    else:
        while True:

            if n == 0:

                break
            else:
                binario = binario + str(n % 2)
                n = n // 2
        if len(binario) < 5:
            for i in range(5 - len(binario)):
                binario = binario + '0'
        binario = binario[::-1]
    return binario


def converterb_d(n):
    decimal = 0
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2 ** i
    return decimal


def GerarPopulacao(populacao):

    for i in range(tampop):
        bit = ""
        for j in range(tamcrom):

            bit = bit + str(random.randrange(0,2))
        populacao.append(bit)


    return 0


def AvaliarPop(populacao):
    candidatos = []

    for i in range(len(populacao)):
        x = Normalizar(populacao[i])
        print("X: ",x)
        apt = x**2 -3*x + 4
        print("Apt: ",apt)
        candidatos.append([populacao[i], apt])
    return candidatos
def Normalizar(cromo):
    num = converterb_d(cromo)
    x = dominio[0] +((dominio[1]-dominio[0])*((num)/((2**tamcrom)-1)))
    return x
def Selecionarmelhores(avaliados, tampop):
    prob = 0
    maximo = Somatoriofx(avaliados)
    selecionados = []
    for i in range(len(avaliados)):
        prob = prob + avaliados[i][1] / maximo
        avaliados[i].append(prob)
    while len(selecionados) != tampop:
        prob = random.uniform(0, 1)
        for j in range(len(avaliados)):
            if (j == 0):
                if (prob >= 0 and prob <= avaliados[j][2]):
                    selecionados.append(avaliados[j][0])
            else:
                if (prob > avaliados[j - 1][2] and prob <= avaliados[j][2]):
                    selecionados.append(avaliados[j][0])
    return selecionados
def Torneio(avaliados,tampop):
    selecionados = []

    while len(selecionados)<tampop:
        prob1= random.randrange(0,len(avaliados)-1)
        prob2= random.randrange(0,len(avaliados)-1)
        if(avaliados[prob1][1]<avaliados[prob2][1]):
            selecionados.append(avaliados[prob1][0])
        else:
            selecionados.append(avaliados[prob2][0])
    return selecionados

def Crossover(selecionados):

    filhos = []

    for j in range(0,len(selecionados),2):

        filho1 = ""
        filho2 = ""
        caudaf1 = ""
        caudaf2 = ""
        cabecaf1 = ""
        cabecaf2 = ""
        numcross = random.randrange(1, len(selecionados[j]))

        for k in range(len(selecionados[j])):
            if k < numcross:
                cabecaf1 = cabecaf1 + selecionados[j][k]
                cabecaf2 = cabecaf2 + selecionados[j + 1][k]
            else:
                caudaf1 = caudaf1 + selecionados[j][k]
                caudaf2 = caudaf2 + selecionados[j + 1][k]

        filho1 = cabecaf1 + caudaf2
        filhos.append(filho1)
        filho2 = cabecaf2 + caudaf1
        filhos.append(filho2)

    return filhos

def Mutacao(geracao):
    taxamuta = 0.01315846113148461
    novapop = []

    for cromossomo in geracao:
        cromomutado = ""
        for i in range(len(cromossomo)):
            prob = random.uniform(0, 1)
            if (prob <= taxamuta):
                if (cromossomo[i] == "0"):
                    cromomutado = cromomutado + "1"
                else:
                    cromomutado = cromomutado + "0"
            else:
                cromomutado = cromomutado + cromossomo[i]
        novapop.append(cromomutado)
    return novapop


def Somatoriofx(avaliados):
    soma = 0
    for i in range(len(avaliados)):
        soma = soma + avaliados[i][1]
    return soma


main()

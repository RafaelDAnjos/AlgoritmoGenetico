import random

dominio = [1, 31]

tamcrom = int(input("Insira o tamanho do cromossomo: "))
tampop = int(input("Insira o tamanho da população: "))
def main():
    populacao = []
    avaliados = []
    selecionados = []
    geracao = []


    GerarPopulacao(populacao)
    print("população: ", populacao)
    for i in range(5):
        avaliados = AvaliarPop(populacao)
        print("avaliados",avaliados)
        selecionados = Selecionarmelhores(avaliados, tampop)
        geracao = Crossover(selecionados)
        geracao = AvaliarPop(geracao)
        geracao = Selecionarmelhores(geracao, tampop)
        populacao = Mutacao(geracao)
    print("população final: ", populacao)

    return 0


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
    print("CARALHO:",populacao)

    return 0


def AvaliarPop(populacao):
    candidatos = []

    for i in range(len(populacao)):
        apt = (Normalizar(populacao[i])) ** 2
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


def Crossover(selecionados):
    taxacross = 0.6
    pais = []
    filhos = []

    for i in range(len(selecionados)):
        prob = random.uniform(0, 1)

        if prob <= taxacross:
            pais.append(selecionados[i])
        else:
            filhos.append(selecionados[i])

    if len(pais) == 1:
        filhos.append(pais[0])
    for j in range(len(pais) - 1):

        filho1 = ""
        filho2 = ""
        caudaf1 = ""
        caudaf2 = ""
        cabecaf1 = ""
        cabecaf2 = ""
        numcross = random.randrange(1, len(pais[j]))

        for k in range(len(pais[j])):
            if k < numcross:
                cabecaf1 = cabecaf1 + pais[j][k]
                cabecaf2 = cabecaf2 + pais[j + 1][k]
            else:
                caudaf1 = caudaf1 + pais[j][k]
                caudaf2 = caudaf2 + pais[j + 1][k]

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

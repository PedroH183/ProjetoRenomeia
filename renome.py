#! python3

"""
Script que reorganiza a numeração dos arquivo 

EXAMPLE ::
relatorio1.pdf
relatorio2.pdf
relatorio4.pdf 

ele irá identificar que não há o relatorio 3 e renomeiará o relatorio 4 para relatorio 3
e assim por diante, corrigindo a sequencia.
"""


import os, re
from sys import exit
import shutil as sh
from random import randint


def gerar_arq():
    
    """GERAR ARQUIVOS PARA FAZER O SCRIPT RENOMEIAR, SÃO ARQUIVOS DE TESTE"""

    print(os.getcwd())
    for i in range(10):
        with open(f'popli{randint(5,20)}.png',mode='a'):
            print('ok')

    return

def sequencia(prefixo,exten):
    
    """RECONHECER A NUMERAÇÃO DOS ARQUIVOS"""

    regex_num_arq = re.compile(fr"\b({prefixo}(\d\d?\d?)[.]{exten})\b")
    dire = " ".join(os.listdir())
    corres = re.findall(regex_num_arq, dire) # returns a list of tuple ?? 
    #fazer a corres analisar os i na nomenclatura de um dado arquivo e colocar em um grupo !! para substituir

    if corres == []:
        return False
    
    rage_corre = range(len(corres))
    corres = [list(corres[i]) for i in rage_corre] # transforma as tuplas em lista 
    corres = [[corres[i][0], int(corres[i][1])] for i in rage_corre] # transforma o i em um valor inteiro
    corres = sorted(corres, key=lambda corres: corres[1]) # sort by value of file 
    
    return corres

def arquivo():
    
    """PERGUNTANDO AS PROPRIEDADES DO ARQUIVO EM QUESTÃO"""

    prefix = str(input('Digite o prefixo do arquivo\nExemplo :: (relatorio)1, (relatorio)2\n::'))
    exten = str(input('Digite a extensão do arquivo sem o ponto\nExemplo :: .zip, .pdf, .png\n::'))
    
    while True:
    
        esco = str(input('Zerar a numeração ou continuar do valor minimo dos arquivos\nZ: Zerar\nC: Continuar\n[Z/C]::'))
        
        if esco not in ['z','c']:
            print('Digite um valor entre [Z ou C] para ditar como a ordem deve ser feita')
            continue
        
        break
    
    return prefix,exten, esco

def ordenar(valores, desejo):

    """ORDENANDO OS ARQUIVOS COM A NUMERAÇÃO EM ORDEM"""

    # identificar a numeração correta ::
    rage_values = range(len(valores))
    correct_sequ =[]

    for i in rage_values:

        if desejo == 'c' and i == 0: # continuando a ordem pelo menor valor dos arquivos
                correct_sequ.append(valores[i][1])
                continue           

        elif desejo == 'z' and i == 0: # zerar o min valor e recomeçar  
                valores[i][1] = 0
                correct_sequ.append(valores[i][1] + 1 )
                continue
                
        correct_sequ.append(correct_sequ [i-1] + 1)

    valores = [[valores[i][0], valores[i][1], correct_sequ[i]] for i in rage_values]
    del correct_sequ

    #ordenando
    for i in rage_values:

        if valores[i] == valores[-1]:
            pass

        elif valores[i][2] != valores[i+1][1]: # avaliando a ordem e mudando para a ordem correta
            valores[i+1][1] = valores[i][2]
            valores[i+1][2] = valores[i][2] + 1 

        continue

    return valores

def renomear(lista, desejo):

    """Função com o objetivo de renomear todos os arquivos com a sequencia correta"""

    regex_subs = re.compile(r'\d(?:\d?){1,}')
    rage_len = range(len(lista))
    
    for i in rage_len:
    
        #substituindo utilizando regex, mas é possivel importar o prefixo e concatenar em uma string
        
        correct_num_arq = re.sub(regex_subs, str(lista[i][2]), lista[i][0] , count=1)
        # o re.sub funciona substituindo o pattern pelo repl na string !!
        lista[i].append(correct_num_arq)
        # movendo os arquivos para o diretorio atual com o nome trocado 
        sh.move(f'.\{lista[i][0]}',f'.\{lista[i][3]}')

    print(os.getcwd())
    
    return 'ARQUIVOS RENOMEADOS COM A ORDEM CORRETA'



prefixo, extensao, esco = arquivo()
lista = sequencia(prefixo, extensao)

if lista == False:
    exit('Nenhum arquivo com o prefixo e extensão encontrado')

lista = ordenar(lista, esco)
print(renomear(lista, esco))
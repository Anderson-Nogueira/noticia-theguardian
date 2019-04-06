#Programa para pegar uma API, semelhante ao cambio-moedas

from os import system # Importar o método system da biblioteca os
from time import sleep # Importar o método sleep da biblioteca time
from requests import get # Importar o método get da biblioteca requests
import json # Importar a biblioteca JSON
import pandas as pd # Importar biblioteca pandas - referindo ao pandas com pd

import csv

def exportar_csv(s, t, l, nome_arq):
    # Criar o DataFrame para formar a tabela 
    df = pd.DataFrame({'Secao': s, 'Titulos': t, 'Links': l})

    # Importar para CSV
    df.to_csv('%s.csv' % nome_arq, encoding='utf-8-sig', index=False, sep=";")
    #encoding='cp1252' serve para manter a acentuação igual ao encoding acima
    print('Gerando arquivo...\n')
    sleep(2)
    print("Exportado com sucesso!")


def buscar_noticia(dados):
      
    # Criar listas vazias, onde irá armazenar o conteúdo do título e link das noticias
    secao = []
    titulos = []
    links = []

    print("--- Selecione a Opção da Notícia ---")
    print("1 --> Arts")
    print("2 --> Noticias")
    print("3 --> Sports")
    print("4 --> Todas")
    print("0 --> Sair")

    tipo_noticia = int(input("Digite a noticia desejada: "))

    if tipo_noticia == 1:
        tipo_noticia = "Arts"
    elif tipo_noticia == 2:
        tipo_noticia = "News"
    elif tipo_noticia == 3:
        tipo_noticia = "Sport"
    elif tipo_noticia == 4:
        tipo_noticia = 4
    elif (tipo_noticia == 0) or (tipo_noticia > 4):
        exit()
    
    # Laço para pegando a quantidade de noticias e fazer um apende para a lista vazia,
    # no qual será a o valor das chaves, titulos e link, respectivamente.
    # Dependendo do tipo de noticia desejada

    for noticia in dados["response"]["results"]:

        if tipo_noticia == 4: 
            secao.append(noticia['pillarName'])
            titulos.append(noticia['webTitle'])
            links.append(noticia['webUrl'])

        if noticia['pillarName'] == tipo_noticia:
            secao.append(noticia['pillarName'])
            titulos.append(noticia['webTitle'])
            links.append(noticia['webUrl'])

    if len(secao) == 0: #Verifica se houve alguma informação la lista, se houver grava senão gera msg !!!
        print("Não foram encontradas notícias sobre o assunto. Tente mais tarde !!!")
    else:
        nome_arq = str(input("Digite nome do Arquivo: "))
        exportar_csv(secao, titulos, links, nome_arq)
    


def main():

    system("cls") # Limpar a tela antes de mostrar o resultado

    # Realizar a consulta a API do guardian e armazenar na variável URL
    url = 'https://content.guardianapis.com/search?api-key=49ea9a11-be8c-4103-9ee0-02e66afbf026'

    # Usando o método GET da biblioteca JSON, iremos pegar o conteúdo bruto e jogar na variavel RESPOSTA
    resposta = get(url)

    # Testa se o código de retorno foi 200
    if resposta.status_code == 200:
        print('Acessando a base de dados...')
        sleep(2) #Comando para dar uma pausa
        print("Conseguiu acessar base de dados!")
        sleep(1)
        print("Buscando informações das notícias...")
        sleep(2)
        # Caso o código de retorno foi 200, obteve sucesso, então iremos pegar os dados e tratar
        dados = resposta.json()
        buscar_noticia(dados)

    else:
        print("Site com problemas!")



if __name__ == '__main__':
    main()

#OUTRO TESTE
#PRECISA VERIFICAR SE CONSEGUE INSERIR UMA OU MAIS LINHAS NO INICIO DO ARQUIVO

# --- As linhas de Código abaixo, seriam apenas para modo de estudo
# --- Referem-se a inserção de uma linha ao final do Arquivo

#arquivo = open('noticias.csv', 'r') # Abra o arquivo (leitura)
#conteudo = arquivo.readlines()
#conteudo.append('TESTE')   # insira seu conteúdo

#arquivo = open('noticias.csv', 'w') # Abre novamente o arquivo (escrita)
#arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

#arquivo.close()

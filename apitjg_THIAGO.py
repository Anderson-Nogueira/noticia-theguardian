# coding: utf-8
from os import system # Importar o método system da biblioteca os
from time import sleep # Importar o método sleep da biblioteca time
from requests import get # Importar o método get da biblioteca requests
import json # Importar a biblioteca JSON
import pandas as pd # Importar biblioteca pandas - referindo ao pandas com pd

system("cls") # Limpar a tela antes de mostrar o resultado

# Realizar a consulta a API do guardian e armazenar na variável URL
url = 'https://content.guardianapis.com/search?api-key=49ea9a11-be8c-4103-9ee0-02e66afbf026'

# Usando o método GET da biblioteca JSON, iremos pegar o conteúdo bruto e jogar na variavel RESPOSTA
resposta = get(url)

# Testa se o código de retorno foi 200
if resposta.status_code == 200:
    print('Acessando a base de dados...')
    sleep(2)
    print("Conseguiu acessar base de dados!")
    sleep(1)
    print("Buscando informações das notícias...")
    sleep(2)
    # Caso o código de retorno foi 200, obteve sucesso, então iremos pegar os dados e tratar
    dados = resposta.json()
    noticias = dados["response"]["results"]
    
    # Criar listas vazias, onde irá armazenar o conteúdo do título e link das noticias
    titulos = []
    links = []

    # Laço para pegando a quantidade de noticias e fazer um apende para a lista vazia,
    # no qual será a o valor das chaves, titulos e link, respectivamente.
    for noticia in range(len(noticias)):
        titulos.append(noticias[noticia]["webTitle"])
        links.append(noticias[noticia]["webUrl"])

    # Criar o DataFrame para formar a tabela 
    df = pd.DataFrame({'Titulos': titulos, 'Links': links})

    # Importar para CSV
    df.to_csv('Noticias.csv', encoding='cp1252' ,index=False, sep=',')
    print('Gerando arquivo...\n')
    sleep(2)
    print("Exportado com sucesso!")

else:
    print("Site com problemas!")

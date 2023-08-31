import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=";")
print(dados)

media = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
grafico = media.plot(figsize=(14, 10), color ='purple')
grafico.set_visible()
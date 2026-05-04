from collections import deque

grafoConexoes = {}

#Conexões de primeiro grau
grafoConexoes['voce'] = ['bob','claire','alice']

#Conexões de segundo grau
grafoConexoes['bob'] = ['anuj','peggy']
grafoConexoes['claire'] = ['thom','jonny']
grafoConexoes['alice'] = ['peggy']

#Conexões de terceiro grau
grafoConexoes['anuj'] = []
grafoConexoes['thom'] = []
grafoConexoes['jonny'] = []
grafoConexoes['peggy'] = []

#Pesquisar no grafo de conexões a pessoa mais próxima que o nome termina em 'm'
def terminaEmM(nome):
    if nome[-1] == 'm':
        return True
    return False 

filaPesquisa = []
filaPesquisa += grafoConexoes['voce']
encontrouObjetivo = False
contPesquisas = 0
print(filaPesquisa)

while filaPesquisa : #enquanto a lista de pesquisa tiver itens
    pessoa = filaPesquisa.pop(0)
    if terminaEmM(pessoa):
        encontrouObjetivo = True
    else:
        filaPesquisa+=grafoConexoes[pessoa]
    
    print(filaPesquisa)

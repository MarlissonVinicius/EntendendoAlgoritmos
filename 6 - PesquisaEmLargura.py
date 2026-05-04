from collections import deque

grafoConexoes = {}

#Conexões de primeiro grau
grafoConexoes['marlisson'] = ['bob','claire','alice']

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

def pesquisarConexoes(nome): #Função para pesquisar se há alguma pessoa com o nome que termina com a letra m com conexão de enésimo grau com o pessoa passada
    filaPesquisa = deque() #criação da fila 
    filaPesquisa += grafoConexoes[nome] #iniciar a pesquisa adicionando todas as minhas conexões
    pessoasPesquisadas = []
    encontrouObjetivo = False

    while filaPesquisa : #enquanto a lista de pesquisa tiver itens
        pessoa = filaPesquisa.popleft() #retirada do primeiro elemento da fila, que tem tempo de execução O(1)
        if not pessoa in pessoasPesquisadas: #verificar se a pessoa já foi pesquisada para evitar pesquisa dubla ou looping infinito 
            
            if terminaEmM(pessoa):
                encontrouObjetivo = True
                break
            else:
                filaPesquisa+=grafoConexoes[pessoa]
        pessoasPesquisadas.append(pessoa)
    
    resultado = f'Pessoa encontrada: {pessoa}' if encontrouObjetivo else f"Ninguém que possui conexão com {nome} termina com 'm'"
    print(resultado)

pesquisarConexoes('claire')
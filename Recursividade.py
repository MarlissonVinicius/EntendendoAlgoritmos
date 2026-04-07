from time import sleep

def timer(second):
    
    print(f"{second}s")
    sleep(1)

    #caso recursivo - o time é maior que 0, necessário a autochamada  
    if(second < 0):
        return
    #caso Base - o timer é 0m ponto de parada
    else:
        timer(second-1)

#recursão comum - É feito o empilhamento das chamadas e após chegar no caso base ela volta executando as funções antes chamadas 
def fatorial(num):
    #caso base
    if num == 1:
        return 1
    #caso recursivo
    else:
        return num*fatorial(num-1)

#recursão de cauda - O valor é guardado em uma variável que é repassada como parâmetro na próxima chamada. 
def fatorialCauda(num,acum):
    #caso base
    if num == 0:
        return acum
    #caso recursivo
    else:
        return(fatorialCauda(num-1,acum*num))

def Main():
    print(fatorial(4))

Main()
def SomarArrayIte(nums):
    acum=0
    for i in range(len(nums)):
        acum+=nums[i]
    return acum

def SomarArrayRecur(nums):
    #caso base - quando o array estiver vazio
    if len(nums) == 0:
        return 0
    #caso recursivo
    else:
        return nums[0] + SomarArrayRecur( nums[1:])

def contItens(list,cont=0):
    if(len(list) == 0):
        return cont
    else:
        return contItens(list[1:], cont+1) 

def maiorNum(list,maior=0):
    if(len(list) == 0):
        return maior
    else:
        print(maior)
        maior = list[0] if list[0] > maior else maior
        return maiorNum(list[1:],maior)

def Main():
    nums = [3,6,1,4,5]
    print(maiorNum(nums))

    

Main()
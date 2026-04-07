def Quick(list):
    if len(list) < 2:
        return list
    else:
        pivo = list.pop(0)
        leftList = []
        rigthList = []

        for i in list:
            leftList.append(i) if i < pivo else rigthList.append(i)
        return Quick(leftList)+[pivo]+Quick(rigthList)
    
def Main():
    num = [5,2,8,9,0]

    print(Quick(num))

Main()
def SelectionSort(listaDes):
    listaOrd = []

    while len(listaDes) > 0:
        menor = listaDes[0]

        for i in range(len(listaDes)):
            if(menor > listaDes[i]):
                menor = listaDes[i]
        listaOrd.append(menor)
        listaDes.remove(menor)
        print(listaOrd)

def Main():
    listaDesordenada = [45, 12, 89, 3, 67, 24, 91, 56, 18, 72,
5, 39, 84, 27, 63, 10, 95, 41, 76, 14,
58, 2, 99, 33, 70, 21, 87, 6, 50, 30,
93, 16, 61, 8, 74, 28, 97, 43, 65, 11,
52, 1, 80, 36, 69, 19, 90, 25, 47, 7,
82, 31, 60, 13, 96, 40, 71, 22, 88, 4,
54, 17, 79, 29, 92, 34, 66, 9, 73, 26,
98, 44, 57, 15, 81, 32, 64, 20, 85, 37,
59, 23, 94, 42, 68, 35, 77, 49, 86, 53,
38, 62, 46, 75, 100, 51, 83, 55, 78, 48]
    
    SelectionSort(listaDesordenada)

Main()
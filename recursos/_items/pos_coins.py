from Clases._objetos.clase_item import Items

pos_coins_nivel1 = [[370,565],[458,565],[545,565],[640,535],[728,535],[815,535],[890,465],[965,465],[1043,395],[830,335],[905,335],[460,265],[598,265],[735,265],[325,235],[163,235],[0,235]]

list_coins_nivel1 = []

for i in range(len(pos_coins_nivel1)):
    list_coins_nivel1.append(Items('coin',(25,25),pos_coins_nivel1[i]))
    list_coins_nivel1[i].definir_limite()

# POSICION DE LAS MONEDAS DE NIVEL 2 ----------------------------------------------------------------

pos_coins_nivel2 = [[520,615],[595,615],[320,615],[395,615],[120,615],[195,615],[28,555],[120,465],[195,465],[372,345],[552,345],[732,345],[900,345],[965,345],[1028,275],[800,205],[865,205],[250,165],[488,165],[725,165],[63,165]]

list_coins_nivel2 = []

for i in range(len(pos_coins_nivel2)):
    list_coins_nivel2.append(Items('coin',(25,25),pos_coins_nivel2[i]))
    list_coins_nivel2[i].definir_limite()


# POSICION DE LAS MONEDAS DE NIVEL 3 ----------------------------------------------------------------

pos_coins_nivel3 = [[0,465],[95,465],[200,505],[295,505],[400,545],[655,545],[760,505],[855,505],[960,465],[1055,465],[18,365],[1038,365],[140,325],[215,325],[840,325],[915,325],[320,265],[735,265],[528,185],[148,125],[285,125],[423,125],[632,125],[769,125],[907,125]]

list_coins_nivel3 = []

for i in range(len(pos_coins_nivel3)):
    list_coins_nivel3.append(Items('coin',(25,25),pos_coins_nivel3[i]))
    list_coins_nivel3[i].definir_limite()

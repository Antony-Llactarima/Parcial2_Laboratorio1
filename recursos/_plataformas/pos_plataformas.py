

lista_pos1 = [(0,650), (370,600), (640,570), (890,500), (1030,430), (830, 370), (460, 300), (0,270)]

lista_tam1 = [(300, 70), (200,120), (200,150), (100,580), (50,650), (100,25), (300,25), (350,25)]

lista_limit1 = []

for i in range(len(lista_pos1)):
    lista_limit1.append((lista_pos1[i][0] + lista_tam1[i][0], lista_pos1[i][1] + lista_tam1[i][1]))

# ----------------------------------------------------------------

lista_pos2 = [(720,650),(520,650),(320,650),(120,650),(0,580),(120,500),(320,450),(370,380),(550,380),(730,380),(900,380),(1000,310),(800,240),(250,200),(0,200)]

lista_tam2 = [(360,70),(100,120),(100,150),(100,580),(80,25),(100,25),(500,25),(30,70),(30,70),(30,70),(100,25),(80,25),(100,25),(500,25),(150,25)]

lista_limit2 = []

for i in range(len(lista_pos2)):
    lista_limit2.append((lista_pos2[i][0] + lista_tam2[i][0], lista_pos2[i][1] + lista_tam2[i][1]))

# ----------------------------------------------------------------

lista_pos3 = [(000,500),(200,540),(400,580),(760,540),(960,500),(000,400),(1020,400),(140,360),(840,360),(320,300),(528,220),(148,160),(632,160)]

lista_tam3 = [(120,270),(120,180),(280,140),(120,180),(120,220),(60,25),(60,25),(100,25),(100,25),(440,25),(24,80),(300,25),(300,25)]

lista_limit3 = []

for i in range(len(lista_pos3)):
    lista_limit3.append((lista_pos3[i][0] + lista_tam3[i][0], lista_pos3[i][1] + lista_tam3[i][1]))

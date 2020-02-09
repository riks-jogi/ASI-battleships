from probabilityTable import probtable
import numpy as np

laevad = [5,4,3,3,2]

playermatrix = np.array([[0,0,0,0,0,0,0,0,0,0,2], #matrix kus hoitakse infot käikude kohta. need kahed on stopperid. ära puutu
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,1,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,1,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [2,2,2,2,2,2,2,2,2,2,2]])

outputmatrix = np.array([[0,0,0,0,0,0,0,0,0,0], #matrix mille peale liidetakse tõenäosus. iga kasutusega taastatakse algne seis
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0]])


def resetOutput(): #taastab tõenäosustabeli algse seisu
    global outputmatrix
    outputmatrix = np.array([[0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0]])

def playerLasi(): #kontrollib AI laevade seisu ja updateib laske. tagastab 0-6 integeri
    pass

def aiLask(): #funktsioon kutsub välja aiLasi funktsiooni kordinaatidega, ootab vastuseks 0-6 integeri

    if hitCoords:
        destroy()
    else:
        seek()
    vastus = aiLasi(kordinaadid)
    
    
    if vastus == 1:             #valmistan destroy funktsiooni ette potentsiaalseks leiuks
        hitCoords.append(kordinaadid)
    elif vastus > 1 and vastus <6:
        laevad.remove(vastus)
        hitCoords.append(kordinaadid)

sink = 0
hitCoords = []

#TEMP
def aiLasi(pask):
    return 1
#TEMP

def leiaNaabrid(coords): #EI OLE VALMIS
    #üleval
    ruum = coords[1]-4 #trust me
    if ruum > 0:
        ruum = 0
    for i in range(1,5 + ruum):
        if playermatrix[coords[1]-i][coords[0]] == 0 and (coords[0],coords[1]-i) not in hitCoords:
            for j in [2,3,4,5]:
                if j in laevad and j >= i+1:
                    outputmatrix[coords[1]-i][coords[0]] += 1
        elif playermatrix[coords[1]-i][coords[0]] != 0:
            break
    #all
    ruum = 9 -coords[1]  # trust me
    if ruum < 0:
        ruum = 0
    for i in range(1, ruum+1):
        if playermatrix[coords[1] + i][coords[0]] == 0 and (coords[0], coords[1] + i) not in hitCoords:
            for j in [2, 3, 4, 5]:
                if j in laevad and j >= i + 1:
                    outputmatrix[coords[1] + i][coords[0]] += 1
        elif playermatrix[coords[1] - i][coords[0]] != 0:
            break
    #vasak
    ruum = coords[0] - 4  # trust me
    if ruum > 0:
        ruum = 0
    for i in range(1, 5 + ruum):
        if playermatrix[coords[1]][coords[0] - i] == 0 and (coords[0]- i, coords[1]) not in hitCoords:
            for j in [2, 3, 4, 5]:
                if j in laevad and j >= i + 1:
                    outputmatrix[coords[1]][coords[0] - i] += 1
        elif playermatrix[coords[1] - i][coords[0]] != 0:
            break
    #parem
    ruum = 9 - coords[0]  # trust me
    if ruum < 0:
        ruum = 0
    for i in range(1, ruum + 1):
        if (coords[0] + i, coords[1]) in hitCoords:
            break
        elif playermatrix[coords[1]][coords[0] + i] == 0 and (coords[0] + i, coords[1]) not in hitCoords:
            for j in [2, 3, 4, 5]:
                if j in laevad and j >= i + 1:
                    outputmatrix[coords[1]][coords[0] + i] += 1
        elif playermatrix[coords[1] - i][coords[0]] != 0:
            break


def destroy(): #laseb põhja juba leitud laevu
    global hitCoords
    for i in hitCoords:
        leiaNaabrid(i)

def seek(): #otsib laevu tõenäosuse põhjal
    resetOutput()
    global playermatrix
    global outputmatrix

    findHoles(playermatrix)
    playermatrix = playermatrix.T
    outputmatrix = outputmatrix.T
    findHoles(playermatrix) 
    playermatrix = playermatrix.T
    outputmatrix = outputmatrix.T

    return (int(str(outputmatrix.argmax())[1]), int(str(outputmatrix.argmax())[0]))



def findHoles(matrix): #leiab tõenäosuse arvutamiseks laualt tühjad kohad, kutsub välja fillrow funktsiooni
    for reacounter in range(10):
        rida=matrix[reacounter]
        tyhi = (rida[0]==0)
        if tyhi:
            tyhjaalgus=0
        for i in range(1,11):
            if tyhi:
                if rida[i]!=0:
                    if (i-tyhjaalgus >= 2):
                        fillrow(reacounter,tyhjaalgus,i)
                    tyhi=False
            else: #pole tyhi
                if rida[i]==0:
                    tyhjaalgus=i
                    tyhi=True

def fillrow(rida, start, end): #täidab leitud tühjad kohad tõenäosustabelist väärtustega outputmatrixisse
    pikkus = end - start
    for i in range(pikkus):
        lisa = 0
        for l in [2,3,4,5]:
            if l in laevad and l<=pikkus:
                lisa += probtable[pikkus-2][l-2][i]
        outputmatrix[rida][start+i] += lisa 

def testseek():
    global playermatrix
    global outputmatrix

    findHoles(playermatrix)
    playermatrix = playermatrix.T
    outputmatrix = outputmatrix.T
    findHoles(playermatrix) 
    playermatrix = playermatrix.T
    outputmatrix = outputmatrix.T
    print("----------------board---------------")
    for i in playermatrix:
        for j in i:
            print("{:<4}".format(j),end = "")
        print("\n")
    print("----------------prob----------------")
    for i in outputmatrix:
        for j in i:
            print("{:<4}".format(j), end="")
        print("\n")
    print(f"suurim tõenäosus on ruudul {int(str(outputmatrix.argmax())[1])+1}:{int(str(outputmatrix.argmax())[0])+1}")
#testseek()

def testHunt():
    global hitCoords
    hitCoords.append((3,3))
    #hitCoords.append((4,5))
    destroy()

    print("----------------board---------------")
    for i in playermatrix:
        for j in i:
            print("{:<4}".format(j),end = "")
        print("\n")
    print("----------------prob----------------")
    for i in outputmatrix:
        for j in i:
            print("{:<4}".format(j), end="")
        print("\n")
    print(f"suurim tõenäosus on ruudul {int(str(outputmatrix.argmax())[1])+1}:{int(str(outputmatrix.argmax())[0])+1}")
testHunt()

from probabilityTable import  probtable
from random import randint
import random
import numpy as np

laevad = [5,4,3,3,2]

<<<<<<< HEAD
playermatrix = np.array([[0,0,0,0,0,0,0,0,0,0,2], #matrix kus hoitakse infot käikude kohta. need kahed on stopperid. ära puutu
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,1,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,1,0,0,2],
=======
testmatrix = np.array([[0,0,0,0,1,0,0,0,0,0,2],
>>>>>>> cd03f9168a76a772c757e9c32de62d0c1ef46d63
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,1,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,1,0,0,0,0,0,0,2],
                       [0,0,0,0,0,1,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [0,0,0,0,0,0,1,0,0,0,2],
                       [0,0,0,0,0,0,0,0,0,0,2],
                       [2,2,2,2,2,2,2,2,2,2,2]])

matrix = np.array([[0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [0,0,0,0,0,0,0,0,0,0,2],
                   [2,2,2,2,2,2,2,2,2,2,2]])

<<<<<<< HEAD
def resetOutput(): #taastab tõenäosustabeli algse seisu
    global outputmatrix
    outputmatrix = np.array([[0,0,0,0,0,0,0,0,0,0],
=======
outputmatrix = np.array([[0,0,0,0,0,0,0,0,0,0],
>>>>>>> cd03f9168a76a772c757e9c32de62d0c1ef46d63
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0,0]])

<<<<<<< HEAD
def playerLasi(): #kontrollib AI laevade seisu ja updateib laske. tagastab 0-6 integeri
    pass

def aiLask(): #funktsioon kutsub välja aiLasi funktsiooni kordinaatidega, ootab vastuseks 0-6 integeri

    if hitCoords:
        destroy()
    else:
        seek()
    vastus = aiLasi(kordinaadid)
=======

##### Place Ships ---------------------------------------------------------------

def randomCords(): # Valib suvaka koha laual, kus ei ole juba laeva
    x = ""
    y = ""
>>>>>>> cd03f9168a76a772c757e9c32de62d0c1ef46d63
    
    while x == "" and y == "":
        temp_x = randint(0,(len(matrix)-1))
        temp_y = randint(0,(len(matrix)-1))
        if matrix[temp_x][temp_y] == 0:
            x = temp_x
            y = temp_y
    
<<<<<<< HEAD
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
=======
    return x, y

def eiOleLaevaKõrval(x, y): # Kas antud cordi 1 block raadiuses on teine laev?
    if matrix[y][x] != 1 and matrix[y-1][x+1] != 1 and matrix[y][x+1] != 1 and matrix[y+1][x+1] != 1 and matrix[y-1][x] != 1 and matrix[y+1][x] != 1 and matrix[y-1][x-1] != 1 and matrix[y][x-1] != 1 and matrix[y+1][x-1] != 1:
        return True         # Ei ole laeva
    return False            # On laev
>>>>>>> cd03f9168a76a772c757e9c32de62d0c1ef46d63

def updateLaevadeSõnastik(laev, cords):  # Vajalik, sest on 2 suurus 3 laeva ja need muidu läheks sama key alla sõnastikus
    if laev in placedLaevad:             # Kui laev, mida paigutati juba key (juhtub ainult kolmega)
        laev=3.1                         # Siis anna keyks
        placedLaevad[laev] = cords       # Ja lisa sõnastikku
    else:
        placedLaevad[laev] = cords       # Muidu pane keyks laeva suurus ja lisa sõnastikku

def placeLaev():            # Proovib paigutada laeva
    global laevad
    global placedLaevad

    placed = False
    x, y = randomCords()
    laev = laevad[randint(0, len(laevad)) - 1]                      # Võtab suvaka numbri laevade listi pikkusest, teeb sellest indexi ja valib selle indexiga listist laeva
    
    if laev in laevad and matrix[y][x] != 1:                        # Kui valitud laev ja kordinaanid ppole juba kasutuses
        teljed = {}
        if x+laev-1 < 10 and x-laev+1 >= 0:                         # Kas x teljel on selle laeva jaoks ruumi
            teljed["0"] = True
        if y+laev-1 < 10 and y-laev+1 >= 0:                         # Kas y teljel on selle laeva jaoks ruumi?
            teljed["1"] = True

        if teljed:                                                  # Kui leaval on mingil teljel ruumi
            telg = random.choice(list(teljed.keys()))               # Vali suvakas telg sobivatest
            võimalused = []
            if telg == "0":                                         # Kui telg on x
                parem = []
                vasak = []
                for ruut in range(laev):                            # Kontrollib laeva suurusele vastava korra, kas selle ruudu kõrval on teine laev
                    parem.append(eiOleLaevaKõrval(x+(1*ruut), y))   # Kontrollib paremale poole
                    vasak.append(eiOleLaevaKõrval(x-(1*ruut), y))   # Kontrollib vasakule poole

                if all(parem):                                      # Kui kõik ruutudest ja nende raadius tühi
                    võimalused.append('parem')
                if all(vasak):
                    võimalused.append('vasak')
            
            if telg == "1":                                         # Kui telg on y, sama teema
                üles = []
                alla = []
                for ruut in range(laev):
                    üles.append(eiOleLaevaKõrval(x, y-(1*ruut)))
                    alla.append(eiOleLaevaKõrval(x, y+(1*ruut)))

                if all(üles) and all(alla):
                    võimalused.append('üles')
                    võimalused.append('alla')
                elif all(üles):
                    võimalused.append('üles')
                elif all(alla):
                    võimalused.append('alla')
    
            if võimalused:                                          # Kui on mingi suund, kuhu laev saaks minna
                valik = võimalused[randint(0, len(võimalused) - 1)] # Vali nendest suvaline
                placedCords = []
                if valik == "parem":                                # Kui valik paremale poole
                    for i in range(laev):
                        placedCords.append([x+i, y])                # Lisa laeva blockide lisit kordinaat
                        matrix[y][x+i] = 1                          # Ning uuenda tabelit vastavalt
                    
                    updateLaevadeSõnastik(laev, placedCords)                # Lisa laual olevate laevade listi laeva kordid
                    placed = True                                   # Ütle, et mingi laev sai paigutatud
                elif valik == "vasak":
                    for i in range(laev):
                        placedCords.append([x-i, y])
                        matrix[y][x-i] = 1
                    
                    updateLaevadeSõnastik(laev, placedCords)
                    placed = True
                elif valik == "üles":
                    for i in range(laev):
                        placedCords.append([x, y-i])
                        matrix[y-i][x] = 1
                    
                    updateLaevadeSõnastik(laev, placedCords)
                    placed = True
                elif valik == "alla":
                    for i in range(laev):
                        placedCords.append([x+1, y+i])
                        matrix[y+i][x] = 1

                    updateLaevadeSõnastik(laev, placedCords)
                    placed = True    

            if placed:
                laevad.remove(laev) # Eemalda olemasolevatest laev paigutatud laevades

def paigutaLaevad():                    # Paigutab AI lauale laevad
    while laevad:                       # Kuniks on kõik laevad paigutatud               
        placeLaev()                     # Proovi paigatada laev

##### AI Playing functions ---------------------------------------------------------------

def seek(testmatrix):
    pass

def findHoles(matrix):
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

def fillrow(rida, start, end):
    pikkus = end - start
    for i in range(pikkus):
        lisa = 0
        for l in [2,3,4,5]:
            if l in laevad and l<=pikkus:
                #print(f"Küsin elementi {pikkus-2}, {l-2}, {i}")
                lisa += probtable[pikkus-2][l-2][i]
        outputmatrix[rida][start+i] += lisa


##### Handle opponents shot ---------------------------------------------------------------

def playerLasi(x, y):
    cords = [x, y]                          # Lasu kordinaanid listina, nagu on ka sõnastiksu
    for i in placedLaevad.keys():           # Iterate läbi iga meie laual oleva laeva
        if i == 3.1:                         # Suurus 3 kahte paati eristatud nii, et üks neist on 3.1
            laevaSuurus = 3                 # Laevasuurus siiski 3, isegi, kui tähistatud 3.1
        else:
            laevaSuurus = i                 # Teisi laeva suurusi 1, seega saame otsu suuruse võtta keyst
        
        if cords in placedLaevad[i]:        # Kui lasu kordinaat on sama mingi meie paadiosaga
            oldMap = placedLaevad[i]        # Vanad selle laeva allesolevate tükkkide cordid
            oldMap.pop(oldMap.index(cords)) # Võta olemasolevate tükkide cordidest ära pihta saanu
            placedLaevad[i] = oldMap        # Uuenda sõnastikus paati, nüüd ilma pihta saanud tüki
            
            if not oldMap:                  # Kui paadil on kõik cordid ära võetud, aga põhjas
                placedLaevad.pop(i, None)   # Võta ära vastav key laevade sõnastukust
                if not placedLaevad:        # Kui sõnastikus pole keysid (laevu)
                    return 6                # Ütle, et kaotasime
                else:                       # Kui sõnastikus on veel keysid (laevu)
                    return laevaSuurus      # Ütle põhja lastud laeva suurus
            else:                           # Kui laeval on veel mingi tükk alles
                return 1                    # Ütle, et saadi pihta
    return 0                                # Kui kuskile pihta ei saadud, vasta vastavalt

##### Main loop ---------------------------------------------------------------

<<<<<<< HEAD
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
=======
def main():
   global testmatrix
   global outputmatrix

   findHoles(testmatrix)
   testmatrix = testmatrix.T
   outputmatrix = outputmatrix.T
   findHoles(testmatrix) 
   testmatrix = testmatrix.T
   outputmatrix = outputmatrix.T
   print("----------------board---------------")
   for i in testmatrix:
       for j in i:
           print("{:<4}".format(j),end = "")
       print("\n")
   print("----------------prob----------------")
   for i in outputmatrix:
       for j in i:
           print("{:<4}".format(j), end="")
       print("\n")
   print(f"suurim tõenäosus on ruudul {int(str(outputmatrix.argmax())[1])+1}:{int(str(outputmatrix.argmax())[0])+1}")

   print(randomPlacement(laevad, outputmatrix))
main()
>>>>>>> cd03f9168a76a772c757e9c32de62d0c1ef46d63

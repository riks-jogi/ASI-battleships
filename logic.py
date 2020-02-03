from probabilityTable import  probtable
import numpy as np

laevad = [5,4,3,3,2]

testmatrix = np.array([[0,0,0,0,1,0,0,0,0,0,2],
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

def seek(testmatrix):
    pass

def probability(matrix):
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

def main():
    global testmatrix
    global outputmatrix

    probability(testmatrix)
    testmatrix = testmatrix.T
    outputmatrix = outputmatrix.T
    probability(testmatrix) 
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
main()

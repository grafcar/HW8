
rows, cols = (5, 8)
parsingTable = [["none" for i in range(cols)] for j in range(rows)]

parsingTable[0][0] = "TQ"
parsingTable[0][5] = "TQ"
parsingTable[1][1] = "+TQ"
parsingTable[1][2] = "-TQ"
parsingTable[1][6] = "Lambda"
parsingTable[1][7] = "Lambda"
parsingTable[2][0] = "FR"
parsingTable[2][5] = "FR"
parsingTable[3][1] = "Lambda"
parsingTable[3][2] = "Lambda"
parsingTable[3][3] = "*FR"
parsingTable[3][4] = "/FR"
parsingTable[3][6] = "Lambda"
parsingTable[3][7] = "Lambda"
parsingTable[4][0]= "i"
parsingTable[4][5] = "(E)"

stack = []
input = "i(i+i)$"

columns =["i","+","-","*","/","(",")","$"]

rows = ["E","Q","T","R","F"]

def read (str):
    str = str[1:]
    return str

stack.append("$")
stack.append("E")
varPop = stack.pop()

while(len(input) > 0):
    
    while(input[:1] != varPop):
        temp = parsingTable[rows.index(varPop)][columns.index(input[:1])]
        if(temp == "Lambda"):
            break
        if(temp == "none"):
            break
        if(temp == "$"):
            print("WORD ACCEPTED")
            break
        else:
            while(len(temp) > 0):
                stack.append(temp[len(temp)-1])
                temp = temp[:len(temp)-1]
        varPop = stack.pop()
    varPop = stack.pop()
    if(varPop== "$"):
        print ("Word Accepted")
        break
    if(varPop == input[:1]):
        varPop = stack.pop()
        input = read(input)
    if(temp != "Lambda"):
        input = read(input)
    if(temp == "none"):
        print ("Word not accepted")
        break
    
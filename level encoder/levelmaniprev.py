

class Item:
    properties = []

    def __init__(self, proplist):
        self.properties = proplist
    
    def printprops(self):
        print(self.properties)

class Connection:
    properties = []

    def __init__(self, proplist):
        self.properties = proplist
    
    def printprops(self):
        print(self.properties)

class Voxel:
    def __init__(self, solid, portal0, portal1, portal2):
        self.solid = solid
        self.portal0 = portal0
        self.portal1 = portal1
        self.portal2 = portal2
    
    def setSolid(self, solid):
        self.solid = solid
    
    def setPortal0(self, portal0):
        self.portal0 = portal0

    def setPortal1(self, portal1):
        self.portal1 = portal1

    def setPortal2(self, portal2):
        self.portal2 = portal2
    
    



level = open("1602637452.p2c", 'r+b')

itemList = []
connectionList = []

itemPropList = []
prop = ""
value = ""
propTupple = []

#iterating over all the lines
for line in level:
    #clearing property and value strings at the start of each line
    prop = ""
    value = ""

    #check if the string contains "Item" and not "Items"
    if((str(line).find("Item") != -1) and (str(line).find("Items") == -1)):
        
        itemPropList = []
        for line in level:
            tempLine = line
            prop = ""
            value = ""
            propTupple = []
            i = 0
            #if line contains "{" do nothing
            if(str(tempLine).find("{")!= -1):
                print("do nothing")
            elif(str(tempLine).find("}")!= -1):
                if(len(itemPropList) > 0):
                    newItem = Item(itemPropList)
                    itemList.append(newItem)
                    itemPropList = []
                    break
            else:

                #skipping the 3 tabs and the inverted comma
                letter = tempLine[4:5]
                i = 4
                #recording the string uptill the next inverted comma
                while(letter != b'"'):
                    prop = "".join([prop, letter.decode("utf-8")])
                    i = i + 1
                    letter = tempLine[i:i+1]
                
                #skipping the 2 tabs uptill the next inverted comma
                i = i + 4
                letter = tempLine[i:i+1]

                #recording the string uptill the next inverted comma
                while(letter != b'"'):
                    
                    value = "".join([value, letter.decode("utf-8")])
                    i = i+1
                    letter = tempLine[i:i+1]
                
                

                
                #print(prop)
                #print(value)
                propTupple.append(prop)
                propTupple.append(value)
        
        #adding property to the current list
                itemPropList.append(propTupple)
                

        #restting the property tupple

    if((str(line).find("Connection") != -1) and (str(line).find("Connections") == -1)):
        
        connectionPropList = []
        for line in level:
            tempLine = line
            prop = ""
            value = ""
            propTupple = []
            i = 0
            #if line contains "{" do nothing
            if(str(tempLine).find("{")!= -1):
                print("do nothing")
            elif(str(tempLine).find("}")!= -1):
                if(len(connectionPropList) > 0):
                    newConnection = Connection(connectionPropList)
                    connectionList.append(newConnection)
                    connectionPropList = []
                    break
            else:

                #skipping the 3 tabs and the inverted comma
                letter = tempLine[4:5]
                i = 4
                #recording the string uptill the next inverted comma
                while(letter != b'"'):
                    prop = "".join([prop, letter.decode("utf-8")])
                    i = i + 1
                    letter = tempLine[i:i+1]
                
                #skipping the 2 tabs uptill the next inverted comma
                i = i + 4
                letter = tempLine[i:i+1]

                #recording the string uptill the next inverted comma
                while(letter != b'"'):
                    
                    value = "".join([value, letter.decode("utf-8")])
                    i = i+1
                    letter = tempLine[i:i+1]
                
                

                
                #print(prop)
                #print(value)
                propTupple.append(prop)
                propTupple.append(value)
        
        #adding property to the current list
                connectionPropList.append(propTupple)

print(len(itemList))
print(len(connectionList))
itemList[2].printprops()
level.close()

level = open("1602637452.p2c", 'r+b')
x = 0
y = 0
z = 0

for line in level:
    if(str(line).find("ChamberSize") != -1):
        tempLine = line
        letter = tempLine[17:18]
        i = 17
        while(letter != b" "):
            x = x*10 + int(letter.decode("utf-8"))
            i = i + 1
            letter = tempLine[i:i+1]
        i = i + 1
        letter = tempLine[i:i+1]
        while(letter != b" "):
            y = y*10 + int(letter.decode("utf-8"))
            i = i + 1
            letter = tempLine[i:i+1]
        i = i + 1
        letter = tempLine[i:i+1]
        while(letter != b'"'):
            z = z*10 + int(letter.decode("utf-8"))
            i = i + 1
            letter = tempLine[i:i+1]
        break

print(x)
print(y)
print(z)
X = []
Y = []
Z = []
for line in level:
    
    if((str(line).find("Solid") != -1)):
        for line in level:
            tempLine = line
            #print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    print(letter)
                    X.append(Voxel(int(letter.decode("utf-8")),1,1,1))
                    i = i + 1
                    letter = tempLine[i:i+1]
                #print("Length of X" + str(len(X)))
                Y.append(X)
                X = []
            elif(str(tempLine).find("}") != -1):
                #print("Length of Y" + str(len(Y)))
                Z.append(Y)
                Y = []
            elif(str(tempLine).find("Portal0") != -1):
                #print(len(Z))
                break
        
        xIter = 0
        yIter = 0
        zIter = 0

        for line in level:
            tempLine = line
            print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    print(letter)
                    Z[zIter][yIter][xIter].setPortal0(int(letter.decode("utf-8")))
                    xIter = xIter + 1
                    i = i + 1
                    letter = tempLine[i:i+1]
                #print("Length of X" + str(len(X)))
                yIter = yIter + 1
                xIter = 0
            elif(str(tempLine).find("}") != -1):
                #print("Length of Y" + str(len(Y)))
                zIter = zIter + 1
                yIter = 0
            elif(str(tempLine).find("Portal1") != -1):
                #print(len(Z))
                break
        
        xIter = 0
        yIter = 0
        zIter = 0

        for line in level:
            tempLine = line
            print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    print(letter)
                    Z[zIter][yIter][xIter].setPortal1(int(letter.decode("utf-8")))
                    xIter = xIter + 1
                    i = i + 1
                    letter = tempLine[i:i+1]
                #print("Length of X" + str(len(X)))
                yIter = yIter + 1
                xIter = 0
            elif(str(tempLine).find("}") != -1):
                #print("Length of Y" + str(len(Y)))
                zIter = zIter + 1
                yIter = 0
            elif(str(tempLine).find("Portal2") != -1):
                #print(len(Z))
                break

        xIter = 0
        yIter = 0
        zIter = 0

        for line in level:
            tempLine = line
            print(tempLine)
            if(str(tempLine).find("f") != -1):
                i = 12
                #print(i)
                letter = tempLine[i:i+1]
                while(letter != b'"'):
                    print(letter)
                    Z[zIter][yIter][xIter].setPortal2(int(letter.decode("utf-8")))
                    xIter = xIter + 1
                    i = i + 1
                    letter = tempLine[i:i+1]
                #print("Length of X" + str(len(X)))
                yIter = yIter + 1
                xIter = 0
            elif(str(tempLine).find("}") != -1):
                #print("Length of Y" + str(len(Y)))
                zIter = zIter + 1
                yIter = 0
            elif(str(tempLine).find("Items") != -1):
                #print(len(Z))
                break

            



                



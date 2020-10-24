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



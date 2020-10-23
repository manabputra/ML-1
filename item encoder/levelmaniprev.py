class Item:
    properties = []

    def __init__(self, proplist):
        self.properties = proplist
    
    def printprops(self):
        print(self.properties)



level = open("1602637452.p2c", 'r+b')

itemlist = []

Itemproplist = []
prop = ""
value = ""
proptupple = []

#iterating over all the lines
for line in level:
    #clearing property and value strings at the start of each line
    prop = ""
    value = ""

    #check if the string contains "Item" and not "Items"
    if((str(line).find("Item") != -1) and (str(line).find("Items") == -1)):
        
        Itemproplist = []
        for line in level:
            templine = line
            prop = ""
            value = ""
            proptupple = []
            i = 0
            #if line contains "{" do nothing
            if(str(templine).find("{")!= -1):
                print("do nothing")
            elif(str(templine).find("}")!= -1):
                if(len(Itemproplist) > 0):
                    newitem = Item(Itemproplist)
                    itemlist.append(newitem)
                    Itemproplist = []
                    break
            else:

                #skipping the 3 tabs and the inverted comma
                letter = templine[4:5]
                i = 4
                #recording the string uptill the next inverted comma
                while(letter != b'"'):
                    prop = "".join([prop, letter.decode("utf-8")])
                    i = i + 1
                    letter = templine[i:i+1]
                
                #skipping the 2 tabs uptill the next inverted comma
                i = i + 4
                letter = templine[i:i+1]

                #recording the string uptill the next inverted comma
                while(letter != b'"'):
                    
                    value = "".join([value, letter.decode("utf-8")])
                    i = i+1
                    letter = templine[i:i+1]
                
                

                
                #print(prop)
                #print(value)
                proptupple.append(prop)
                proptupple.append(value)
        
        #adding property to the current list
                Itemproplist.append(proptupple)
                

        #restting the property tupple


print(len(itemlist))
itemlist[2].printprops()
level.close()



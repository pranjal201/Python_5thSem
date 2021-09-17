list = ["rohan", "amy", "sapna", "muhammad","aakash", "raunak", "chinmoy"]
print(sorted(list, key =len))

# the above code sorts the list on the basis of the len

def Sorter(listly):
    lenlist=[]
    #This will make a list of lenghts
    for x in listly:
        lenlist.append(len(x))

    for i in range(0, len(listly)):
        for j in range(i, len(listly)):

            if(lenlist[i] == lenlist[j]):
                pass
            elif(lenlist[i] > lenlist[j]):
                temp = listly[j]
                listly[j] = listly[i]
                listly[i] = temp
                temp = lenlist[j]
                lenlist[j] = lenlist[i]
                lenlist[i] = temp
            elif(lenlist[i] < lenlist[j]):
                pass

    return listly
print(Sorter(list))

'''
Input : [10, 20, 30, 40, 50, 40, 40, 60, 70] range: 40-80

Output : 6



Input : [10, 20, 30, 40, 50, 40, 40, 60, 70] range: 10-40

Output : 4 ]]
''' 

def find_range(list,r1,r2):
    count = 0
    for i in list:
        if((i <=r2) and (i>=r1)):
            count += 1

    return count

lists = [10, 20, 30, 40, 50, 40, 40, 60, 70]
print(find_range(lists,40,80))

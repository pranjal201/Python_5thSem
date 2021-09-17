''' This problem is to convert list of tuples to Dictionary'''

''' input = [("akash", 10), ("gaurav", 12), ("anand", 14),("suraj", 20), ("akhil", 25), ("ashish", 30)]
     Output : {'akash': [10], 'gaurav': [12], 'anand': [14],'ashish': [30], 'akhil': [25], 'suraj': [20]}'''


List = [("akash", 10), ("gaurav", 12), ("anand", 14),("suraj", 20), ("akhil", 25), ("ashish", 30)]
Dict = dict()
for i in List:
    Dict[i[0]] = i[1]
print(Dict)

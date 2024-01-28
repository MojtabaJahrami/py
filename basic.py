#دیکشنری (dict)
myDict = {
    'name': 'hamid',
    'family': 'hamidi',
    'score': 20,
    'passed': True,
}
# Dictionary features: ordered, changeable, 
myDict = {
    'name': 'hamid',
    'family': 'hamidi',
    'score': 20,
    'passed': True,
}
# print(myDict)
# myDict['name'] = 'reza'
# print(myDict)
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())
# myDict['age'] = 20
# myDict.pop('score')
# myDict.popitem()
# del myDict
# myDict.clear()
newdict = myDict.copy()
print(newdict)












#لیست (list
myList1 = ['ali', 'mohammad', 'reza', 'mahmood', 'reza']

# List features: Duplicateable, changeable
myList1 = ['ali', 'mohammad', 'reza', 'mahmood', 'reza']
myList2 = [400, 500, 3, 6800, 25]
myList3 = [True, False, False, True]
myList4 = ['ali', 4500, True]

print(myList1)
# print(myList1[2:])
# myList1[1] = 'hamid'
# myList1[1:2] = ['hamid', 'majid']
# myList1.insert(2, 'majid')
# myList1.append('majid')
# myList1.extend(myList4)
# newlist = myList1 + myList2
# myList1 = myList1 + myList2
# myList1 += myList2
# myList1.remove('reza')
# myList1.remove('reza')
# myList1.pop(4)
# myList1.pop()
# del myList1[3]
# del myList1
# myList1.clear()
# myList1.sort(reverse= True)
# myList2.sort()
# newlist = myList1.copy()
print(newlist)










#مجموعه (set)
mySet = {'ali', 'ahmad', 'hamid', 'reza', 'hamid'}

# Set features: not ordered, not changeable, not duplicateable
mySet = {'ali', 'ahmad', 'hamid', 'reza', 'hamid'}
mySet1 = {'mahmood', 'morteza', 'reza'}
# print(mySet[1])
# mySet.add('majid')
# mySet.update(mySet1)
# mySet.remove('ali')
# mySet.pop()
mySet.clear()
print(mySet)







#تاپل (tuple)
myTuple1 = ('ali', 'hassan', 'hossein', 'mahmood', 'majid', 'ali')



# Tuple features: duplicateable, ordered, unchangeable
myTuple1 = ('ali', 'hassan', 'hossein', 'mahmood', 'majid', 'ali')
myTuple2 = ('ali', 20, True)
# myTuple2 = ('ali',)
print(myTuple1)
# print(type(myTuple1))
# print(len(myTuple1))
# print(myTuple1[-1])

myList = list(myTuple1)
myList[2] = 'majid'
myTuple1 = tuple(myList)
# myTuple1[2] = 'majid'

myTuple = myTuple1 + myTuple2
print(myTuple)





#حلقه for
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("Number ", i);

#if
a = 33
b = 200
if b > a:
  print("b is greater than a")



def lstadd(b , k):
    #lstadd will append any inputs given in k to the list lst
    y = [k]
    a = [b]
    lst1 = [a + y]
    return lst1
z = [input("please enter your list with the items separated by commas")]
x = [input("Please enter your second list with the items separated by commas")]
output = list(map(lstadd, z,x))
print(output)

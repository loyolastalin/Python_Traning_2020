# alpha to integer testing the code 
x = '92666'
b = 0
for item in x:
    b = (b *10) + (ord(item)- ord('0'))
   
print(b)
print(type(b))
import re
##g = input("Enter your real path of the file : ")
##File write
fw = open(r'input.txt','w+')
fw.writelines('Write new line 1\n')
fw.close()
## File Read
f = open('input.txt', 'r')

content = f.readlines()
print(content)

f.close







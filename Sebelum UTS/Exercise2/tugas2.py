firstnum = open('num1.txt').read()
secnum = open('num2.txt').read()

print((lambda x,y: int(x)+int(y))(firstnum,secnum))

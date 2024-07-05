from random import randint
a= randint (0,1000)
y= int(input("adivinha"))
while a!=y:
    if a<y:
        print ("o número é menor")
        y= int(input('advinha')) 
    elif a>y:
        print ('o número é maior')
        y= int(input('advinha')) 
if a==y:
    print("acertaste")


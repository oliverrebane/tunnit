#oliver rebane
#it20

#ylesanne 01
number1 = int(input("Sisesta esimene number: "))
number2 = int(input("Sisesta teine number: "))
vastus = number1+number2
print(f"{number1} ja {number2} summa on {vastus}")

#ylesanne 05
#not very sure on how to do this

print("\n")
#ylesanne 08
string = input("Sisesta lause: ")
words = string.split()
words = list(reversed(words))
print(" ".join(words))

#ylesanne 09
for i in range(1,67):
    print(i,end="")

print("\n")
#ylesanne 12
for i in range(1,6):
    if i%2==0:
        print("",end="")
    else:
        print("*"*i)
for i in range(1,6):
    if i==3:
        print("*"*i)
for i in range(1,6):
    if i==1:
        print("*"*i)
print(" ")

for i in range(0,6):
    a = 5-i
    print("*"*a)

for i in range(0,6):
    print("*"*i)
    
print("")

for i in range(0,6):
    b=5-i
    if i<4:
        print("*"*b)
    else:
        print("*"*b,end="")
for i in range(0,6):
    print("*"*i)
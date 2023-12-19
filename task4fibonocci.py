########## WAP to print the fibonacci series upto fixed term user want ##########

term=int(input("enter the no of terms u want: "))
a=0
b=1
print(a)
print(b)
while(term>2):
    c=a+b
    print(c)
    a=b
    b=c
    term=term-1
print("is required series")

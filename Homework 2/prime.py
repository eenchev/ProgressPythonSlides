var=int(input())
a=2
toggle=0
while(a<var):
    if(var%a==0):
        toggle=1
    a=a+1
if(toggle==0):
    print("Your number is Prime")
else:
    print("Your number is not Prime")
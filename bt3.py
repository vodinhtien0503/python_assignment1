n=int(input("input:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+1
if(sum==n):
    print("The number is a Perfect number")
else:
    print("The numbet is not a Perfect number")

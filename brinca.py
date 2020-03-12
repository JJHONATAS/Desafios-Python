x=input().split()
a=int(x[0])
b=int(x[1])
c=int(x[2])

maiorAB = (a+b+abs(a-b))/2           #calcula maior ab
maiorAC=(a+c+abs(a-c))/2           #calcula maior ac
maiorBC=(b+c+abs(b-c))/2           #calcula maior bc
if maiorAB > maiorAC:
    print(max(maiorAB,' eh o maior'))
elif maiorBC > maiorAC or maiorAB:
    print(max(maiorBC,' eh o maior'))
else:
    print(max(maiorAC,' eh o maior'))
#/usr/bin/python3
num=int(input("enter your rows:"))
for i in range(1,num+1):
	for j in range(1,num-i+1):
		print(end="")
	for j in range(i,0,-1):
		print(j)
	for j in range(2,i+1):
		print(j)
	print()

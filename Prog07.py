print("Input 10 numbers")
evennumber=0
for i in range(1,11):
	number=float(input())
	if number%2==0:
		evennumber=evennumber+1
print(evennumber)
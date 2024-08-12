def add(num1,num2):
	return num1+num2

def subtract(num1,num2):
	return num1-num2

def multiply(num1,num2):
	return num1*num2

def divide(num1,num2):
	return num1/num2

print("Please select an opertion")
print("1.Add")
print("2.Subtract")
print("3.MUltiply")
print("4.Divide")
print("5.Exit")

while True:
	choice=input("Enter your choice(1/2/3/4/5):")
	
	if choice=='5':
		print("Good Bye!")
		break
	if choice in ('1','2','3','4'):
		num1=float(input("Enter the first number: "))
		num2=float(input("Enter the second number: "))

		if choice=='1':
			print(num1,"+",num2,"=",add(num1,num2))
			
		elif choice=='2':
			print(num1,"-",num2,"=",subtract(num1,num2))

		elif choice=='3':
			print(num1,"*",num2,"=",multiply(num1,num2))

		elif choice=='4':
			print(num1,"/",num2,"=",divide(num1,num2))

		else:
			print("Invalid Input")

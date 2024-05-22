n = int(input("Enter the number of rows : "))

def lower_pyramid(n):
    for i in range(1 , n+1):
        print("* " * i)
        
def upper_pyramid(n):
    for i in range(n, 0, -1):
        print(i * "* ")
        
def pyramid(n):
    for i in range(1,n+1):
        print(' '*(n - i)+ "* "*i)
        
print("\nThe Lower Pyramid is : ")        
lower_pyramid(n)
print("\nThe Upper Pyramid is : ")        
upper_pyramid(n)
print("\nThe Pyramid is : ")        
pyramid(n)
while True:
    try:
        a=input("Enter the elements of the set A: ")
        A=set(map(int,a.split(',')))
        break
    except ValueError:
        print('Invalid Input.Enter the numbers separated by commas.')
while True:
    try:
        b=input("Enter the elements of the set B: ")
        B=set(map(int,b.split(',')))
        break
    except ValueError:
        print('Invalid Input.Enter the numbers separated by commas.')
print("The operations on the sets are as follows: \n")
print("The Union of sets A and B is:", A|B,'\n')
print("The Intersection of sets A and B is:", A&B,'\n')
print("The Difference of sets A and B is:", A-B,'\n')
print("The Symmetric-Difference of sets A and B is:", A^B)

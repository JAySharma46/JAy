for i in range(1,3):
    l= list(map(int,input("Enter the numbers you wish to filter positive numbers from: ").split()))
    print("Input:",l)
    positive_numbers=[i for i in l if i>0]
    print("Output:", positive_numbers)


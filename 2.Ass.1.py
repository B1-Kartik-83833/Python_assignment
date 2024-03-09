def factorial():

    for num in range(10):
        fact = 1

        for i in range(1, num +1 ):
            fact *= i
        print(f"the facotial of number {num} is {fact}")





factorial()
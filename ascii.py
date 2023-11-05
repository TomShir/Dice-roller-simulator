import random 
one='0'
two='0\n\t0'
three='0\n\t0\n\t\t0'
four='0\t0\n\n0\t0'
five='0\t0\n    0\n0\t0'
six='0\t0\n0\t0\n0\t0\n0\t0\n0\t0\n0\t0'
while True:
    numerical_values=[num for num in range(1,7,1)]
    random_number=random.choice(numerical_values)
    choice=input('press r to roll dice  or press q to exit:')
    r='r'
    q='q'
    if choice==r:
        if random_number==1:
            print(f'{one}') 
        elif random_number==2:
            print(f'{two}')
        elif random_number==3:
            print(f'{three}')
        elif random_number==4:
            print(f'{four}')
        elif random_number==5:
            print(f'{five}')
        elif random_number==6:
            print(f'{six}') 
    elif choice==q:
        print('Dice roll simulator exitted...')
        break
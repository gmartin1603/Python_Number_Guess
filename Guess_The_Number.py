while True:
    import random
    #generates a random number to be guessed
    answer = random.randint(1,50)
    trace = False
    #allows user to guess until correct
    while trace == False:
        guess = int(input('Make your guess, 1-50 '))
        if guess > answer:
            print(guess, 'is too high')


        elif guess < answer:
            print(guess, 'is too low')


        else:
            trace = True

    print(guess, 'is correct!')
    break
again = input('Hit "Enter" to play again')

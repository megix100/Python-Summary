from random import randint
def guessing(guess,answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')

if __name__=="__main__":
    answer = randint(1, 10)
    while True:
        try:
            guess=int(input('guess a number 1 to 10:  '))
            if guessing(guess,answer)==True: #Or just if guessing(guess,answer)
                break
        except ValueError:
            print('please enter a number')
            continue
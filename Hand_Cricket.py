import random
option1 = ['Batting', 'Bowling']
option2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_toss = input('Enter your choice(from Even or Odd):')
user_number = int(input('Enter a number(from 1 to 10):'))
computer_number = random.choice(option2)
print(f'The computer did a {computer_number}')
sum_toss = user_number + computer_number
rem = sum_toss % 2
if rem == 0:
    toss_result = 'Even'
else:
    toss_result = 'Odd'
print(f'The toss result is {toss_result}')
if toss_result == user_toss:
    print('You won the toss')
    user_choice = input('Choose what to do(from Batting or Bowling):')
    print(f'You chose {user_choice}')
    if user_choice == 'Batting':
        user_score = 0
        i = 0
        while i >= 0:
            user_runs = int(input('Enter a number(from 1 to 10):'))
            computer_bowls = random.choice(option2)
            print(f'The computer bowled a {computer_bowls}')
            if user_runs != computer_bowls:
                user_score = user_runs + user_score
            else:
                print('User is out')
                break
        print(f'User scored {user_score} runs')
        print(f'The target is {user_score + 1}')
        computer_score = 0
        i = 0
        while i >= 0:
            computer_runs = random.choice(option2)
            user_bowls = int(input('Enter a number(from 1 to 10):'))
            print(f'Computer took {computer_runs} runs')
            if user_bowls != computer_runs:
                computer_score = computer_score + computer_runs
                if computer_score >= user_score + 1:
                    print('Computer won')
                    break
                elif computer_score == user_score:
                    print("It's a tie")
                else:
                    pass
            else:
                print('Computer is out')
                print(f'The computer scored {computer_score} runs')
                print(f'User won by {user_score - computer_score + 1} runs')
                break
    else:
        computer_score = 0
        i = 0
        while i >= 0:
            user_bowls = int(input('Enter a number(from 1 to 10):'))
            computer_runs = random.choice(option2)
            print(f'The computer took {computer_runs} runs')
            if user_bowls != computer_runs:
                computer_score = computer_score + computer_runs
            else:
                print('The computer is out')
                break
        print(f'The computer scored {computer_score}')
        print(f'The target is {computer_score + 1}')
        user_score = 0
        i = 0
        while i >= 0:
            user_runs = int(input('Enter a number(from 1 to 10):'))
            computer_bowls = random.choice(option2)
            print(f'Computer bowled a {computer_bowls}')
            if user_runs != computer_bowls:
                user_score = user_score + user_runs
                if user_score >= computer_score + 1:
                    print('User won')
                    break
                elif user_score == computer_score:
                    print("It's a tie")
                else:
                    pass
            else:
                print('User is out')
                print(f'User scored {user_score} runs')
                print(f'Computer won by {computer_score - user_score + 1}')
                break
else:
    print('You lost the toss')
    computer_choice = random.choice(option1)
    print(f'The computer chose {computer_choice}')
    if computer_choice == 'Batting':
        computer_score = 0
        i = 0
        while i >= 0:
            computer_runs = random.choice(option2)
            user_bowls = int(input('Enter a number(from 1 to 10):'))
            print(f'The computer took {computer_runs} runs')
            if user_bowls != computer_runs:
                computer_score = computer_score + computer_runs
            else:
                print('Computer is out')
                break
        print(f'Computer scored {computer_score}')
        print(f'The target is {computer_score + 1}')
        user_score = 0
        i = 0
        while i >= 0:
            user_runs = int(input('Enter a number(from 1 to 10):'))
            computer_bowls = random.choice(option2)
            print(f'Computer bowled a {computer_bowls}')
            if computer_bowls != user_runs:
                user_score = user_score + user_runs
                if user_score >= computer_score + 1:
                    print('User won')
                    break
                elif user_score == computer_score:
                    print("It's a tie")
                else:
                    pass
            else:
                print('User is out')
                print(f'User scored {user_score}')
                print(f'Computer won by {computer_score - user_score + 1}')
                break
    else:
        user_score = 0
        i = 0
        while i >= 0:
            user_runs = int(input('Enter a number(from 1 to 10):'))
            computer_bowls = random.choice(option2)
            if user_runs != computer_bowls:
                user_score = user_score + user_runs
            else:
                print('User is out')
                break
        print(f'User scored {user_score} runs')
        print(f'The target is {user_score + 1}')
        computer_score = 0
        i = 0
        while i >= 0:
            computer_runs = random.choice(option2)
            user_bowls = int(input('Enter a number(from 1 to 10):'))
            print(f'Computer took {computer_runs} runs')
            if user_bowls != computer_runs:
                computer_score = computer_score + computer_runs
                if computer_score >= user_score + 1:
                    print('Computer won')
                    break
                elif computer_score == user_score:
                    print("It's a tie")
                else:
                    pass
            else:
                print('Computer is out')
                print(f'Computer scored {computer_score} runs')
                print(f'User won by {user_score - computer_score + 1}')
                break

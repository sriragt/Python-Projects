def guessing_game(range1 = 1, range2 = 100):
        rangeoffirstguess = 10 ** (len(str(range2 - range1 + 1)) - 2)
        print(f"WELCOME TO GUESS ME!\nI'm thinking of a number between {range1} and {range2}\nIf your guess is not between {range1} and {range2}, I'll say OUT OF BOUNDS\nIf your guess is more than {rangeoffirstguess} away from my number, I'll tell you you're COLD\nIf your guess is within {rangeoffirstguess} of my number, I'll tell you you're WARM\nIf your guess is farther than your most recent guess, I'll say you're getting COLDER\nIf your guess is closer than your most recent guess, I'll say you're getting WARMER\nLET'S PLAY!")
        replay = True
        while replay == True:
                import random
                solution = random.randint(range1, range2)
                guesses = []
                guesses.append(int(input(f'Guess an integer between {range1} and {range2}: ')))
                if guesses[0] >= range1 and guesses[0] <= range2 and guesses[0] != solution:
                        if abs(guesses[0] - solution) < rangeoffirstguess:
                                print('WARM!')
                        else:
                                print('COLD!')
                while guesses[-1] != solution:
                        if guesses[-1] < range1 or guesses[-1] > range2:
                                print('OUT OF BOUNDS')
                        if len(guesses) > 1 and not guesses[-1] < range1 and not guesses[-1] > range2:
                                if abs(guesses[-1] - solution) <= abs(guesses[-2] - solution):
                                        print('WARMER!')
                                else:
                                        print('COLDER!')
                        guesses.append(int(input('Guess another integer: ')))
                else:
                        print(f'You guessed the number correctly! It was {solution}!!\nIt took you only {len(guesses)} tries to guess the correct number.')
                playagain = input('Do you want to play again? (Y)es or (N)o: ').capitalize()
                if playagain == 'Y' or playagain == 'Yes':
                        newrange = input('Do you want to use a new range of numbers to guess? (Y)es or (N)o: ').capitalize()
                        if newrange == 'Y' or newrange == 'Yes':
                                from ast import literal_eval
                                answer = input('Input your new range as a tuple- (range1, range2): ')
                                new_range = literal_eval(answer)
                                range1 = new_range[0]
                                range2 = new_range[1]
                                rangeoffirstguess = 10 ** (len(str(range2 - range1 + 1)) - 2)
                                print(f"\nNow I'm thinking of a number between {range1} and {range2}\nIf your guess is not between {range1} and {range2}, I'll say OUT OF BOUNDS\nIf your guess is more than {rangeoffirstguess} away from my number, I'll tell you you're COLD\nIf your guess is within {rangeoffirstguess} of my number, I'll tell you you're WARM\nIf your guess is farther than your most recent guess, I'll say you're getting COLDER\nIf your guess is closer than your most recent guess, I'll say you're getting WARMER")
                        else:
                                print(f"\nI'm thinking of another number between {range1} and {range2}\nIf your guess is not between {range1} and {range2}, I'll say OUT OF BOUNDS\nIf your guess is more than {rangeoffirstguess} away from my number, I'll tell you you're COLD\nIf your guess is within {rangeoffirstguess} of my number, I'll tell you you're WARM\nIf your guess is farther than your most recent guess, I'll say you're getting COLDER\nIf your guess is closer than your most recent guess, I'll say you're getting WARMER")

                else:
                        print('Thanks for playing!!')
                        replay = False

if __name__ == '__main__':
        guessing_game()
def tictactoe():
    from colorama import init
    init()
    from colorama import Fore
    def gameplay():
        q='onions'
        w='------------------\n'
        x='\n'
        y='     |      |     \n'
        a=b=c=d=e=f=g=h=i='     '
        z='|'
        player='Player 1'
        def square(person, letter, part):
            if person==1:
                if answer2 == f'{part}':
                    if first=='  X  ':
                        if letter == '     ':
                            return 'hi'
                        elif letter=='  X  ':
                            print(f'Sorry {name}, you have already placed a marker on this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
                        elif letter=='  O  ':
                            print(f'Sorry {name}, {name2} has already taken this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
                    else:
                        if letter == '     ':
                            return 'hi'
                        elif letter=='  O  ':
                            print(f'Sorry {name}, you have already placed a marker on this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
                        elif letter=='  X  ':
                            print(f'Sorry {name}, {name2} has already taken this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
            elif person==2:
                if answer2==f'{part}':
                    if second=='  O  ':
                        if letter == '     ':
                            return 'hi'
                        elif letter=='  O  ':
                            print(f'Sorry {name}, you have already placed a marker on this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
                        elif letter=='  X  ':
                            print(f'Sorry {name}, {name2} has already taken this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
                    else:
                        if letter == '     ':
                            return 'hi'
                        elif letter=='  X  ':
                            print(f'Sorry {name}, you have already placed a marker on this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'
                        elif letter=='  O  ':
                            print(f'Sorry {name}, {name2} has already taken this space. Please choose another square.')
                            player='Player 1'
                            q='rotten tomatoes'

        def check():
            if a==b==c!='     ' or d==e==f!='     ' or g==h==i!='     ' or a==d==g!='     ' or b==e==h!='     ' or c==f==i!='     ' or g==e==c!='     ' or a==e==i!='     ':
                return False
            else:
                return True
        choice=start=True
        board=y+g+z+h+' '+z+i+x+y+w+y+d+z+e+' '+z+f+x+y+w+y+a+z+b+' '+z+c+x+y
        print('WELCOME TO TIC-TAC-TOE! In this game of Tic-Tac-Toe, each player takes turns placing their designated marks into the different squares of the board. When its your turn, input the number of the designated square on the Tic-Tac-Toe board to place your marker on that square:\n     |     |     \n  7  |  8  |  9  \n     |     |     \n------------------\n     |     |     \n  4  |  5  |  6  \n     |     |     \n------------------\n     |     |     \n  1  |  2  |  3  \n     |     |     \nIf you want to leave the game at any time, just input "leave" or "exit".')
        n=input('Player 1, what is your name? ')
        name=n.title()
        if name.lower()=='leave' or name.lower()=='exit':
                print('\nThank you for playing Tic-Tac-Toe. You are now exiting the game.')
                return('bye')
        n2=input('Player 2, what is your name? ')
        name2=n2.title()
        if name2.lower()=='leave' or name2.lower()=='exit':
                print('\nThank you for playing Tic-Tac-Toe. You are now exiting the game.')
                return('bye')
        while choice==True:
            answer1=input(f'{name}, do you want to be X or O? ')
            if answer1.lower()=='x':
                first='  X  '
                second='  O  '
                choice=False
            elif answer1.lower()=='o':
                first='  O  '
                second='  X  '
                choice=False
            elif answer1.lower()=='leave' or answer1.lower()=='exit':
                print('\nThank you for playing Tic-Tac-Toe. You are now exiting the game.')
                return('bye')
            else:
                caps=answer1.capitalize()
                print(f'"{answer1}" is not a choice. Please input X or O.')
                choice=True
        while a=='     ' or b=='     ' or c=='     ' or d=='     ' or e=='     ' or f=='     ' or g=='     ' or h=='     ' or i=='     ':
            if check()==True:
                if player=='Player 1':
                    answer2=input(f'{name}, where do you want to place your token? ')
                    if answer2.lower()=='leave' or answer1.lower()=='exit':
                        print('\nThank you for playing Tic-Tac-Toe. You are now exiting the game.')
                        return('bye')
                    elif answer2=='1':
                        square(1, a, 1)
                        if square(1, a, 1)=='hi':
                            a=first
                    elif answer2=='2':
                        square(1, b, 2)
                        if square(1, b, 2)=='hi':
                            b=first
                    elif answer2=='3':
                        square(1, c, 3)
                        if square(1, c, 3)=='hi':
                            c=first
                    elif answer2=='4':
                        square(1, d, 4)
                        if square(1, d, 4)=='hi':
                            d=first
                    elif answer2=='5':
                        square(1, e, 5)
                        if square(1, e, 5)=='hi':
                            e=first
                    elif answer2=='6':
                        square(1, f, 6)
                        if square(1, f, 6)=='hi':
                            f=first
                    elif answer2=='7':
                        square(1, g, 7)
                        if square(1, g, 7)=='hi':
                            g=first
                    elif answer2=='8':
                        square(1, h, 8)
                        if square(1, h, 8)=='hi':
                            h=first
                    elif answer2=='9':
                        square(1, i, 9)
                        if square(1, i, 9)=='hi':
                            i=first
                    else:
                        incorrect=answer2.capitalize()
                        print(f'"{incorrect}" is not a name a of a Tic-Tac-Toe square. Please choose a number from 1 through 9 to place your token.')
                        player='Player 1'
                        q='rotten tomatoes'
                    if q=='onions':
                        player='Player 2'
                    else:
                        q='onions'
                    board=y+g+z+h+' '+z+i+x+y+w+y+d+z+e+' '+z+f+x+y+w+y+a+z+b+' '+z+c+x+y
                    print(board)
                else:
                    answer2=input(f'{name2}, where do you want to place your token? ')
                    if answer2.lower()=='leave' or answer1.lower()=='exit':
                        print('\nThank you for playing Tic-Tac-Toe. You are now exiting the game.')
                        return('bye')
                    elif answer2=='1':
                        square(2, a, 1)
                        if square(1, a, 1)=='hi':
                            a=second
                    elif answer2=='2':
                        square(2, b, 2)
                        if square(2, b, 2)=='hi':
                            b=second
                    elif answer2=='3':
                        square(2, c, 3)
                        if square(2, c, 3)=='hi':
                            c=second
                    elif answer2=='4':
                        square(2, d, 4)
                        if square(2, d, 4)=='hi':
                            d=second
                    elif answer2=='5':
                        square(2, e, 5)
                        if square(2, e, 5)=='hi':
                            e=second
                    elif answer2=='6':
                        square(2, f, 6)
                        if square(2, f, 6)=='hi':
                            f=second
                    elif answer2=='7':
                        square(2, g, 7)
                        if square(2, g, 7)=='hi':
                            g=second
                    elif answer2=='8':
                        square(2, h, 8)
                        if square(2, h, 8)=='hi':
                            h=second
                    elif answer2=='9':
                        square(2, i, 9)
                        if square(2, i, 9)=='hi':
                            i=second
                    else:
                        incorrect=answer2.capitalize()
                        print(f'"{incorrect}" is not a name a of a Tic-Tac-Toe square. Please choose a number from 1 through 9 to place your token.')
                        player='Player 2'
                        q='rotten tomatoes'
                    if q=='onions':
                        player='Player 1'
                    else:
                        q='onions'
                    board=y+g+z+h+' '+z+i+x+y+w+y+d+z+e+' '+z+f+x+y+w+y+a+z+b+' '+z+c+x+y
                    print(board)
            elif check()==False:
                if a==b==c=='  X  ' or d==e==f=='  X  ' or g==h==i=='  X  ' or a==d==g=='  X  ' or b==e==h=='  X  ' or c==f==i=='  X  ' or g==e==c=='  X  ' or a==e==i=='  X  ':
                    if first=='  X  ':
                        print(Fore.RED + f"{name} wins the game!" + Fore.BLUE + f" Nice try, {name2}.")
                    else:
                        print(Fore.RED + f"{name2} wins the game!" + Fore.BLUE + f" Nice try, {name}.")
                    return
                elif a==b==c=='  O  ' or d==e==f=='  O  ' or g==h==i=='  O  ' or a==d==g=='  O  ' or b==e==h=='  O  ' or c==f==i=='  O  ' or g==e==c=='  O  ' or a==e==i=='  O  ':
                    if first=='  O  ':
                        print(Fore.BLUE + f"{name2} wins the game!" + Fore.RED + f" Nice try, {name}.")
                    else:
                        print(Fore.BLUE + f"{name} wins the game!" + Fore.RED + f" Nice try, {name2}.")
                    return
        else:
            print(Fore.YELLOW + "It's a tie!")
            return
    repeat=1
    end=False
    if gameplay()=='bye':
        return
    else:
        while end==False:
            if repeat==1:
                gameplay()
                print(Fore.RESET)
                repeat=2
            elif repeat==2:
                final_answer=input('Do you want to play Tic-Tac-Toe again? (yes or no) ')
                if final_answer.lower()=='yes' or final_answer.lower()=='y':
                    gameplay()
                    repeat=2
                elif final_answer.lower()=='no' or final_answer.lower()=='leave' or final_answer.lower()=='exit' or final_answer.lower()=='n':
                    print('\nThank you for playing Tic-Tac-Toe.\n\n\nYou are now leaving the game.')
                    break
                else:
                    wrong=final_answer.proper()
                    print(f'"{wrong}" is not a choice. Please input either "yes" to restart the game or "no" to leave the game.')
                    repeat=2


tictactoe()
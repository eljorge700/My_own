def check_winner():
    if area[0][0] == ' X ' and area[0][1] == ' X ' and area[0][2] == ' X ':
        return ' X '



def draw_area():
    for i in area:
        print(*i)

area = [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]']]
print("Welcome to tic-tac!")
print("___________________")
draw_area()
for turn in range(1, 10):
    print(f'Turn: {turn}')
    if turn % 2 == 0:
        turn_char = " 0 "
        print('Turn circles')
    else:
        turn_char = " X "
        print('Turn crosses')
    row = int(input('Enter the raw number(1, 2 or 3): ')) - 1
    column = int(input('Enter the column number(1, 2 or 3): ')) - 1
    if area[row][column] == '[ ]':
        area[row][column] = turn_char
    else:
        print('This cell is full. The turn goes to the next one.')
        draw_area()
        continue

    draw_area()

    if check_winner() == ' X ':
        print('Crosses wins!')
        break
    if check_winner() == ' 0 ':
        print('Circles wins!')
        break
    if check_winner() == '[ ]' and turn == 9:
        print('Nobody wins')
        break

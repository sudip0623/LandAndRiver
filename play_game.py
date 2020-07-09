from authenticate_data import authenticateUser


def adjacentValue(matrix, row, col):
    count = 0
    radius = 1
    # horizontal-right
    while col + radius != len(matrix[0]):
        if matrix[row][col + radius] == 1:

            count += 1
            radius += 1
        else:
            break

    radius = 1
    # horizontal -left
    while col - radius != -1:
        if matrix[row][col - radius] == 1:
            count += 1
            radius += 1

        else:
            break

    # vertical-up
    radius = 1
    while row - radius != -1:
        if matrix[row - radius][col] == 1:
            count += 1
            radius += 1
        else:
            break

    # vertical-down
    radius = 1
    while row + radius != len(matrix):
        if matrix[row + radius][col] == 1:
            count += 1
            radius += 1

        else:
            break

    return count


def displayWelcomeNote():
    with open("welcome_note.txt") as file:  # Use file to refer to the file object
        data = file.read()
        print(data)


def createMatrix():
    print('Enter the size of the matrix')

    rows = int(input('Enter the rows in matrix : '))
    cols = int(input('Enter the columns in matrix : '))

    matrix = []

    for row in range(rows):
        a = []
        for col in range(cols):
            print('Enter the either 0 or 1 for [', row, '][', col, '] : ')
            a.append(int(input()))
        matrix.append(a)
    return matrix, rows, cols


def getRiverSize(matrix, rows, cols):
    river_sizes = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                c = adjacentValue(matrix, row, col)
                river_sizes.append(c)
                #print('count for ', str(row), ' ', col, 'is', c)
            else:
                river_sizes.append(0)

    return river_sizes


def askUserForRiverSizes(river_sizes, rows, cols):
    s = 0
    correct = 0
    for row in range(rows):
        for col in range(cols):
            print('Guess the size of the river for ', row, 'and', col)
            size = int(input())

            if size == river_sizes[s]:
                correct += 1

            s += 1
    return correct


def validateUserResponse(userResponse,river_sizes):
    if userResponse == len(river_sizes):
        print('You are the winner')
    elif userResponse / len(river_sizes) * 100 >= 60:
        print('you got second positio')
    else:
        print('Invest more money on Almonds, then come back')

    res = input('Do you want to play again ? (Yes/No) : ')

    if res == 'Yes' or res == 'y' or res == 'Y':
        return True
    else:
        return False



def main():
    if authenticateUser():

        displayWelcomeNote()



        choice = input('Do you want to get in? (Yes/No) : ')

        if choice == 'Yes' or choice == 'y' or choice == 'Y':
            with open("game_instruction.txt") as file:  # Use file to refer to the file object
                print(file.read())

            while True:
                try:
                    response = input('Enter P to continue : ')

                    if response == 'P':
                        break
                    else:
                        raise Exception('You Entered the wrong choice, Enter P to play')
                except Exception as e:
                    print(e)

            carryOn =True

            while carryOn:
                matrix, rows, cols = createMatrix()

                river_sizes = getRiverSize(matrix, rows, cols)

                #print(matrix)

                userResponse = askUserForRiverSizes(river_sizes, rows, cols)

                carryOn = validateUserResponse(userResponse, river_sizes)


main()

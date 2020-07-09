from read_csv import readcsv

def authenticateUser():
    attempt=1

    while attempt<=3:
        name = input('Enter name : ')
        email = input('Enter email : ')
        attempt+=1

        csv_data = readcsv()

        if any(name in sublist for sublist in csv_data) and any(email in sublist for sublist in csv_data):
            print('present')
            return True
            break
        else:

            continue

    if attempt == 4:
        print('No chance')
        return False





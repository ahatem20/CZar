from maskpass import askpass


def readChoice(question):
    choice = ''
    while True:
        choice = input(
            question + ' yes[y]/No[n]:'
        )
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            break
        else:
            continue
    return choice.lower()


def readPassId():
    passId = ''
    while len(passId) == 0:
        passId = input(
            'Enter your password ID [example: facebook account]: '
        )
    return passId


def readUserName(passId):
    usrName = ''
    while len(usrName) == 0:
        usrName = input(
            'Enter your {}\'s User Name: '.format(
                str(passId)
            )
        )
    return usrName


def readPassword(passId):
    password = ''
    while len(password) == 0:
        password = askpass(
            prompt='Enter your {}\'sPassword: '.format(
                str(passId)
            ),
            mask=''
        )
    return password

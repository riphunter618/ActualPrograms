import random


class CustomError(Exception):
    pass


def play():
    x = ['r', 'p', 's']
    x1 = [['r', 's'], ['s', 'p'], ['p', 'r']]
    x2 = []
    point = 0
    comp_point = 0
    while True:
        a = input('Enter choice')
        b = random.choice(x)
        if a in x:
            if a == b:
                print('Tie')
            else:
                for i in range(0, len(x1)):
                    if a in x1[i]:
                        x2 += [x1[i]]

                for i1 in x2:
                    if a in i1:
                        if b in i1:
                            if i1.index(a) == 0:
                                point += 1
                                print('win')
                                print('your oppenent picked', b)
                                print('your points are', point)
                                x1.clear()
                            if i1.index(a) != 0:
                                comp_point += 1
                                print('lose')
                                print('your opponents picked', b)
                                print('your opponent\'s points are', comp_point)
                                x1.clear()
        else:
            raise CustomError('Can\'t help if ur stupid')
        if point == 3:
            print('you won')
            break
        elif comp_point == 3:
            print('you lost')
            break


if __name__ == '__main__':
    play()

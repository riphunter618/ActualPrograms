HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

x = 'treat'
x = list(x)
occur = []
index_pos = 0
blanks = '_' * len(x)
blanks = list(blanks)
turns = 7
while turns > 0:
    guess = input('enter guess')
    if x.count(guess) > 1:
        for i in range(0, len(x)):
            o = x.index(guess, index_pos)
            occur.append(o)
            index_pos += 1
        occur = set(occur)
        occur = list(occur)
        for i in occur:
            blanks[i] = guess
        print(' '.join(blanks))
    else:
        if guess in x:
            index = x.index(guess)
            blanks[index] = guess
            print(' '.join(blanks))
        else:
            print('guess is wrong')
            turns -= 1
            print(HANGMANPICS[turns])
    if blanks == x:
        print('won')
        break

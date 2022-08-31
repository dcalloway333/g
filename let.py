import os
from os import system
from re import S
system("clear")

import random

words = ['texture', 'accurate', 'banana', 'terminal', 'identification', 'substitute', 'favourite', 'revolution', 'elaborate', 'consensus', 'monarch', 'genuine', 'essential', 'wallflower', 'supercilious', 'splendiferous', 'bamboozle', 'cornucopia', 'demitasse', 'doppelganger', 'ersatz', 'festooned', 'gizmo', 'heyday', 'interrobang', 'jalopy', 'juggernaut', 'lummox', 'mnemonic', 'razzmatazz']

hint = ['how something feels', 'on the mark', 'a yellow fruit', 'a word for a computer', 'A card to tell who are you', 'a person or thing acting or serving in place of another', 'preferred before all others of the same kind.', 'a forcible overthrow of a government or social order, in favor of a new system.', 'involving many carefully arranged parts or details; detailed and complicated in design and planning.', 'a general agreement.', 'a sovereign head of state, especially a king, queen, or emperor.', 'truly what something is said to be; authentic.', 'absolutely necessary; extremely important.', 'a person who has no one to dance with or who feels shy, awkward, excluded at a party or a flower', 'behaving or looking as though one thinks one is superior to others', 'splendid', 'fool or cheat', "an ornamental container shaped like a goat's horn", 'a small coffee cup', 'an apparition or double of a living person.', 'not real or genuine', 'a place with ribbons, garlands, or other decorations', 'a gadget', "the period of a person's or thing's greatest success, popularity, or vigor", 'a non-standard punctuation mark indicating a question expressed in an exclamatory manner', 'an old car in a dilapidated condition', 'a huge, powerful, and overwhelming force or institution', 'a clumsy, stupid person', 'aiding or designed to aid the memory', 'another term for razzle-dazzle']

space = []

l = ['Try again!', 'Take another jab!', 'Give it another round!', 'trying again wont hurt!', 'two more times!']
lose = random.choice(l)

w = ['Congratulations!', 'Nice Job!', 'Good Work!', 'Fantastic!', 'Well Done!']
win = random.choice(w)


randWord = random.choice(words)
chances = len(randWord) + 3




word = [*randWord]


for num in randWord:
    space.append('-')

h = words.index(randWord)
print('Hint - ' + hint[h])

print(' '.join(space))
# print(word)
# print(chances)


x = 1
low = chances - 1

print('You got ' + str(low) + ' chances left in this game')

while x < chances:
    x = x + 1
    low -= 1
   
    if '-' in space:
        letter = input('Please type a letter not a number: ')
        if letter in word:
            for num in range(len(word)):
                system('clear')
                if word[num] == letter:
                    space[num] = letter
            print('Hint - ' + hint[h])
            print('The letter ' + letter + ' was in the word!')
            print(' '.join(space))
            print('You have ' + str(low) + ' chances left')
       
       
        else:
            system('clear')
            print('Hint - ' + hint[h])
            print('The letter '+letter+' was not in the word.')
            print(' '.join(space))
            print('You have ' + str(low) + ' chances left')
   
   
    else:
        break


print('The word was ' + randWord)
if x == chances and '-' in space:
    print('Sorry YOU LOSE.')
    print(''.join(lose))


else:
    print('You Jest WON THE GAME!')
    print(''.join(win))


# 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

import os
from os import system
system("clear")
import random

bank = {'texture': 'how something feels', 'accurate': 'on the mark', 'banana': 'a yellow fruit', 'batman':'a viglinte that dresses as a bat', 'cowboys':'dallas based football team', 'halloween':'a holiday in which people dress up in costumes', 'export':'not inport but', 'python': 'coding language names after snake', 'collar':'something around a dogs neck', 'celtics': 'boston based basektball team', 'warriors':'won the 2022 nba finals', 'falcons':'atlanta based football team', 'cheifs':'kansas based football team', 'yankees': 'new york based baseaball team', 'bulls':'chicago based basektball team', 'pistons':'detroit based basektball team', 'rangers':'texas based baseball team', 'rams':'los angeles based football team', 'bucks':'milwaluke based basektball team', 'cubs':'chicago based baseball team', 'nets':'brooklyn based basketball team', 'rockets':'houston based basektball team', 'rays':'tampa bay based baseball team', 'ravens':'baltimore based football team' , 'braves':'atlanta based baseball team', 'mets':'new york based baseball team', 'stars':'dallas based hockey team', 'panthers':'carolina based football team', 'saints':'new orleans based football team', 'texans':'houston based football team', 'nationals':'washington d.c based baseball team'}
ran_value =random.choice(list(bank.items()))
ran_key =random.choice(list(bank.keys()))
print(ran_value)
print("Your word has", len(ran_key), "letters")

# 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
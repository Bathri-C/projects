import math
import random

start = int(input('enter a starting value of the range :: '))
end = int(input('enter ending vaule of the range :: '))
gen_rand = random.randint(start, end)

print('do you want chances from ur input \n or \ngenerating approximate chances ')
get = input(' if u want from ur chances TYPE : ME \n else TYPE : GEN \n::  ')
# def guess_count():
  # if get == 'me'.lower():
  #   int(input('how many chances do u want :: '))
  # elif get == 'gen':
gen_appr = round(math.log(end - start + 1, 2))
  # return get

count = 0

while count <= gen_appr:
    count += 1
    guess = int(input(f'enter ur {count} guess :) '))
    if guess == gen_rand:
        print(f'congrats u tried in {count} guess ;) ')
        break

    elif guess > gen_rand:
        print('u guess too high \n  enter lower int ')
    elif guess < gen_rand:
        print(f' u guess too low \n enter a higher int :) ')
if count > gen_appr :
    print(f'the number is {gen_rand} \n  BETTER LUCK NXT TIME :( ')


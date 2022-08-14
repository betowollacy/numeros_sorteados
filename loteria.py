#Adalberto de Oliveira
#14/08/2022
#Relembrando o modulo Random


import random

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

print("Before: ",numbers)
random.shuffle(numbers)
print("Later:",numbers)
#Before and Later

print("15 Lucky Numbers ",sorted(numbers[0:15]))

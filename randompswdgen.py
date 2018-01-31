import string
import random


def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 4
    return ''.join(random.choice(chars) for x in range(size,20))

n = 0

print ('Welcome to Random PWD GEN!')
print('NOW RENDERING -')
print('...')

while n<25:
    print(randompassword())
    n=n+1
    
print('...')
print('RENDERING COMPLETE')

print('END PROGRAM.-')


























print('...')
print('smitniko :)')

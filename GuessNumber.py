import random
x=random.randint(1, 9)
g=0
c=int(input('Guess a Number'))
if(c==x):
    print('you won')
else:
    while(c!=x):
        g+=1
        if(g<6):
            if(c>x):
              m='Enter a number smaller than'+str(c)
              c=int(input(m))
            elif(c==x):
                print('you won')
            elif(c<x):
                m='Enter a number greater than than'+str(c)
                c=int(input(m))
        else:
            print('you lost')
            quit()

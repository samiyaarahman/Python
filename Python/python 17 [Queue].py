#Queue (first in first out)
from collections import deque

bank= deque (["Avik","Rahi","Shimla"])

bank.popleft()
print (bank)

print ("Now the first person is :  ", bank[0])


bank.popleft()
bank.popleft()



if not bank:
    print ("No person left")
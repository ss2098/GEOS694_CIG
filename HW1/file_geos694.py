#import numpy as np
#print(np.random.choice(np.arange(1, 11), size=10, replace=False))

#main code 
import numpy as np

num = int(np.random.random() * 10) + 1
print(num)
#array from 1 to 10 randomly shuffled
arr=np.arange(1, 11)
np.random.shuffle(arr) 
print(arr)
result = arr[:num]
print(result)

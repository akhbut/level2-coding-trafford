# When importing libraries can either do: (this one imports the entire random library, which then requires you to select the methods you need from it)

import random

print(random.random())
print(random.uniform(1,10))
print(random.randint(1, 10))


# Or (this one searches the random library and only imports the methods you need)

from random import random, randint, uniform

print(random())
print(uniform(1,10))
print(randint(1,10))
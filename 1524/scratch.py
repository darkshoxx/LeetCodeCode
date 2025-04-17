from math import comb
for o in range(20):
    if o%2==0:
        end = int(o/2)
    else:
        end = int((o+1)/2)
    accumulator = 0
    for i in range(1, end+1):
        accumulator += comb(o,2*i-1)
    print(accumulator)
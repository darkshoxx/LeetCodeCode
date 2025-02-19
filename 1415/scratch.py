
init_dict = {
    1:"a",
    2:"b",
    3:"c",
}
next_small = {
    "a":"b",
    "b":"a",
    "c":"a"
}
next_large = {
    "a":"c",
    "b":"c",
    "c":"b"
}
import math
n = 1
leng = 3*2**(n-1)
for i in range(1,leng + 1):
    result = []
    chunk = int(leng/3)
    res = math.ceil(i/chunk)
    init = init_dict[res]
    prev = init
    result.append(prev)
    for _ in range(n-1):
        rem = ((i-1) % chunk)+1
        chunk = int(chunk/2)
        if rem <= chunk:
            prev = next_small[prev]
            result.append(prev)
        else:
            prev = next_large[prev]
            result.append(prev)
    print("".join(result))
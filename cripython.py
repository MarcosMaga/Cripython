import string

a = [" "]

for i in list(string.ascii_letters):
    a.append(i)

for i in list(string.digits):
    a.append(i)

for i in list(string.punctuation):
    a.append(i)

def encode(value, key, direction):
    result = ""
    val = 0

    for i in value:
        for x in range(len(a)):
            if i == a[x]:
                val = x + (key * direction)
                if val > len(a):
                    val -= len(a)
                elif val < 0:
                    val +- len(a)
                result+=a[val]
    return result

def decode(value, key, direction):
    result = ""
    val = 0

    for i in value:
        for x in range(len(a)):
            if i == a[x]:
                val = x + (key * (direction * -1))
                if val > len(a):
                    val -= len(a)
                elif val < 0:
                    val +- len(a)
                result+=a[val]
    return result

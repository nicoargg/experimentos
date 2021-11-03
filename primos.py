import time

def primos(max):
    n1 = 10000
    count = 0
    divisible = 0

    while max > count:
        n1 += 1
        count += 1
        divisible = 0
        for e in range(n1):
            primo = n1 % (e+1)
            if primo  == 0:
                divisible += 1
            if divisible > 2:
                break
        if divisible == 2:
            yield n1

if __name__ == '__main__':
    numbers = primos(100000000000000000000000000000000)
    for i in numbers:
        print(i)
        time.sleep(0.01)          

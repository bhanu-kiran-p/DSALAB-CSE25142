import time

def main():
    print("program starrt")
    stime = time.time()
    print(gcd(700000, 98000000000))
    etime = time.time()
    print(f"time taken : {etime-stime}")
    print(gcd(10, 5))


def gcd(a, b):
    mcf = 1
    for i in range (1, min(a,b)+1):  # never repeat this mistake . make sure to check for the 0 division error
        if a%i==0 and b%i==0:
            mcf = i
    return mcf

if __name__ == '__main__':
    main()
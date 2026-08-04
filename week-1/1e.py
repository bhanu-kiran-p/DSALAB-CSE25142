def main():
    print_fib(n)

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def print_fib(n):     
    for i in range(1, 9):
        print(fib(i))

if __name__ == '__main__':
    main()


    


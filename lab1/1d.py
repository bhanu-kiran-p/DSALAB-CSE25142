def main():
    result = fac(0)
    print(result)

def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)

if __name__ == '__main__':
    main()

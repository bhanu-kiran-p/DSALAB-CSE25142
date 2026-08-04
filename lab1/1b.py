def main():
    result1 = growth(2, 10)
    print(result1)
    result2 = growth(2, -1)
    print(result2)
    result3 = growth(2, 0) 
    print(result3)
    result4 = growth(-1, 9)
    print(result4)
    
def growth(p, n):
    if p < 0:
        print("principal growth cannot be negative : ", end = "")
        return
    if n == 0:
        return 1
    if n < 0:
        print("number of years cannot be negative : ", end="")
        return
    else:
        return p*growth(p, n-1)
    
if __name__ == '__main__':
    main()
    
    


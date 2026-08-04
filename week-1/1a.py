def main():
    launch(10)

def launch(n):
    if n == 0:
        print("launch")
    else:
        print(n)
        launch(n-1)
    
if __name__ == '__main__':
    main()
    
    



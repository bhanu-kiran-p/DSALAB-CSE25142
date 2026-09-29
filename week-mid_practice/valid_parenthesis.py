def main():
    str = "()(()[())])"
    print("the result is {}".format(valid_parenthesis(str)))
def valid_parenthesis(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[' or str[i]== '{':
            stack.append(str[i])
        elif str[i] == ')':
            if len(stack) == 0:
                return False
            if  stack.pop() != '(':
                return False
        elif str[i] == ']':
            if len(stack) == 0:
                return False
            if stack.pop() != '[':
                return False
        elif str[i] == '}':
            if len(stack) == 0:
                return False
            if stack.pop() != '{':
                return False
    if len(stack) == 0:
        return True
    return False
if __name__ == "__main__":
    main()
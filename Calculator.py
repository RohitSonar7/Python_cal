def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b


if __name__=="__main__":
    num1=int(input("Enter the first num"))
    num2=int(input("Enter the second num"))

    result = add(num1, num2)
    print(result)
    result = sub(num1, num2)
    print(result)
    result = mult(num1, num2)
    print(result)
    result = div(num1, num2)
    print(result)

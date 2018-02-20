def greeting(CustName, NumApples):
    print("Hello " + CustName)
    print"We have " + str(NumApples) + " apples"

def main():
    greeting("Ray", 10)

    apples = 5

    while apples > 0:
        print "We have " + str(apples) + " apples"
        apples -= 1


main()

while True:
    try:
        strAge = input("Enter your age: ")
        intAge = int(strAge)
        print("You are {} year(s) old.".format(intAge))
        break
    except:
        print("Enter digits. Please try again.")
    print("Still going.")
    print()

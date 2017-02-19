def cheer(s):
    'prints a cheer for team s'
    print("How do you spell winner?\nI Know, I Know!")
    for i in range(len(s)):
         print(s[i].upper(), end = " ")
    print('!')
    print("And that's how you spell winner!\nGo " + s + "!")

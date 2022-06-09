import time

print("Beggar Game!")
name = input("Enter your name to join the game:") #Enter name to start
print('''Hello, Loser {}! The mechanics is easy. There are 3-4 options and you only need to choose one.
Let us see where your choices can get you! Have fun!'''.format(name))
time.sleep(3) #timer

n = True

while True:

    print('''You need to go to the supermarket to buy groceries.\nOn your way, you saw a beggar. What will you do?''')

    print("[a] Give money.")
    print("[b] Give food.")
    print("[c] Join the beggar.")
    print("[d] Ignore.")
    x = input("Answer:") #1st 

    if x == 'a': #2nd       for choice a
        print("Beggar wants more money.")
        print("[a] Give more.")
        print("[b] Complain.")
        print("[c] Ignore.")
        y = input("Answer:")
        if y == 'a': #3rd   for choice aa
            print("Beggar wants more money.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a': #4th   for choice aaa
                print("[a] Go home. You don't have money anymore.")
            elif z == 'b':
                print("[b] You die.")
            elif z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        elif y == 'b':
            print("Beggar gets mad.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            elif z == 'b':
                print("[b] You die.")
            elif z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'c':
            print("Beggar follows you.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
    elif x == 'b':
        print("Beggar wants money.")
        print("[a] Give money.")
        print("[b] Complain.")
        print("[a] Ignore.")
        y = input("Answer:")
        if y == 'a':
            print("Beggar wants more money.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'b':
            print("Beggar gets mad.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'c':
            print("Beggar follows you.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
    elif x == 'c':
        print("Beggar gets mad.")
        print("[a] Give money.")
        print("[b] Complain.")
        print("[a] Ignore.")
        y = input("Answer:")
        if y == 'a':
            print("Beggar wants more money.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'b':
            print("Beggar gets mad.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'c':
            print("Beggar follows you.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
    elif x == 'd':
        print("Beggar follows you.")
        print("[a] Give money.")
        print("[b] Complain.")
        print("[c] Ignore.")
        y = input("Answer:")
        if y == 'a':
            print("Beggar wants more money.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'b':
            print("Beggar gets mad.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            if z == 'b':
                print("[b] You die.")
            if z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        if y == 'c':
            print("Beggar follows you.")
            print("[a] Give more.")
            print("[b] Complain.")
            print("[c] Ignore.")
            z = input("Answer:")
            if z == 'a':
                print("[a] Go home. You don't have money anymore.")
            elif z == 'b':
                print("[b] You die.")
            elif z =='c':
                print("[c] Beggar follows you home and your family dies.")
            else:
                print("You can only choose from ['a' 'b' 'c' 'd']")
                continue
        else:
            print("You can only choose from ['a' 'b' 'c' 'd']")
            continue
    else:
        print("You can only choose from ['a' 'b' 'c' 'd']")
        continue

    print('''\n Type quit to exit game.\n
    Press any other letter to Try Again.''')
    n = input()
    if n == 'quit': #quit the game
        break






import os


def main_menu():

    file = open("ascii art\castle1.txt",'r') 
    print (file.read())

    
    print("""
    1.create character and start a game
    2.highscores
    3.how to play
    4.authors
    5.exit""")
    

    choice = input("Type a number: ")
    if choice == '1':
        pass

    elif choice == '2':
        pass

    elif choice == '3':
        file = open("ascii art\howtoplay.txt",'r') 
        print (file.read())
        back = input("press b to go back to main menu")
        if back == 'b':
            main_menu()
        else:
            print("press b")

    elif choice == '4':
        file = open("ascii art\Authors.txt",'r') 
        print (file.read())
        back = input("press b to go back to main menu")
        if back == 'b':
            main_menu()
        else:
            print("press b")

    elif choice == '5':
        quit()
 
    

def main():
    main_menu()


main()












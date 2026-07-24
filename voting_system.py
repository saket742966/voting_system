from voting import *

while True :
    print("\n" + "=" * 50)
    print(" " * 17 + "VOTING SYSTEM")
    print("=" * 50 + "\n")

    print("1. View Candidates")
    print("2. Cast Vote")
    print("3. View Results")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1 :
        view_candidates()
        
    elif choice == 2 :
        cast_vote()
        
    elif choice == 3 :
        print("View Results Selected")
        
    elif choice == 4 :
        print("Exiting ... ")
        break
        
    else :
        print("Invalid Input !")

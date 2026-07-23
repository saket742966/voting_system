candidates = [
    "Candidate A",
    "Candidate B",
    "Candidate C"
]

votes = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}


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
        print("View Candidates Selected")
        
    elif choice == 2 :
        print("Cast Vote Selected")
        
    elif choice == 3 :
        print("View Results Selected")
        
    elif choice == 4 :
        print("Exiting ... ")
        break
        
    else :
        print("Invalid Input !")

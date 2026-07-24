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

def view_candidates():
    print("\n" + "=" * 50)
    print(" " * 17 + "CANDIDATES")
    print("=" * 50 + "\n")
    
    for index, candidate in enumerate(candidates, start = 1):
        print(f"{index}. {candidate}")
    
def cast_vote():
    print("\n" + "=" * 50)
    print(" " * 17 + "CAST VOTE")
    print("=" * 50)

    print()

    for index, candidate in enumerate(candidates, start=1):
        print(f"{index}. {candidate}")

    while True:
        try:
            choice = int(input("\nEnter candidate number: "))

            if choice < 1 or choice > len(candidates):
                print("Invalid candidate number. Please try again.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    selected_candidate = candidates[choice - 1]

    votes[selected_candidate] += 1

    print(f"\nVote cast successfully for {selected_candidate}!")
    


def view_results():
    print("\n" + "=" * 50)
    print(" " * 17 + "VOTING RESULTS")
    print("=" * 50)

    print()

    highest_votes = -1
    winner = ""

    for candidate in votes:
        print(f"{candidate:<20} : {votes[candidate]}")

        if votes[candidate] > highest_votes:
            highest_votes = votes[candidate]
            winner = candidate

    print("\n" + "-" * 50)
    print(f"Winner              : {winner}")
    print(f"Votes                : {highest_votes}")
    print("-" * 50)
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
    

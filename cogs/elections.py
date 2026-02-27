# Election System

class Election:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def cast_vote(self, candidate):
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            print(f"{candidate} is not a valid candidate.")

    def get_winner(self):
        return max(self.votes, key=self.votes.get)

# Example usage:
if __name__ == '__main__':
    election = Election(['Alice', 'Bob', 'Charlie'])
    election.cast_vote('Alice')
    election.cast_vote('Bob')
    election.cast_vote('Alice')
    print(f'The winner is: {election.get_winner()}')

class VotingCog:
    def __init__(self):
        self.votes = {}

    def start_vote(self, bill_title):
        self.votes[bill_title] = {'yes': 0, 'no': 0}
        return f'Voting started for: {bill_title}'

    def cast_vote(self, bill_title, vote):
        if bill_title not in self.votes:
            return 'Vote not found!'
        if vote.lower() == 'yes':
            self.votes[bill_title]['yes'] += 1
        elif vote.lower() == 'no':
            self.votes[bill_title]['no'] += 1
        else:
            return 'Invalid vote! Use yes or no.'
        return f'Vote counted for {vote.lower()} on {bill_title}'

    def view_results(self, bill_title):
        if bill_title not in self.votes:
            return 'Vote not found!'
        yes_votes = self.votes[bill_title]['yes']
        no_votes = self.votes[bill_title]['no']
        return f'Results for {bill_title}: Yes: {yes_votes}, No: {no_votes}'

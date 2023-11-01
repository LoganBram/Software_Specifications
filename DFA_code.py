class NFA:

    def __init__(self):
        self.states = ['A', 'B', 'C', 'D', 'E', 'F', 'dead']
        self.alphabet = [0, 1]

        self.transitions = {'A': ['B', 'dead'], 'B': ['C', 'D'], 'C': ['dead', 'A'],
                            'D': ['E', 'dead'], 'E': ['F', 'D'], 'F': ['C', 'D'], 'dead': ['dead', 'dead']}
        self.curr_state = 'A'
        self.accept = ['A', 'D', 'E']

    def main(self, input):
        # loop through input
        for i in input:
            # check if value is 0 or 1
            try:
                if int(i) not in self.alphabet:
                    print("integer not in alphabet")
                    break
            except:
                print("value not integer")

    # change state based on transition dict
            self.curr_state = self.transitions[self.curr_state][int(i)]
            print(self.curr_state)

        if self.curr_state in self.accept:
            print('accepted')
        else:
            print('rejected')


nfa = NFA()
nfa.main("001")

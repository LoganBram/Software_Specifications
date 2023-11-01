
class DFA:

    def __init__(self):
        # transitions are in order of input [a,b,/,*]
        self.transitions = {'A': ['dead', 'dead', 'B', 'dead'], 'B': ['dead', 'dead', 'dead', 'C'], 'C': ['C', 'C', 'C', 'D'],
                            'D': ['C', 'C', 'E', 'D'], 'E': ['dead', 'dead', 'dead', 'dead'], 'dead': ['dead', 'dead', 'dead', 'dead']}
        self.accept = 'E'
        self.curr_state = 'A'

    # a=0, b=1, /=2, *=3

    def main(self, input):

        for i in input:
            if i == 'a':
                index = 0
            elif i == 'b':
                index = 1
            elif i == '/':
                index = 2
            elif i == '*':
                index = 3
            else:
                print('invalid string input')
                break
            self.curr_state = self.transitions[self.curr_state][index]
            print(self.curr_state)
        if self.curr_state == self.accept:
            print("accepted")
        else:
            print("not accepted")


dfa = DFA()
dfa.main('/*ab*/')

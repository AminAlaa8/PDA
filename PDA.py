
### Github Link :

#### a Pushdown Automaton that recognizes the language {0^n 1^n | n ≥ 0}. ####

# actions: push, pop, input  // input,pop ==> push
class PDA:
    def __init__(self):
        # Initialize the PDA with a stack containing '$'.
        self.stack = ['$']

    def push(self, symbol):
        # Push a symbol onto the stack.
        self.stack.append(symbol)

    def pop(self):
        # Pop a symbol from the stack. If the stack contains only '$', return None.
        if self.stack[-1] == '$':  # ['$',_,_,_]
            return '$'
        else:
            return self.stack.pop()

    def process_input(self, input_string):
        # Process the input string to recognize the language {0^n 1^n | n ≥ 0}.
        current_state = 0
#['$']0001111
        for symbol in input_string:  # 000111  ==>['$']
            if current_state == 0 and symbol == '0':
                self.push(symbol)
            elif current_state == 0 and symbol == '1' and self.pop() != '$':  # 011
                pass  # Continue processing
            else:
                # Transition to a non-accepting state if the input is not valid
                current_state = -1
                break

        # Check if the stack contains only '$' and the input is valid
        if current_state == 0 and self.pop() == '$':
            print("Accepted: 0^n 1^n")
        else:
            print("Rejected: Not 0^n 1^n")


#### a Pushdown Automaton that recognizes the language of even and odd Palindrome. ####

class PalindromePDA:
    def __init__(self):
        # Initialize the PalindromePDA with a stack containing '$'.
        self.stack = ['$']

    def push(self, symbol):
        # Push a symbol onto the stack.
        self.stack.append(symbol)

    def pop(self):
        # Pop a symbol from the stack. If the stack contains only '$', return None.
        if self.stack[-1] == '$':  # ['$',_,_,_]
            return '$'
        else:
            return self.stack.pop()

    def process_input(self, input_string):
        # Process the input string to recognize palindrome strings.

        current_state = 0
#1010  ['$',1,0,1]
        for symbol in input_string:
            self.push(symbol)

        # Check if the input is a palindrome
        for symbol in input_string:         # 0110           symbol=1
            popped_symbol = self.pop()      # ['$',0,1,1,0]  popped_symbol=0
            if popped_symbol == '$' or popped_symbol != symbol:
                current_state = -1
                break

        # Check if the stack is empty (contains only '$') and the input is valid
        if current_state == 0 and self.pop() == '$' and len(input_string) % 2 == 0: #4/2=2
            print("Accepted: Even Palindrome")
        elif current_state == 0 and self.pop() == '$' and len(input_string) % 2 != 0:#5/2=2 ,1
            print("Accepted: Odd Palindrome")
        else:
            print("Rejected: Not a Palindrome")


def main():
    # Main function to interactively choose and test PDAs.
    print("Choose a PDA:")
    print("1. PDA (Recognizes {0^n 1^n | n ≥ 0})")
    print("2. Palindrome PDA (Recognizes palindrome strings)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        pda = PDA()
        input_string = input("Enter a string of 0s and 1s: ")
        pda.process_input(input_string)
    elif choice == '2':
        palindrome_pda = PalindromePDA()
        input_string = input("Enter a string of 0s and 1s: ")
        palindrome_pda.process_input(input_string)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    while True:
        main()
        print("+______________________________________________+\n")

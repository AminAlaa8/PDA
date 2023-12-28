import streamlit as st


class PDA:
    def __init__(self):
        self.stack = ['$']

    def push(self, symbol):
        self.stack.append(symbol)

    def pop(self):
        if self.stack[-1] == '$':
            return '$'
        else:
            return self.stack.pop()

    def process_input(self, input_string):
        current_state = 0

        for symbol in input_string:
            if current_state == 0 and symbol == '0':
                self.push(symbol)
            elif current_state == 0 and symbol == '1' and self.pop() != '$':
                pass
            else:
                current_state = -1
                break

        if current_state == 0 and self.pop() == '$':
            st.success("Accepted: 0^n 1^n")
        else:
            st.error("Rejected: Not 0^n 1^n")


class PalindromePDA:
    def __init__(self):
        self.stack = ['$']

    def push(self, symbol):
        self.stack.append(symbol)

    def pop(self):
        if self.stack[-1] == '$':
            return '$'
        else:
            return self.stack.pop()

    def process_input(self, input_string):
        current_state = 0

        for symbol in input_string:
            self.push(symbol)

        for symbol in input_string:
            popped_symbol = self.pop()
            if popped_symbol == '$' or popped_symbol != symbol:
                current_state = -1
                break

        if current_state == 0 and self.pop() == '$' and len(input_string) % 2 == 0:
            st.success("Accepted: Even Palindrome")
        elif current_state == 0 and self.pop() == '$' and len(input_string) % 2 != 0:
            st.success("Accepted: Odd Palindrome")
        else:
            st.error("Rejected: Not a Palindrome")


def main():
    st.title("Pushdown Automaton Simulator")

    choice = st.radio("Choose a PDA:", [
                        "PDA (Recognizes {0^n 1^n | n ≥ 0})", "Palindrome PDA (Recognizes palindrome strings)"])

    if choice == "PDA (Recognizes {0^n 1^n | n ≥ 0})":
        pda = PDA()
        input_string = st.text_input("Enter a string of 0s and 1s:")
        if st.button("Process Input"):
            pda.process_input(input_string)
    elif choice == "Palindrome PDA (Recognizes palindrome strings)":
        palindrome_pda = PalindromePDA()
        input_string = st.text_input("Enter a string of 0s and 1s:")
        if st.button("Process Input"):
            palindrome_pda.process_input(input_string)


if __name__ == "__main__":
    main()

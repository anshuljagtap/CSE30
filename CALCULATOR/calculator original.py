

# function to convert infix notation to postfix notation
def infix_to_postfix(infix):
    # define the operator precedence dictionary
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    # initialize an empty stack and output string
    stack = []
    output = []

    # iterate over each token in the infix string
    for token in infix.split():
        # if the token is an operand, add it to the output string
        if token.isnumeric():
            output.append(token)
        # if the token is an operator
        elif token in precedence:
            # while the stack is not empty and the top operator has higher precedence than the token
            while stack and precedence[stack[-1]] >= precedence[token]:
                # pop the top operator from the stack and add it to the output string
                output.append(stack.pop())
            # push the token onto the stack
            stack.append(token)
        # if the token is a left parenthesis, push it onto the stack
        elif token == '(':
            stack.append(token)
        # if the token is a right parenthesis
        elif token == ')':
            # pop operators from the stack and add them to the output string
            # until the corresponding left parenthesis is reached
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            # pop the left parenthesis from the stack and discard it
            stack.pop()

    # pop any remaining operators from the stack and add them to the output string
    while stack:
        output.append(stack.pop())

    # return the postfix expression as a string
    return ' '.join(output)


# function to calculate the value of an arithmetic expression
def calculate(expression):
    # convert the infix expression to postfix notation
    postfix = infix_to_postfix(expression)

    # initialize an empty stack
    stack = []

    # iterate over each token in the postfix expression
    for token in postfix.split():
        # if the token is an operand, push it onto the stack
        if token.isnumeric():
            stack.append(float(token))
        # if the token is an operator, pop two operands from the stack,
        # apply the operator, and push the result back onto the stack
        elif token == '+':
            op2, op1 = stack.pop(), stack.pop()
            stack.append(op1 + op2)
        elif token == '-':
            op2, op1 = stack.pop(), stack.pop()
            stack.append(op1 - op2)
        elif token == '*':
            op2, op1 = stack.pop(), stack.pop()
            stack.append(op1 * op2)
        elif token == '/':
            op2, op1 = stack.pop(), stack.pop()
            stack.append(op1 / op2)
        elif token == '^':
            op2, op1 = stack.pop(), stack.pop()
            stack.append(op1 ** op2)

    # the final value of the expression is the only element left in the stack
    return stack.pop()


# main driver code
if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        expression = input("Please enter your expression here. To quit enter 'quit' or 'q': ")
        if expression == 'quit' or expression == 'q':
            print("Goodbye!")
            break
        try:
            result = calculate(expression)
            print(result)
        except:
            print("Invalid expression. Please try again.")
        print("Please enter your expression here. To quit enter 'quit' or 'q': ")

 
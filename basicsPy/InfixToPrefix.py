
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def isOperand(ch):
    return ch.isalpha() or ch.isdigit()


def infix_to_prefix(expression):
   
    expression = expression[::-1]


    expression = list(expression)
    for i in range(len(expression)):
        if expression[i] == '(':
            expression[i] = ')'
        elif expression[i] == ')':
            expression[i] = '('
    expression = ''.join(expression)

    
    stack = []
    result = ''

    for ch in expression:
        if isOperand(ch):
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
          
            while stack and precedence(ch) < precedence(stack[-1]):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()


    prefix = result[::-1]
    return prefix


infix_expr = "A+B*C"
print("Infix Expression:", infix_expr)
print("Prefix Expression:", infix_to_prefix(infix_expr))

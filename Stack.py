def is_balanced(expression):
    #empty stack to keep track 
    stack = []
    
    #dictionary to store the mapping of bracket
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_pairs.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs.keys():
            # Check if the stack is not empty 
            if not stack or bracket_pairs[char] != stack.pop():
                # Return False if brackets are not balanced
                return False

    # Return True if the stack is empty at the end 
    return not stack

# Sample input
expression1 = "([]{})"
expression2 = "([)]"

# Test cases
print(is_balanced(expression1))  
print(is_balanced(expression2))  

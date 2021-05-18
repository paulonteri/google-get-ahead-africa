""" 
Balanced Parenthesis:

Given a string of parentheses, find the size of the longest contiguous substring of balanced parentheses.
Parentheses are considered balanced when there is a valid closing parenthesis for an opening one.

Example: 
    In this string: ())(()), the longest continuous set would be 4 characters long (the last 4 characters of the input):
"""


def longest_balanced(string):

    longest_length = 0
    stack = []  # stack used to store indeces of the opeing brackets we saw
    for idx, bracket in enumerate(string):

        # opening
        if bracket == '(':
            # store index of the last opening bracket we saw
            stack.append(idx)

        # closing
        else:
            if len(stack) > 0:
                # the size of the contiguous substring of balanced parentheses is the distance between
                #  the current closing bracket & the last opening bracket we saw
                opening_bracket_pos = stack.pop()
                curr_length = (idx - opening_bracket_pos) + 1

                longest_length = max(curr_length, longest_length)

    return longest_length

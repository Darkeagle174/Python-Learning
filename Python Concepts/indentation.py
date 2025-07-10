# Identation refers to the spaces or tabs at the beginning of a line of code.
# In Python, indentation is used to define the scope of loops, functions, and classes.
if 5 > 2:
    print("Five is greater than two!") # This line is indented, so it belongs to the if block
    
# if 5 > 2:
# print("Five is greater than two!") # This line is not indented, so it does not belong to the if block

if 5 > 2:
    print("Five is greater than two!") # This line is indented, so it belongs to the if block
    print("This is also part of the if block") # This line is also indented, so it belongs to the if block
    #same no. of space should be given for the lines inside the same block
print("This line is outside the if block") # This line is not indented, so it does not belong to the if block

# if ( 5 > 2):
#     print("Five is greater than two!") # This line is indented, so it belongs to the if block
#         print("This is also part of the if block") # This line is indented with more spaces, so it does not belong to the if block it causes an IndentationError
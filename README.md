Muzaffarhusain Turak mturak@stevens.edu
Aaryaman Katoch akatoch@stevens.edu

Url:https://github.com/tmuzu98/bcCalculator

Estimate time spent: 15-20 hours

# a description of how you tested your code
Here is a list of tests that we performed to ensure the code works correctly for various cases, including negative numbers, arithmetic operations, comparisons, logical operations, and comments
1. Basic Arithmetic Operations
x = 3
y = 4
print x + y
print x - y
print x * y
print x / y
print x % y
print x ^ y
2. Using negative numbers:
x = -3
y = 4
print x + y
print x - y
print x * y
print x / y
print x % y
print x ^ y
3. Comparison operators:
x = 5
y = 6
print x == y
print x != y
print x < y
print x > y
print x <= y
print x >= y
4. Logical operators:
x = 1
y = 0
print x && y
print x || y
print !x
print !y
5. Increment and decrement:
x = 5
x += 1
print x 
x -= 1
print x
x *= 2
print x 
x /= 2
print x
x %= 3
print x 
x ^= 2
print x
6. Using variables: 
a = 3
b = 4
c = a + b
print c
7. Expressions with multiple operators:
x = 1
y = 2
z = 3
print x + y * z
print (x + y) * z
8. Comments:
x = 5 # This is a comment
y = 6 /* This is a
         multiline comment */
print x + y

# any bugs or issues you could not resolve



# an example of a difficult issue or bug and how you resolved
Issue: Handling negative numbers in the custom parser
While working on a custom parser for a mini language, we encountered a bug where the parser failed to handle negative numbers as inputs, like x = -1. The code raised a "pop from empty list" error when attempting to parse negative numbers.

Resolution:
Identify the issue: We traced the issue back to the parse_expression function. The function failed to properly recognize and handle negative numbers in the input expressions.

Modify the tokenization process: To fix this issue, we updated the tokenization process to recognize the negative sign in front of a number as part of the number. This was achieved by modifying the regular expression used to tokenize the input expression.

Update the parsing logic: Next, we modified the parsing logic in the parse_expression function to correctly handle the negative numbers during evaluation. Specifically, we added a check to ensure that the op_stack was not empty before attempting to pop an item from it. This resolved the "pop from empty list" error.

Test the fix: To ensure that the bug was resolved and the parser was working as expected, we performed extensive testing, including tests with negative numbers and various other cases such as arithmetic operations, comparisons, logical operations, and comments.


By following these steps, we were able to resolve the difficult issue of handling negative numbers in the custom parser. The process involved identifying the root cause, updating the tokenization and parsing logic, and testing the fix with various test cases to ensure the parser worked correctly.

# a list of the four extensions you’ve chosen to implement
Following is the list of four extensions that we've chosen to implement in the code:
1. Op-equals: Every binary action, such as +=, -=, *=, /=, %=, and =, has the op-equals feature built in. x op= e means the same thing as x = x op(e). To deal with the op-equals requirements, the code does the following:

Regular expression matching: To match the op-equals pattern, the code in the parse_assignment method uses the regular expression r'([A-Za-z_][A-Za-z0-9_]*)s*([+-*/%]=). This regular expression looks for two groups: the name of the variable (like "x") and an operator followed by an equal sign (like "+=").

Extract variable and operator: If the op-equals pattern matches, the code calls the groups() method on the match object to get the variable name and the operator. The equal sign is also taken away from the user.

Parse the expression: The code then parses the expression on the right side of the op-equals assignment. It does this by sending the rest of the line after the op-equals match to the parse_expression() function.

Update the variable: Once the code has successfully parsed the expression and gotten the result, it uses the appropriate binary operation to update the variable in the variables dictionary. The code looks in the operators dictionary to find the right function for the operator (for example, lambda x, y: x + y for "+") and then calls that function with the current value of the variable (or 0 if the variable hasn't been defined yet) and the parsed expression value.

By doing these things, the code is able to handle the op-equals requirements for all the binary operations that it supports.

2. Relational operations: The relational operations (==, =, >=,!=,, >) are handled by the code by using 1 for true and 0 for false, as stated. Here are the steps for putting relationship operations into action:

Define operators: The code's operators dictionary has the meanings for all relational operations that can be used. Each operator is mapped to a tuple with its precedence, associativity, and a lambda function that does the action. Relational operators have a priority value of 0, which makes them less important than arithmetic operators. The associativity is set to "left," which makes sure that these operators have left associativity.

Tokenize the expression. Using a regular expression, the parse_expression method tokenizes the expression you give it. The regular expression is made to match all available operators, including relational operators.

Process tokens: Then it process the tokens in the input phrase by the parse_expression function. When a relational operator is found, the function compares the operator's precedence and associativity to the operators on the op_stack. If the operator on the stack has a greater precedence or the same precedence with left associativity, the function uses the operator on the stack on the operands.

Evaluate the relational operation. When a relational operator is found in the op_stack, the lambda function linked with that operator is called with the operands (output list). This lambda function checks if the relational action is true or false and returns 1 or 0. The result is added back to the list of things to be sent out.

By doing these things, the code handles the relational operations with the stated precedence and associativity rules and returns the expected results with 1 for true and 0 for false.

3. Boolean operations: The code handles the boolean operations (&&, ||, and!) by handling any number that is not zero as true and returning either 1 or 0. Here are the steps for putting it into action:

Define operators: The operators dictionary has definitions for all boolean functions that can be used. Each operator is mapped to a tuple with its precedence, associativity, and a lambda function that does the action. The precedence values for boolean operators are set to be lower than both arithmetic and relational expressions. Associativity is described as "left" for && and ||, while! is "non-associative."

Tokenize the expression: The parse_expression function tokenizes the input expression by matching all available operators, including boolean operators, with a regular expression.

Process tokens: It then processes the tokens in the input phrase by the parse_expression function. When a boolean operator is found, the function compares the operator's precedence and associativity to the operators on the op_stack. If the operator on the stack has a higher precedence or the same precedence with left associativity (for && and ||), the function uses the operator on the stack on the operands.

Evaluate the boolean operation. When a boolean operator is found in the op_stack, the lambda function linked with that operator is called with the operands (output list). This lambda function checks if the boolean operation is true or false and gives 1 or 0. Only one operand is needed for the! operator, which gives 1 if the operand is 0 (false) and 0 if it is not 0 (true). The result is added back to the list of things to be sent out.

By doing these things, the code handles the boolean operations according to the stated precedence and associativity rules and returns the expected results using 1 for true and 0 for false. As part of the operators dictionary, the boolean functions can also be used with the op-equals extension.

4. The code handles both comments with more than one line and comments with just one line. Here's a short summary of how the code handles comments:

Remove comments: The remove_comments method is in charge of removing both multi-line and single-line comments from the input program. This function is called at the start of the parse code to make sure that comments are taken out before processing continues.

Remove comments that span multiple lines. The remove_comments method uses the regular expression r'/*(?:.|[rn])*?*/' to remove comments that span multiple lines. This expression matches a string that starts with /*, continues with any mix of characters (including line breaks), and ends with */. By replacing all matches with an empty string, the re.sub() method gets rid of multi-line comments from the program.

Remove single-line comments. The regular expression r'#.*' is used by the remove_comments function to remove single-line comments. This formula looks for a string of characters that starts with # and goes on until the end of the line. By replacing all matches with an empty string, the re.sub() method gets rid of single-line comments from the program.

By doing these steps, the code handles both multi-line and single-line comments as expected, making sure that the comments are cleared before the program is parsed and run.

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
stack = stack.Stack()

for letters in string:
    stack.push(letters)

print(stack)
while not stack.is_empty():
    reversed_string += stack.pop()
print(reversed_string)



print(reversed_string)

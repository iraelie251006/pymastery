# Write your code below and press Shift+Enter to execute

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

i = 0

while (i < len(squares)) and (squares[i] == 'orange'):
    new_squares.append(squares[i])
    i += 1
    
print(new_squares)
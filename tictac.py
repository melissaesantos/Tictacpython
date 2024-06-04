import turtle

# Initialize the turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Function to draw the grid
def draw_grid():
    pen.penup()
    pen.goto(-50, 150)
    pen.pendown()
    pen.goto(-50, -150)
    pen.penup()
    pen.goto(50, 150)
    pen.pendown()
    pen.goto(50, -150)
    pen.penup()
    pen.goto(-150, 50)
    pen.pendown()
    pen.goto(150, 50)
    pen.penup()
    pen.goto(-150, -50)
    pen.pendown()
    pen.goto(150, -50)
    pen.penup()

# Function to draw a character in a tile
def draw_char(tile, char):
    x_coords = [-100, 0, 100, -100, 0, 100, -100, 0, 100]
    y_coords = [100, 100, 100, 0, 0, 0, -100, -100, -100]
    x = x_coords[tile-1]
    y = y_coords[tile-1]
    pen.penup()
    pen.goto(x, y - 20)  # Adjust y position to center the character
    pen.write(char, align="center", font=("Arial", 32, "bold"))

# Function to check for a winner
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if taken[combo[0]] == taken[combo[1]] == taken[combo[2]] != 0:
            return taken[combo[0]]
    return None

# Initialize the game state
taken = [0] * 9
turn = 0

# Draw the initial grid
draw_grid()

# Main game loop
while turn < 9:
    current_turn = "X" if turn % 2 == 0 else "O"
    tile = int(input(f"It's {current_turn}'s turn. Where will you play (1-9)? "))
    if tile < 1 or tile > 9:
        print("Invalid tile. Choose a number between 1 and 9.")
        continue
    if taken[tile-1] != 0:
        print("That space is taken! Try again.")
        continue
    taken[tile-1] = current_turn
    draw_char(tile, current_turn)
    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
        break
    turn += 1
else:
    if not winner:
        print("It's a draw!")

print("Game over.")
turtle.done()
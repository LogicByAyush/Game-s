from tkinter import *
import random
# ---------------- Window ----------------
WIDTH = 600
HEIGHT = 600
SIZE = 20
SPEED = 100
root = Tk()
root.title("Snake Game")
#root.resizable(False, False)
# ---------------- Score ----------------
score = 0
score_label = Label(root,text=f"Score: {score}",font=("Arial", 16))
score_label.pack()
# ---------------- Canvas ----------------
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()
# ---------------- Snake ----------------
snake = [[100, 100],[10, 10]]
#----------------- starting direction
direction = "Right"
# ---------------- Food ----------------
def create_food():
    x = random.randint(0, (WIDTH // SIZE) - 1) * SIZE
    y = random.randint(0, (HEIGHT // SIZE) - 1) * SIZE
    return [x, y]
food = create_food()
# ---------------- Draw ----------------
def draw():
    canvas.delete("all")
    # Food
    canvas.create_oval(
        food[0], food[1],
        food[0] + SIZE, food[1] + SIZE,
        fill="red"
    )
    # Snake
    for segment in snake:
        canvas.create_rectangle(segment[0], segment[1],segment[0] + SIZE,segment[1] + SIZE,fill="green")
# ---------------- Direction ----------------
def change_direction(event):
    global direction
    if event.keysym == "Up" and direction != "Down":
        direction = "Up"
    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"
    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"
    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"
# ---------------- Game Over ----------------
def game_over():
    canvas.delete("all")
    canvas.create_text(WIDTH // 2,HEIGHT // 2,text=f"GAME OVER\nScore: {score}",fill="white",font=("Arial", 24))
# ---------------- Move ----------------
def move():
    global food
    global score
    head_x = snake[0][0]
    head_y = snake[0][1]
    if direction == "Right":
        head_x += SIZE
    elif direction == "Left":
        head_x -= SIZE
    elif direction == "Up":
        head_y -= SIZE
    elif direction == "Down":
        head_y += SIZE
    new_head = [head_x, head_y]
    # Wall Collision
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT):
        game_over()
        return
    # Self Collision
    if new_head in snake:
        game_over()
        return
    snake.insert(0, new_head)
    # Food Collision
    if new_head == food:
        score += 1
        score_label.config(text=f"Score: {score}")
        food = create_food()
    else:
        snake.pop()
    draw()
    root.after(SPEED, move)
# ---------------- Start ----------------
root.bind("<Key>", change_direction)
draw()
move()
root.mainloop()
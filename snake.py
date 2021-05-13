from tkinter import messagebox
from turtle import *
from random import *
from tkinter import *
from base import vector, square # This is the vector movement, with magic implementations ( overload components )

food = vector(0, 0)
snake = [vector(10, 0)] # A list of vectors - the body starts with a initial vector but increases each time eats other vector (food)
speed = 10
aim = vector(0,-speed) # Moves the snake


def run_game():

  # Updates the values of the aim
  def change(x, y):
    "change snake direction"
    aim.x = x
    aim.y = y

  # Define boundaries
  def inside(head):
    "return True if head is isinde the boundary"
    return -200 < head.x < 190 and -200 < head.y < 190


  # Move function
  # Retrieves the head of the snake and copy it to move it with the aim ( the aim is updated in change function )
  def move():
    "move the snake forward"
    # The Head will be the last element of the list
    head = snake[-1].copy() # The Head will be the last element of the list
    head.move(aim)


  # Two conditions for end game
  #===========================
  # 1 - The head is not inside of the boundaries (-200, 190)
  # 2 - The head is ate itself or its body --> 'a' in 'abc' --> true // head in snake
    if not inside(head) or head in snake:
      square(head.x, head.y, 9, 'red') # Shows the snake as dead
      update() # You need to update each time you render something otherwise won't be render
      score = "Your total score is {}.".format(len(snake) - 1)
      message = messagebox.showinfo("Game over ", score)
      print(message)

      if message == "ok":
        bye()
        return # return false an the game is terminated


    snake.append(head)

    ## Has the snake eaten ? 
    if head == food: # Head and food are in the same position
      print("Snake point: ", len(snake))
      # Updates the new food position ( random )
      food.x = randrange(-15, 15) * 10 # Range between -150 and 150 in the screen
      food.y = randrange(-15, 15) * 10
    
    else : # Snake has not eaten!
      snake.pop(0)

    clear() # This methoed is from Turtle module


    ##  Increases the lenght of the body's snake
    for body in snake:
      square(body.x, body.y, 9, 'orange') # This square method uses the Turtle method BUT is defined in base.py

    ##  Renders food
    square(food.x, food.y, 9, 'black')  
    update()

    ##  Initialiazes movement 
    ontimer(move, 100)



  # Turtle setup
  setup(420, 420, 370, 0) # Setup the screen -- This module comes from Turtle --> turtle.setup
  hideturtle() # Hides the cursor - this is from Turtle module
  tracer(False) # Removes the delay
  listen()


  # event handling - arrow keys
  onkey(lambda: change(speed,0), 'Right') # x and y
  onkey(lambda: change(-speed,0), 'Left')
  onkey(lambda: change(0,speed), 'Up')
  onkey(lambda: change(0,-speed), 'Down')
  move() # Calls the move method - will be called every 100 millliseconds - check the move() function
  done()

run_game()
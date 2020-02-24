# Even and Odd Game by Armon Burton
# For INFO 697 - Rapid Prototyping and Physical Computing
# Using A Button and B Button on Microbit unit for user 
# inputs and LCD module for directions.
# Game has 10 questions and returns results to user after they finish

#import libraries
from microbit import *
from mb_i2c_lcd1602 import *
import random

# initialize variables
lcd=LCD1620()
score = 0
probnum = 0
correctscore = 0
wrongscore = 0
gamestatus = False

# Game Title and prompt to user to start game by pressing A Button on Microbit.
# By default, game status is set to false. Once A button is press, game status 
# is set to True and enters 2nd while loop to start game.
while gamestatus is False:
    lcd.clear()
    lcd.puts('Ready to play', 1 ,0)
    lcd.puts('Even or Odd???', 1 ,5)
    sleep(2500)
    lcd.clear()
    lcd.puts('10 timed probs', 0 ,0)
    lcd.puts('Press A to play!', 0 ,5)
    sleep(2500)
    if (button_a.was_pressed()):
        lcd.clear()
        gamestatus = True


# While loop where 10 random numbers are generated, displayed, and inputs by 
# users are checked. User will use A button for Even and B button for Odd
# Correct answer shows a check mark e.g. Image.YES
# Incorrect answer or failure to answer within 2 secs shows X. e.g. Image.NO
while (probnum < 10) and gamestatus is True:
    lcd.puts('Press A for EVEN', 0 ,0)
    lcd.puts('Press B for ODD', 0 ,5)

    # random number variable
    random_number = random.randint(1, 9)
    display.show(random_number)
    sleep(2000)
    
    # If statement when user correctly guess even number with A button the output is a checkmark.
    if button_a.was_pressed() and (random_number % 2 == 0):
        display.show(Image.YES)
        sleep(1000)
        correctscore += 1

    # If statement when user correctly guess odd number with B button the output is a checkmark.
    elif button_b.was_pressed() and (random_number % 2 != 0):
        display.show(Image.YES)
        sleep(1000)
        correctscore += 1

    # Else if user guesses wrong or fails to answer, output X
    else:
        display.show(Image.NO)
        sleep(1000)
        wrongscore += 1
   
    # Increment to next number
    probnum = probnum + 1

# After user finishes 10 problems, clear LCD screen and output the score
lcd.clear()
lcd.puts('Score: ' + str(correctscore) + '/10', 0 ,0)

# depending on score output Happy (< 50%) or Sad face (> 50%) on Microbic.
# Also display message on LCD and directions to restart (reset) game to play again.
display.clear()
if (correctscore > wrongscore):
    display.show(Image.HAPPY)
    lcd.puts('Congrats!!', 0 ,5)
    sleep(3000)
    lcd.clear()
    lcd.puts('Press RESET to', 0 ,0)
    lcd.puts('play again!', 0 ,5)
else:
    display.show(Image.SAD)
    lcd.puts('Oh nooo!!', 0 ,5)
    sleep(3000)
    lcd.clear()
    lcd.puts('Press reset to', 0 ,0)
    lcd.puts('play again!', 0 ,5)
    
display.clear
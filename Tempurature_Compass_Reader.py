from microbit import *

# tempurature and compass variables.
# before starting you need to calibrate microbit.
# Follow the directions on the screen.
temperature = temperature()
compass = compass.heading()

while True:
    # user starts tempurature and compass reading by
    # pressing the A button on the Microbit and readings
    # are displayed on the microbit screen.
    if button_a.is_pressed():
        #display tempurature in celsius
        display.scroll("temp " + str(temperature) + "C")
        display.scroll("& compass " + str(compass))
        # file name data.csv is created to capture temp and compass readings
	# w for write to file and comma as delimiter.
        with open('data.csv', 'w') as file:
            file.write(str(temperature) + ',' + str(compass))
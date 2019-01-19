from sense_hat import SenseHat
sense = SenseHat()
sense.low_light = True

# Define the colours red and green
red = (55, 0, 0)
green = (0, 55, 0)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "T: " + str(t) + " P: " + str(p) + " H: " + str(h)
  
  if t > 18.3 and t < 26.7:
    bg = green
  else:
    bg = red
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, text_colour=(0, 50, 0), back_colour=bg)
A
A


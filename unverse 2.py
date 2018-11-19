from PIL import Image

background = Image.new('RGB', (500, 500), "black")  # create a new black image
foreground = Image.open("planets/planet_2.png")

background.paste(foreground, (0, 0), foreground)
background.show()
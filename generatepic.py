from images import Image
image = Image("Untitled.gif")
image.draw()
black_pixel = (0, 0, 0)
white_pixel = (255, 255, 255)
for y in range (image.getHeight()):
    for x in range (image.getWidth()):
        (r,g,b) = image.getPixel(x, y)
        avg = (r+g+b)//3
        if avg < 128:
            image.setPixel(x, y, black_pixel)
        else:
            image.setPixel(x, y, white_pixel)
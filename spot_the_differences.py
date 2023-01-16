from PIL import Image, ImageChops


# Open the image
im = Image.open("Spot_the_difference.png")


# Get the width and height of the image
width, height = im.size

# Crop the image in half horizontally
left = im.crop((0, 0, width/2, height))
right = im.crop((width/2, 0, width, height))

# Save the left and right halves
left.save("left.png")
right.save("right.png")

image1_path = Image.open("left.png")
image2_path = Image.open("right.png")

diffs = ImageChops.difference(image1_path, image2_path)

if diffs.getbbox():
    print("The images are different.")
    diffs.show()
else:
    print("The images are the same.")








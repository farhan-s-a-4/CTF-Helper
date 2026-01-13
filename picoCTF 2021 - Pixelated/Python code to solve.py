from PIL import Image

# 1. Load the source images
image1 = Image.open("scrambled1.png")
image2 = Image.open("scrambled2.png")

# Ensure both images are the same size, just in case
if image1.size != image2.size:
    print("Resizing image2 to match image1 size.")
    image2 = image2.resize(image1.size)

# 2. Create a blank destination image ('flag') in the correct mode (CMYK)
flag = Image.new("RGB", image1.size)

# 3. Load the PixelAccess objects for efficient access
array1 = image1.load()
array2 = image2.load()
flag_pixels = flag.load()

# Get image dimensions for looping
width, height = image1.size

# 4. Iterate through every pixel (X, Y coordinate)
for x in range(width):
    for y in range(height):
        # Get the pixel tuples (C, M, Y, K) from both source images
        pixels_img1 = array1[x, y]
        pixels_img2 = array2[x, y]

        # Add the corresponding channel values
        # Since pixel values can exceed 255 (the max value in an 8-bit image),
        # we typically clamp the result using min(255, value) to prevent errors or wrap-around
        new_r = (pixels_img1[0] + pixels_img2[0]) % 256
        new_g = (pixels_img1[1] + pixels_img2[1]) % 256
        new_b = (pixels_img1[2] + pixels_img2[2]) % 256

        # Assign the new combined pixel to the destination image
        flag_pixels[x, y] = (new_r, new_g, new_b)

# 5. Display and save the final result
flag.show()
flag.save("reconstructed_image.png")
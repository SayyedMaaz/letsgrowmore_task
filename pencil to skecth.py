
import cv2

# Step 1: Read the image in RGB format
image = cv2.imread('dog.jpg')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Invert the grayscale image
inverted_image = cv2.bitwise_not(gray_image)

# Step 4: Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)

# Step 5: Create the pencil sketch by dividing the grayscale image by the inverted blurred image
pencil_sketch = cv2.divide(gray_image, blurred_image, scale=256.0)

# Step 6: Display the original image and the pencil sketch
cv2.imshow('Original Image', image)
cv2.imshow('Pencil Sketch', pencil_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 7: Save the pencil sketch image to a file
cv2.imwrite('pencil_sketch.jpg', pencil_sketch)

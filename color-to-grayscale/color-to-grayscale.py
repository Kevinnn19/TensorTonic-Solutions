def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    greyscale = []
    for row in image :
        greyrow = []
        for pixel in row :
            r, g, b = pixel
            y = 0.299 * r + 0.587 * g + 0.114 * b
            greyrow.append(y)
        greyscale.append(greyrow)
    return greyscale
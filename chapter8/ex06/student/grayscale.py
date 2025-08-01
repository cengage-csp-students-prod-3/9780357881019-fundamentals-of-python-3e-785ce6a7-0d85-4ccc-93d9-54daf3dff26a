def grayscale_weighted(image):
    """
    Convert an image to grayscale using weighted average method.
    Weights: 0.299*R + 0.587*G + 0.114*B (standard luminance formula)
    """
    image = image.convert("RGB")
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]
            weighted_avg = int(0.299*r + 0.587*g + 0.114*b)
            pixels[x, y] = (weighted_avg, weighted_avg, weighted_avg)

    return image
if __name__ == "__main__":
    filename = input("Enter the image file name: ")
    img = Image.open(filename)

    img_avg = grayscale_average(img.copy())
    img_avg.show(title="Grayscale (Average Method)")

    img_weighted = grayscale_weighted(img.copy())
    img_weighted.show(title="Grayscale (Weighted Method)")

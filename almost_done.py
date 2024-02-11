from PIL import Image, ImageDraw, ImageFont


def text_to_image(text, font_path, max_width=600, font_size=24, text_color=(0, 0, 0), bg_color=(255, 255, 255)):
    # Create a new image with a large width to accommodate long text
    image = Image.new('RGB', (max_width, 1000), bg_color)

    # Load a font
    font = ImageFont.truetype(font_path, size=font_size)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Calculate text size
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the number of lines needed to fit the text within the max width
    lines = []
    line = ''
    for word in text.split():
        if draw.textsize(line + word, font=font)[0] <= max_width:
            line += word + ' '
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)

    # Calculate the height of the image based on the number of lines
    image_height = text_height * len(lines)

    # Resize the image to fit the text
    image = image.resize((max_width, image_height), Image.ANTIALIAS)

    # Create a new drawing context for the resized image
    draw = ImageDraw.Draw(image)

    # Draw the text on the image
    y_offset = 0
    for line in lines:
        draw.text((0, y_offset), line, fill=text_color, font=font)
        y_offset += text_height

    # Crop the image to remove excess whitespace
    image = image.crop((0, 0, max_width, image_height))

    return image


# Example usage
text = "To convert text into an image, you'll need a library that allows you to programmatically create and manipulate images. One popular library for this purpose in Python is Pillow (PIL), which is a fork of the Python Imaging Library (PIL). Pillow provides a wide range of functionality for working with images, including creating new images, drawing shapes, and adding text."
# Replace with the path to your font file
font_path = "painting-with-chocolate-font (1)\Paintingwithchocolate-K5mo.ttf"
image = text_to_image(text, font_path)
image.show()  # Display the image

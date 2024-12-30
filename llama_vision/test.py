from base64 import b64encode

image_path = "/Users/linzhanyao/Downloads/photo-1465984111739-03a1ee4647a0.jpeg"
with open(image_path, "rb") as image_file:
    print(type(image_file))
    base64_image = b64encode(image_file.read()).decode("utf-8")

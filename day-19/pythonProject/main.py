from PIL import Image, ImageEnhance, ImageFilter
import os

path = '/Users/kashyapkanumuri/Documents/GitHub/Python_Projects/day-19/pythonProject/imgs'
pathOut = '/Users/kashyapkanumuri/Documents/GitHub/Python_Projects/day-19/pythonProject/editedImgs'

for filename in os.listdir(path):
    if not filename.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        continue
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SMOOTH)
    factor = 1
    enhancer = ImageEnhance.Brightness(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')


from PIL import Image
from rembg import remove
import easygui
import glob

source = easygui.diropenbox(title="Source")
destination = "Insert File Path"
print(source)

files = glob.glob(f"{source}/*.jpg")

for file in files:
    # string that specifies the destination and changes the ouput images type name to png so that transparent shit can be sav
    output_path = f"{destination}/{file.split('/')[-1].replace('.jpg', '.png')}"

    with Image.open(file) as img:
        output_img = remove(img)
        width, height = output_img.size

    # (width/2,height/2) is the center of the image. Then we go 1000 to the left and 1000 up to set the top left point. Next we go 1000 to the right and 1000 down to set the bottom right point. These two points are diagonal on a 2000x2000 box.
        left = (width/2) - (2000/2)
        top = (height/2) - (2000/2)
        right = (width/2) + (2000/2)
        bottom = (height/2) + (2000/2)

    # Crop the image by giving the two diagonal points
        output_img = output_img.crop((left, top, right, bottom))
        # uses ouput_path string to name the cleaned img as same name as input img but change it to a png and also specify where it is to be saved. Does two things at once
        output_img.save(output_path)
    




import os
from PIL import Image


# im=Image.open('5904798606015.jpg').convert("RGB")
# im.save("test.webp", "webp", quality=50)




def Convert(file):
    im = Image.open(file).convert("RGB")
    file = file.replace(".jpg", ".webp")
    os.chdir("convert")
    im.save(file, "webp", quality=50)
    os.chdir("../")



def main():

    cwd = os.getcwd()

    formats = ('.jpg', '.jpeg')

    for file in os.listdir(cwd):

        if os.path.splitext(file)[1].lower() in formats:
            Convert(file)
            





if __name__ == "__main__":
    main()

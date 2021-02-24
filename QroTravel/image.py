from PIL import Image, ImageFilter
try:
    original = Image.open("Los_Cuervos_CUE22.jpg")
except:
    print "Unable to load image"
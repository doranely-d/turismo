import sys , os, glob
from PIL import Image
cont =0
 
### Configuracion
diri = "/srv/www/mediafiles/qrotravel/whatshot_card_photos/" # directorio donde tendremos nuestras imagenes
qualityimg = 60 #calidad de salida de las imagenes
### termina configuracion
print ("comprimiendo...")
for img in glob.glob(diri+'*.jpeg') + glob.glob(diri+'*.JPG') + glob.glob(diri+'*.jpg') + glob.glob(diri+'*.png') + glob.glob(diri+'*.gif'):

    try:
        namefile =os.path.basename(img)
        splitname =  os.path.splitext(namefile)
        namefile = splitname[0]
        extens = splitname[1]
        i = Image.open(img)
        width, height = i.size
        i = i.resize((width,height),Image.ANTIALIAS)
        i.save(diri+namefile+extens,quality=qualityimg,optimize=True)
    except ValueError:
        print (ValueError)
        cont=cont +1
if cont >0:
    print ("Algunos archivos no se puedieron comprimir")
else:
    print ("todos los ficheros fueron comprimidos con éxito")


##PIL
# from PIL import Image
# im = Image.open('whatever.png')
# width, height = im.size 
# from PIL import Image
# b = Book.objects.get(title='Into the wild')
# image = Image.open(b.cover_pic.path)
# image.save(b.image.path,quality=20,optimize=True) 
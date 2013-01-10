__author__ = 'ober'
__author__ = 'ober'

from boto.s3.connection import S3Connection
import cStringIO
import urllib
from PIL import Image
import PIL.Image
import cv2

#
##Retrieve our source image from a URL
#fp = urllib.urlopen('http://example.com/test.png')
#
##Load the URL data into an image
buff = cStringIO.StringIO()

#buff.write(data)
im = Image.open("flish.bmp")
im.save(buff,'BMP')

#
##Resize the image

#
##NOTE, we're saving the image into a cStringIO object to avoid writing to disk

##You MUST specify the file type because there is no file name to discern it from
#im2.save(out_im2, 'PNG')

#Now we connect to our s3 bucket and upload from memory
#credentials stored in environment AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
AK = 'AKIAIR4V26EWM67WYFVQ' # Access Key ID
SK = 'OmWrHotIsaWbFaExYSBf1JBaiaKVHKVY5leC3ps/' # Secret Access Key


conn =S3Connection(AK,SK)


#Connect to bucket and create key
b = conn.get_bucket('aquatest2')
k = b.new_key('example2__2.bmp')

#Note we're setting contents from the in-memory string provided by cStringIO
k.set_contents_from_string(buff.getvalue())

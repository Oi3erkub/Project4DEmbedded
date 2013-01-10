__author__ = 'ober'

import cStringIO
import urllib
from PIL import Image
import boto


#Retrieve our source image from a URL
#fp = urllib.urlopen('http://example.com/test.png')

#Load the URL data into an image
#img = cStringIO.StringIO(fp.read())
#im = open("fish.bmp")
print 'image'
#Resize the image
#im2 = im.resize((500, 100), Image.NEAREST)


#NOTE, we're saving the image into a cStringIO object to avoid writing to disk
#out_im2 = cStringIO.StringIO()
#You MUST specify the file type because there is no file name to discern it from
#im2.save(out_im2, 'PNG')

#Now we connect to our s3 bucket and upload from memory
#credentials stored in environment AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
AK = 'AKIAIR4V26EWM67WYFVQ' # Access Key ID
SK = 'xxOmWrHotIsaWbFaExYSBf1JBaiaKVHKVY5leC3ps/' # Secret Access Key


conn = boto.connect_s3(AK,SK)

#Connect to bucket and create key
b = conn.get_bucket('aquatest2')
k = b.new_key('example.png')

#Note we're setting contents from the in-memory string provided by cStringIO
#k.set_contents_from_string(out_im2.getvalue())

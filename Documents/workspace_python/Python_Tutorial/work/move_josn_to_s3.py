import boto
from boto.s3.key import Key

keyId = "AKIAJIAGTJVAJPZY4UQQ"
sKeyId= "hYfEWypNt+hy1RcM8DTD2UWZlF2mi6q38zw4TOEy"

fileName="/home/thileepan/Documents/Thileepan/test.json"
bucketName="ivy-test-new"
file = open(fileName)

conn = boto.connect_s3(keyId,sKeyId)
bucket = conn.get_bucket(bucketName)

#Get the Key object of the bucket
k = Key(bucket)

#Crete a new key with id as the name of the file
k.key=fileName

#Upload the file
result = k.set_contents_from_file(file)
#result contains the size of the file uploaded
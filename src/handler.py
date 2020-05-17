# handler.py
import os
import io
import logging
import sys
import shutil

import boto3

from PIL import Image
from PIL import ExifTags
from botocore import errorfactory

s3client = boto3.client('s3')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


PORTRAIT_MAX = dict(x=600, y=1200)
LANDSCAPE_MAX = dict(x=1200, y=600)


def extract_extension(key):
    return key.split('.').pop()


def s3upload(file, bucket, key, acl=None):
    if not acl:
        acl = 'private'
    return s3client.put_object(Body=file, Bucket=bucket, Key=key, ACL=acl)


def resize_file(name, localfile, x, y):
    image: Image = Image.open(localfile)
    w, h = image.size

    root.info(f'File: {image}')
    root.info(f'{w}, {h}')

    metadata = image.getexif()
    rotation = dict(metadata.items()).get(274, None)

    if rotation:
        image = image.resize((x, y))
        if rotation == 3:
            image = image.rotate(180, expand=True)
        if rotation == 6:
            image = image.rotate(270, expand=True)
        if rotation == 8:
            image = image.rotate(90, expand=True)
    elif h < w:
        image = image.resize((x, y))
    else:
        image = image.resize((y, x))
    image.save(f'{localfile}')


def main(event, context):
    key = event.get('key', None)
    bucket = event.get('bucket', None)
    acl = event.get('acl', None)

    if not key or not bucket:
        raise ValueError('Function requires an S3 Bucket name & Object key to operate')

    try:
        resp = s3client.get_object(Bucket=bucket, Key=key)
    except errorfactory.ClientError as error:
        raise ValueError('S3 Bucket / Key does not exist.')

    buffer = io.BytesIO()
    chunks = resp.get('Body').iter_chunks(chunk_size=1024)
    for chk in chunks:
        buffer.write(chk)

    name = key.split('/').pop()
    name = ".".join(name.split(".")[:-1])

    localfile = f'/tmp/_{name}.{extract_extension(key)}'
    copy = f'/tmp/image_{name}.{extract_extension(key)}'

    with open(localfile, 'wb') as filestream:
        filestream.write(buffer.getbuffer().tobytes())
        filestream.close()

    shutil.copyfile(localfile, copy)

    resize_file(name, localfile, 1200, 625)
    s3upload(open(localfile, 'rb'), bucket, key, acl=acl)

    if event.get('thumbnail', None):
        resize_file(name, copy, 600, 300)
        keypath = keys = key.split('/')
        keypath.insert(len(keys) - 1, 'thumbnail')
        key = '/'.join(keys)
        s3upload(open(copy, 'rb'), bucket, key, acl=acl)

    os.remove(localfile)
    return dict(
        status=200,
        message='Image resize successful'
    )


if __name__ == "__main__":
    main({}, '')

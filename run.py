from src.handler import main

data = """
'https://s3-eu-west-1.amazonaws.com/bns.assets/public/images/2020/may/IMG_20200517_194237.jpg'
'https://s3-eu-west-1.amazonaws.com/bns.assets/public/images/2020/may/everest-1150px.jpg'
"""

for item in data.split('\n'):
    if item != '':
        item = item.replace('\'', '')
        item.replace("'", '')
        item = item.replace('https://s3-eu-west-1.amazonaws.com/bns.assets/', '')
        main({'bucket': 'bns.assets', 'key': item, 'acl': 'public-read', 'thumbnail': True}, '')
        print(item)



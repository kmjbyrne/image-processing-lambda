from src.handler import main

data = """
"""

for item in data.split('\n'):
    if item != '':
        item = item.replace('\'', '')
        item.replace("'", '')
        item = item.replace('https://s3-eu-west-1.amazonaws.com/bns.assets/', '')
        main({'bucket': 'bns.assets', 'key': item, 'acl': 'public-read', 'thumbnail': True}, '')
        print(item)



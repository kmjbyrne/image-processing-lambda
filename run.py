from src.handler import main

data = """
https://s3-eu-west-1.amazonaws.com/bns.assets/public/images/IMG_20200517_194237.jpg
https://s3-eu-west-1.amazonaws.com/bns.assets/public/images/2020/april/IMG_20200517_194237.jpg
"""

for item in data.split('\n'):
    if item != '':
        item = item.replace('\'', '')
        item.replace("'", '')
        item = item.replace('https://s3-eu-west-1.amazonaws.com/bns.assets/', '')
        # event = {'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'eu-west-1', 'eventTime': '2020-07-09T22:15:33.472Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AHSNSMR94E2B8'}, 'requestParameters': {'sourceIPAddress': '84.247.48.74'}, 'responseElements': {'x-amz-request-id': 'ENAXAS4K4Y0HDN9J', 'x-amz-id-2': '6Xt41dKGjU6nFz3wR5DjJQ/eCvmuERqC1jjVtgzSGj7fP09wRHJbfKylp10Sxo1s35bF7b0S8YNaCZMkPmV5Las7Dgu1GpDH'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'ImageProcessingService-10697522e2feeb9a024a57b384e290aa', 'bucket': {'name': 'bns.assets', 'ownerIdentity': {'principalId': 'AHSNSMR94E2B8'}, 'arn': 'arn:aws:s3:::bns.assets'}, 'object': {'key': 'public/images/IMG_20200517_194237.jpg', 'size': 2746948, 'eTag': 'b7a6d22c86198f246b5b280de7fabb4c', 'sequencer': '005F0797069E56726A'}}}
        # main(event)
        main({'bucket': 'bns.assets', 'key': item, 'acl': 'public-read', 'thumbnail': True}, '')
        print(item)



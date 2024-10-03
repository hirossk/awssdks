import boto3

# リージョンを指定してs3サービスを起動する
s3 = boto3.client('s3', region_name='us-east-1')
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定
keyname = 'filename.txt'

# s3から取得する
response = s3.get_object(Bucket=bucketname, Key=keyname)
print(response['Body'].read().decode('utf-8'))
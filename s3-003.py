import boto3

# リージョンを指定してs3サービスを起動する
s3 = boto3.client('s3', region_name='us-east-1')
# 送るイメージファイルを指定
sourcefile = 'cat1.jpg'
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定
keyname = 'image.jpg'

# s3にファイルを保存する
s3.upload_file(Filename=sourcefile , Bucket=bucketname, Key=keyname)


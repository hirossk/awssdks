import boto3

# リージョンを指定してs3サービスを起動する
s3 = boto3.client('s3', region_name='us-east-1')
# 送るファイルを指定
sourcedata = 'Data Contentsだよ'
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定
keyname = 'filename.txt'

# s3に保存する
s3.put_object(Body=sourcedata , Bucket=bucketname, Key=keyname)
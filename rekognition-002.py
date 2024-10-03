import boto3
# jsonの出力を整形するためのモジュールpprint
from pprint import pprint

# リージョンを指定してRekognitionサービスを呼び出す
rekognition = boto3.client('rekognition', region_name='us-east-1')
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定
keyname = 'image.jpg'
# s3のデータ（image.jpg）を指定できるようにする
sourcedata = {'S3Object':{'Bucket': bucketname,'Name': keyname}}

# rekognitionで解析する（ラベル取得）
response = rekognition.detect_labels(Image=sourcedata)
# 出力を整形する
# pprint(response)

# for label in response['Labels']:
#   pprint(label)
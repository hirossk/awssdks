import boto3
# jsonの出力を整形するためのモジュールpprint
from pprint import pprint

# リージョンを指定してRekognitionサービスを呼び出す
rekognition = boto3.client('rekognition', region_name='us-east-1')
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定
keyname = 'photo1.jfif'
# s3のデータ画像を指定できるようにする
sourcedata = {'S3Object':{'Bucket': bucketname,'Name': keyname}}

# rekognitionで解析する（有名人検出）
response = rekognition.recognize_celebrities(Image=sourcedata)
# 出力を整形する
pprint(response['CelebrityFaces'])

# for label in response['Labels']:
#   pprint(label)
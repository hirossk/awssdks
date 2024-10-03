import boto3
# jsonの出力を整形するためのモジュールpprint
from pprint import pprint

# リージョンを指定してRekognitionサービスを呼び出す
rekognition = boto3.client('rekognition', region_name='us-east-1')
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定元となる写真の名前
source = 'ishiba.jpg'
# 検索対象の写真
target = 'photo1.jfif'
# s3のデータ画像を指定できるようにする
# 見つけたい人の写真
sourcedata = {'S3Object':{'Bucket': bucketname,'Name': source}}
# 検索する写真
targetdata = {'S3Object':{'Bucket': bucketname,'Name': target}}

# rekognitionで解析する（ラベル取得）
response = rekognition.compare_faces(SimilarityThreshold=80,
                                    SourceImage=sourcedata,
                                    TargetImage=targetdata)
# 出力を整形する
pprint(response['FaceMatches'])

# for label in response['Labels']:
#   pprint(label)
import boto3
# jsonの出力を整形するためのモジュールpprint
from pprint import pprint
# PillowモジュールのImageを使う
from PIL import Image, ImageDraw


# リージョンを指定してRekognitionサービスを呼び出す
rekognition = boto3.client('rekognition', region_name='us-east-1')
# バケット名を指定
bucketname = 'yoshida-0209'
# バケット内のオブジェクト名を指定
source = 'ishiba.jpg'
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

# S3に対する処理を記述
# 保存したいファイル名
source_file = 'groupphoto.jpg'
# リージョンを指定してs3サービスを起動する
s3 = boto3.client('s3', region_name='us-east-1')
# s3からダウンロードする
s3.download_file(Bucket=bucketname, Key=target, Filename=source_file)
# ダウンロードしたファイルを開く
img = Image.open(source_file, 'r')
# 開いたイメージの縦横の大きさを取得する
width, height = img.size
# 描画用オブジェクトの取得
draw = ImageDraw.Draw(img)
# 検出した顔のx, y座標を求める
x = response['FaceMatches'][0]['Face']['BoundingBox']['Left'] * width
y = response['FaceMatches'][0]['Face']['BoundingBox']['Top'] * height
# 検出した顔の幅と高さを求める
w = response['FaceMatches'][0]['Face']['BoundingBox']['Width'] * width
h = response['FaceMatches'][0]['Face']['BoundingBox']['Height'] * height

# 顔を囲む
draw.rectangle([x, y, x + w, h + y], outline=(0, 255, 0), width = 5)
img.show()
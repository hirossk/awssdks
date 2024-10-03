import boto3

# リージョンを指定してs3サービスを起動する
s3 = boto3.client('s3', region_name='us-east-1')

# バケット名の指定
bucketname = 'yoshida-0209'
# バケットリストの取得
response = s3.list_objects(Bucket=bucketname)
print(response)

# バケットの一覧表示
# print('-----separate-----')
# for content in response['Contents']:
    # print(content)

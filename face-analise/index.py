import boto3

s3 = boto3.resource('s3') #conecta no bucket
client = boto3.client('rekognition', 'us-east-1')

def lista_imagens():
    imagens=[]
    bucket = s3.Bucket('face-analise-image')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    print(imagens)
    return imagens

def indexa_colecao(imagens):
    for i in imagens:
        response = client.index_faces(
            CollectionId='faces',
            DetectionAttributes=[],
            ExternalImageId=i[:-4],
            Image={
                'S3Object':{
                    'Bucket': 'face-analise-image',
                    'Name':i,   
                },
            },
        )

imagens = lista_imagens()
indexa_colecao(imagens)
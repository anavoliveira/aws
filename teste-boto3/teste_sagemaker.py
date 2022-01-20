import boto3

client = boto3.client('sagemaker')
# Listar usuarios
# response = client.list_user_profiles(
#     MaxResults=10,
#     SortOrder='Ascending',
#     SortBy='CreationTime',
#     DomainIdEquals='d-tae3zoenipzd',
#     UserProfileNameContains='string'
# )
# print(response)

#Descrever usuarios
# response = client.describe_user_profile(
#     DomainId='d-tae3zoenipzd',
#     UserProfileName='user-criado-boto3'
# )



# listar tags de um recurso
response = client.list_tags(
    ResourceArn='arn:aws:sagemaker:us-east-1:023774873270:user-profile/d-tae3zoenipzd/user-teste-tag'
)

# print(response['Tags'])

# deletar usuario
# response = client.delete_user_profile(
#     DomainId='d-tae3zoenipzd',
#     UserProfileName='default-1638293370675'
# )


#Criar usuario
# response = client.create_user_profile(
#     DomainId='d-tae3zoenipzd',
#     UserProfileName='user-teste-tag',
#     Tags=[
#         {
#             'Key': 'tag-teste',
#             'Value': 'teste-user'
#         },
#     ]
# )

print(response)
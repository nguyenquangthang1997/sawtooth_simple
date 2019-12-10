import ipfsapi
import io
from rest_api.config.config import *

api = ipfsapi.connect('178.128.217.110', 5001)

async def saveToIpfs(image_request):
    #data = await request.post()
    image = image_request.file
    # password = 'password'
    dag_id = ''

    # secret_key = create_secretkey(password)

    imageConvert = image.read()

    # encrypt_information = encrypt_aes_gcm(imageConvert, secret_key)
    # encrypted_data = encrypt_information[0]
    # nonce = encrypt_information[1]
    # tag = encrypt_information[2]
    encrypted_data_path = '{}/data.txt'.format(Config.DATABASE_DIR)
    content_id_path = '{}/cid.txt'.format(Config.DATABASE_DIR)

    with open(encrypted_data_path, 'wb') as f:
        f.write((imageConvert))

    encrypt_content_id = api.add(encrypted_data_path)['Hash']

    if dag_id == '':
        dag_contentid = put_object_CID(encrypt_content_id)
    else:
        dag_contentid = append_link_object_dag(encrypt_content_id,dag_id)


    print(dag_contentid[1])


    # nonce_content_id = api.add_bytes(nonce)
    # tag_content_id = api.add_bytes(tag)

    file_cid = open(content_id_path, 'a')
    file_cid.write(encrypt_content_id + '\n')
    file_cid.close()

    # transaction_id =  push_hash_to_ethereum(encrypt_content_id)
    response_obj = {
        'contentID' : encrypt_content_id,
        'dag_id': dag_contentid[1]
        # 'txHash' : transaction_id
    }
    return response_obj
def put_object_CID(cid):
	data = '''{
		"Data": "Version hash",
		"Links": [{
			"Name": "version 1",
			"Hash": "%s"
		}]
	}'''%cid
	print (type(data.encode('utf-8')))
	dag_id = api.object_put(io.BytesIO(data.encode('utf-8')))
	return (cid, dag_id['Hash'])

def append_link_object_dag(cid, dag_id):
	count_link = len(get_object_dag(dag_id))
	name = "version "+ str(int(count_link) +1)
	infor = api.object_patch_add_link(dag_id,name,cid )
	return (cid, infor['Hash'])

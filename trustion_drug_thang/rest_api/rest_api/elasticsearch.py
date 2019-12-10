from elasticsearch import Elasticsearch
import uuid
import logging

es = Elasticsearch([{"host":"178.128.217.254", "port":"9200"}])

def create_trustion_drug_thang_user_index():
    if not es.indices.exists(index="trustion_drug_thang_user"):
        body = {
            "mappings":{
                "properties":{
                    "username":{"type":"keyword"},
                    "role":{"type":"text"},
                    "hashed_password":{"type":"text"},
                    "encrypted_private_key":{"type":"text"},
                    "public_key":{"type":"text"},
                    "transactionIdBlockchain":{"type":"text"}
                }
            }
        }
        try:
            res = es.indices.create(index='trustion_drug_thang_user', body=body)
            return res
        except Exception as e:
            print("already exist")

create_trustion_drug_thang_user_index()

async def getUserByUsername(
          username,):
    body = {
        "query": {
            "match": {
                "username": username
            }
        }
    }
    res = es.search(index='trustion_drug_thang_user', body=body)

    try:
      return res['hits']['hits'][0]['_source']
    except:
      return []

async def createUser(
          username,
          role,
          hashed_password,
          encrypted_private_key,
          public_key,
          transactionIdBlockchain):
    body={
        "transactionIdBlockchain":transactionIdBlockchain,
        "username":username,
        "role":role,
        "hashed_password":hashed_password.hex(),
        "encrypted_private_key":encrypted_private_key.hex(),
        "public_key":public_key
    }
    res = es.index(index='trustion_drug_thang_user', doc_type='_doc', body=body)
    return res


async def checkid(id):
    body = {
        "query": {
            "match": {
                "id":id
            }
        }
    }
    res = es.search(index='trustion_drug_thang_product', body=body)
    try:
        return res['hits']['hits'][0]['_source']
    except:
        return []

async def query_elasticsearch(body):
    res = es.search(index='trustion_drug_thang_product', body=body)
    try:
        return1= []
        aaa = res['hits']['hits']
        for aa in aaa:
            return1.append(aa['_source'])
        return return1
    except:
        return []
    return res


def create_trustion_drug_thang_product_index():
  if not es.indices.exists(index="trustion_drug_thang_product"):
    body={
    "mappings": {
      "properties": {
        "transactionIdBlockchain":{"type":"text"},
        "timestamp":{"type":"date","format":"epoch_second"},
          "id":{"type":"keyword"},
          "name":{"type":"text"}
        }
      }
    }
    try:
        res = es.indices.create(index='trustion_drug_thang_product', body=body)
        return res
    except Exception as e:
        print("already exist")
# Create index if not exist
create_trustion_drug_thang_product_index()

async def drug_import(
          transactionIdBlockchain,
          timestamp,
          id,
          name
):

    body = {
        "transactionIdBlockchain":transactionIdBlockchain,
        "timestamp":timestamp,
        "id":id,
        "name":name
    }

    res = es.index(index='trustion_drug_thang_product', doc_type='_doc', body=body)
    return res



async def get_drug(
          start123,
          end123,
          limit123,
          id
):
    body = {
               "query":{
                  "bool":{
                     "must":[]
                  }
               }
            }
    if limit123 >0:
        body["size"] = limit123

    body["query"]["bool"]["must"].append({    "match": {
            "id":id
}}
         )

    range_body = {"timestamp":{}}
    if start123 > 0:
        range_body["timestamp"]["gte"] = start123
    if end123 > 0:
        range_body["timestamp"]["lte"] = end123
    body["query"]["bool"]["must"].append({"range": range_body})


    res = es.search(index='trustion_drug_thang_product', body=body)
    try:
        return1= []
        aaa = res['hits']['hits']
        for aa in aaa:
            return1.append(aa['_source'])
        return return1
    except:
        return []



async def update_status(
          transactionIdBlockchain,
          timestamp,
          id,
          quantity,
          price
):
    bodyUpdate = {
                 "transactionIdBlockchain":transactionIdBlockchain,
                 "timestamp":timestamp,
                  "id":id,
                  "quantity":quantity,
                  "price":price
    }

    res = es.search(index='trustion_drug_thang_product', body={"query": {"match": {"id": id}}})
    id = res['hits']['hits'][0]['_id']
    res = es.index(index='trustion_drug_thang_product',body=bodyUpdate)
    return res


async def update_location(
          transactionIdBlockchain,
          timestamp,
          id,
          longitude,
          latitude
):
    bodyUpdate = {
                 "transactionIdBlockchain":transactionIdBlockchain,
                 "timestamp":timestamp,
                  "id":id,
                  "longitude":longitude,
                  "latitude":latitude
    }

    res = es.search(index='trustion_drug_thang_product', body={"query": {"match": {"id": id}}})
    id = res['hits']['hits'][0]['_id']
    res = es.index(index='trustion_drug_thang_product',body=bodyUpdate)
    return res

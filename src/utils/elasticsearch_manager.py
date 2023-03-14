import collections
import os
from typing import Union, List, Dict
import time

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, scan, streaming_bulk

class DocManager():

    def __init__(self):
        self.url = f"https://{os.environ.get('ELASTICSEARCH_HOST')}:{os.environ.get('ELASTICSEARCH_C_PORT')}"
        self.username = os.environ.get('ELASTIC_USERNAME')
        self.password = os.environ.get('ELASTIC_PASSWORD')
        self.client = Elasticsearch(self.url,
                                    verify_certs=False,
                                    basic_auth=(self.username, self.password), timeout=30, max_retries=10, retry_on_timeout=True)

        self.consolidated_actions = []


    def _upload_metadata(self):
        #TODO: upload S3 path of raw audio file to S3
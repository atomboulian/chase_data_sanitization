curl -XPUT http://localhost:9200/transactions -d '
{"mappings": {
  "_default_": {
    "properties": {
       "date": {"type": "date"},
       "subject": {"type": "string"},
       "value": {"type": "float"}
     }
  }
  }
}
';

curl -XPUT http://localhost:9200/_bulk --data-binary @transactions.json

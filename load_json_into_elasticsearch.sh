curl -XPUT http://localhost:9200/transactions -d '
{"mappings": {
  "_default_": {
      "_timestamp": {
        "enabled": true,
        "path": "Posting Date",
        "format": "M/dd/YYYY",
        "default": null,
        "store": true
      },
     "properties": {
        "Description": {"type": "string"},
         "Amount": {"type": "float"},
         "Balance": {"type": "float"},
         "Check or Slip #": {"type": "integer"},
         "Posting Date": {"type": "date",
                          "format": "M/dd/YYYY"}
       }
    }
    }
  }
  ';

curl -XPUT http://localhost:9200/_bulk --data-binary @jsonified/transactions.json

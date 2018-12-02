#!/bin/bash
clear
echo "Elastic Script"

curl -X DELETE -H 'Content-Type: application/json' "localhost:9200/hero"

curl -XPUT -H 'Content-Type: application/json'  "localhost:9200/hero/" -d '{
    "settings" : {
        "index" : {
            "number_of_shards" : 3,
            "number_of_replicas" : 1
        }
    }
}'

php elasticput.php

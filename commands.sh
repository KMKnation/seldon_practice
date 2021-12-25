pip install -r requirements.txt

MDOEL_NAME=CustomModel #This should be same as your model class name
SERVICE_TYPE=MODEL #This is specific seldon enum. There are others too. {MODEL,ROUTER,TRANSFORMER,COMBINER,OUTLIER_DETECTOR}
seldon-core-microservice CustomModel -service-type MODEL

curl -X POST -H 'Content-Type: application/json' -d '{ "data": { "ndarray": [[1,2,3]] }}' http://127.0.0.1:9000/predict
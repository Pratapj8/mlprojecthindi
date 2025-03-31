## End to End Data Science Project


MLFLOW_TRACKING_URI= https://dagshub.com/Pratapj8/mlprojecthindi.mlflow
MLFLOW_TRACKING_USERNAME =Pratapj8
MLFLOW_TRACKING_PASSWORD =e1788da04db40a26aad593d33aaab3110bce6b13
python script.py

import dagshub
dagshub.init(repo_owner='Pratapj8', repo_name='mlprojecthindi', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
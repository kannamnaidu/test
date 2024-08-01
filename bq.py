from google.cloud import bigquery
import sys
config_parameters = {
"QUERY_PROJECT_ID": "clarity-lm-idla-stage",
"QUERY_BRANCH_NAME":"uat",
"QUERY_TOPIC_ID":"clarity_stage_topic",
"QUERY_SUB_ID":"clarity_stage_sub",
"QUERY_BUCKET_NAME":"clarity-stage-bucket"
}
file_name = sys.argv[1]

with open(file_name, 'r') as sql:
    sql_query = sql.read()

for key,value in config_parameters.items():
    sql_query = sql_query.replace(key,value)

sql_query =  sql_query.replace("dev_connector_etl_setting","uat_connector_etl_setting")

client = bigquery.Client(project=config_parameters['QUERY_PROJECT_ID'])

try:
    query_job = client.query(sql_query)
    query_job.result()
except Exception as why:
    # print (sql_query)
    print(why)
    raise Exception(sys.exc_info())

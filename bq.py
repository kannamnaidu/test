from google.cloud import bigquery
import sys
config_parameters = {
"QUERY_PROJECT_ID": "clarity-lm-idla-dev",
"QUERY_BRANCH_NAME":"qa",
"QUERY_BUCKET_NAME":"clarity-qa-bucket"
}
file_name = sys.argv[1]

with open(file_name, 'r') as sql:
    sql_query = sql.read()

for key,value in config_parameters.items():
    sql_query = sql_query.replace(key,value)

sql_query =  sql_query.replace("dev_connector_etl_setting","qa_connector_etl_setting")

client = bigquery.Client()

try:
    query_job = client.query(sql_query)
    query_job.result()
except:
    print (sql_query)
    raise Exception(sys.exc_info())

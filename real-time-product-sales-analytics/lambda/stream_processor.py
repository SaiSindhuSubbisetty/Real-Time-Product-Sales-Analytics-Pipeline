import json
import boto3
import base64
import uuid
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'product-sales-raw-data'

def lambda_handler(event, context):
    records_data = []
    
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = {'raw': payload}
        
        records_data.append(data)

    output_filename = f"sales_records_{datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')}_{uuid.uuid4()}.json"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=output_filename,
        Body=json.dumps(records_data),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': f'Successfully processed {len(records_data)} records and stored in S3 as {output_filename}'
    }
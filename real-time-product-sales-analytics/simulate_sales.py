import boto3
import json
import time
import random
from datetime import datetime

kinesis = boto3.client('kinesis', region_name='ap-south-1')

products = ["Mobile", "Laptop", "Headphones", "Charger", "Keyboard", "Monitor"]

def generate_sale():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "product_id": random.randint(1000, 9999),
        "product_name": random.choice(products),
        "quantity": random.randint(1, 5),
        "unit_price": round(random.uniform(10, 500), 2)
    }

for _ in range(50):
    sale = generate_sale()
    print("Sending sale:", sale)

    response = kinesis.put_record(
        StreamName="product-sales-stream",
        Data=json.dumps(sale),
        PartitionKey="partitionKey"
    )

    print("PutRecord response:", response)
    time.sleep(2)
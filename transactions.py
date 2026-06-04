import pandas as pd
import random
from datetime import datetime, timedelta

branches = ["Chennai", "Mumbai", "Bangalore", "Delhi", "Hyderabad"]
statuses = ["success", "success", "success", "failed", "pending"]
account_types=["savings","current","salary","fd","rd","nri","joint","student","senior","business"]
txn_types=["debit","credit"]
countries=["India","UAE","USA"]
               
print(branches)
print(statuses)
print(account_types)
print(txn_types)
print(countries)
print(random.choice(branches))
random.uniform(100,500000)
def generate_transaction():
    return{
        "txn_id":"TXN001",
        "branch":random.choice(branches),
        "status":random.choice(statuses),
        "account_type":random.choice(account_types),
        "txn_type":random.choice(txn_types),
        "country":random.choice(countries),
        "amount":round(random.uniform(100,500000),2),
        "customer_id":f"CUST{random.randint(1,20):03d}",
        "txn_datetime" : datetime.now()+timedelta(days=random.randint(0,30))

                      }
transactions=[]
for i in range(1,101):
    txn=generate_transaction()
    transactions.append(txn)

print(generate_transaction())



print(f"Total transactions: {len(transactions)}")

df=pd.DataFrame(transactions)
df.to_csv("transactions.csv",index=False)
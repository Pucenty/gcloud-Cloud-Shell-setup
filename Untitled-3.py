#!/usr/bin/python3
import os


print(f'***Siemano z Python logon script***')

print("Exporting gcloud config default settings...\n")

GCP_CURRENT_ACCOUNT = "gclcoud.pucenty@gmail.com"
print(f"Setting GCP_CURRENT_ACCOUNT as {GCP_CURRENT_ACCOUNT}")

os.environ['GCP_CURRENT_ACCOUNT'] = GCP_CURRENT_ACCOUNT
print(os.environ.get('GCP_CURRENT_ACCOUNT'))

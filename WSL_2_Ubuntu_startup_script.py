#!/usr/bin/python3
import os


print(f'***Siemano z Python logon script***')

print("Exporting gcloud config default settings...\n")

GCP_CURRENT_ACCOUNT = "gclcoud.pucenty@gmail.com"
print(f"Setting GCP_CURRENT_ACCOUNT as {GCP_CURRENT_ACCOUNT}")
os.environ['GCP_CURRENT_ACCOUNT'] = GCP_CURRENT_ACCOUNT
os.system("gcloud config set account $GCP_CURRENT_ACCOUNT")

GCP_CURRENT_PROJECT = "my-kubernetes-project-366710"
print(f"Setting GCP_CURRENT_PROJECT as {GCP_CURRENT_PROJECT}")
os.environ['GCP_CURRENT_PROJECT'] = GCP_CURRENT_PROJECT
os.system("gcloud config set project $GCP_CURRENT_PROJECT")

user_input = input("Do you want to connect to Cloud Shell? Type 'y' and press enter to proceed.\n")
# os.system("gcloud cloud-shell ssh --authorize-session")
# print(f"User input is {user_input.lower()}")
if user_input.lower() == 'y':
    os.system("gcloud cloud-shell ssh --authorize-session")
else:
    print("\nDone running Python logon script.\n")
    exit()

#!/usr/bin/python3
import os


print(f'***Siemano z Python logon script***')

print("Exporting gcloud config default settings...\n")

GCP_CURRENT_ACCOUNT = "gclcoud.pucenty2@gmail.com"

print(f"Setting GCP_CURRENT_ACCOUNT as {GCP_CURRENT_ACCOUNT}")
os.environ['GCP_CURRENT_ACCOUNT'] = GCP_CURRENT_ACCOUNT
print(os.environ.get('GCP_CURRENT_ACCOUNT'))
os.system("gcloud config set account $GCP_CURRENT_ACCOUNT")

GCP_CURRENT_PROJECT = "my-project-66314"

print(f"Setting GCP_CURRENT_PROJECT as {GCP_CURRENT_PROJECT}")
os.environ['GCP_CURRENT_PROJECT'] = GCP_CURRENT_PROJECT
print(os.environ.get('GCP_CURRENT_PROJECT'))
command = "gcloud config set project {GCP_CURRENT_PROJECT}"
print(command)
os.system(command)


user_input = input("Do you want to connect to Cloud Shell? Type 'y' and press enter to proceed.\n")

if user_input.lower() == 'y':
    os.system("gcloud cloud-shell ssh --authorize-session")
else:
    print("\nDone running Python logon script.\n")
    exit()


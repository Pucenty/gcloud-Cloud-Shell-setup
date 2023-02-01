import os


print(f'Siemano z Python startup script')

print(f"Setting CURRENT_GCP_ACCOUNT as {GCP_CURRENT_ACCOUNT}\n")

GCP_CURRENT_ACCOUNT = "gclcoud.pucenty@gmail.com"
os.environ['GCP_CURRENT_ACCOUNT'] = GCP_CURRENT_ACCOUNT
os.system("gcloud config set account $GCP_CURRENT_ACCOUNT")

CURRENT_GCP_PROJECT = "my-kubernetes-project-366710"
os.environ['CURRENT_GCP_PROJECT'] = CURRENT_GCP_PROJECT
os.system("gcloud config set project $GCP_CURRENT_PROJECT")
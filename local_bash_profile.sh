printf "Running startup script: ${BASH_SOURCE:-$0}\n"
printf "********************************\n"
printf "Siemano `whoami` kurde\n"
printf "********************************\n"
printf "Exporting gcloud config default settings...\n"
export GCP_CURRENT_ACCOUNT=gclcoud.pucenty@gmail.com
export GCP_CURRENT_PROJECT=my-kubernetes-project-366710
printf "Setting CURRENT_GCP_ACCOUNT as $GCP_CURRENT_ACCOUNT\n"
gcloud config set account $GCP_CURRENT_ACCOUNT
printf "Setting CURRENT_GCP_PROJECT as $GCP_CURRENT_PROJECT\n"
gcloud config set project $GCP_CURRENT_PROJECT
printf "Done.\n********************************\n"
printf "\nSSH to Cloud Shell? Type 'y' for yes:\n"
read $user_input
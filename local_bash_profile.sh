********************************
Running logon script: /home/dell_user/.bash_profile
********************************
Siemano dell_user
********************************
Running Python logon script...
***Siemano z Python startup script***
Exporting gcloud config default settings...

Setting GCP_CURRENT_ACCOUNT as gclcoud.pucenty@gmail.com
Updated property [core/account].
Setting GCP_CURRENT_PROJECT as my-kubernetes-project-366710
Updated property [core/project].

Done running logon script.
********************************
dell_user@dell:~$ cat .bash_profile
printf "********************************\n"
printf "Running logon script: ${BASH_SOURCE:-$0}\n"
printf "********************************\n"
printf "Siemano `whoami`\n"
printf "********************************\n"
printf "Running Python logon script...\n"
./python_logon_script.py
printf "\nDone running logon script.\n********************************\n"
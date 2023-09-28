#! /bin/bash
sudo apt-get update
sudo apt-get install apache2 -y
sudo service apache2 restart
echo '<!doctypehtml><html><body><h1>acloud1</h1></body></html>' | tee /var/www/html/index.html
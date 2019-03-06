#!/bash/bin

git pull origin master
ip a > ip_address.txt
git add ip_address.txt
git commit "Connectors"
git push origin master

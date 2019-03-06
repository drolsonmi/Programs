#!/bash/bin

# To automate this, run the following commands
# on the Raspberry Pi:
#
# git config credential.helper store
# git push origin master
#
# Enter credentials, then you won't need to for
# the next login

git pull origin master
ip a > ip_address.txt
git add ip_address.txt
git commit "Connectors"
git push origin master

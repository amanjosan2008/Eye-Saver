# This script will install a Crontab entry 
# to run script every 20 minutes
# Also it will copy the script to home directory


mkdir ~/scripts && mv eye-saver.py ~/scripts
echo "*/20 * * * * /usr/bin/python3 ~/scripts/eye-saver.py" | sudo tee --append /etc/cron.d/eyesaver > /dev/null
crontab /etc/cron.d/eyesaver 




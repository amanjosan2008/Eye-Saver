# This script will install a Crontab entry 
# to run script every 20 minutes
# Also it will copy the script to home directory


mv eye-saver.py ~
echo "*/20 * * * * /usr/bin/python ~/eyesaver.sh" | sudo tee --append /etc/cron.d/eyesaver > /dev/null
crontab /etc/cron.d/eyesaver 




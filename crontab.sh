# This script will install a Crontab entry to 
# execute eyesaver warning every 20 minutes

echo "*/20 * * * * /usr/bin/python ~/eyesaver.sh" | sudo tee --append /etc/cron.d/eyesaver > /dev/null
mv eye-saver.py ~



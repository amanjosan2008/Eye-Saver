# This script will install a Crontab entry to 
# execute eyesaver warning every 20 minutes

echo "*/05 * * * * aman bash /opt/eyesaver.sh" > /etc/cron.d/eye-saver



from informer import TGInformer
import sys
# ===========
# Quick setup
# ===========

#virtualenv venv
#source venv/bin/activate
#pip install -r requirements.txt

# Read more: https://github.com/paulpierre/informer/

try:
    account_id = sys.argv[1]
except:
    sys.exit('informer.py <account_id> - account_id is a required param')

if not account_id:
    sys.exit('Account ID required')

if __name__ == '__main__':

    informer = TGInformer(
        account_id=account_id,
        db_prod_ip='192.168.2.177',
        db_prod_port=3306,
        db_prod_name='informer_db',
        db_prod_user='root',
        db_prod_password='123456',
        db_local_ip='127.0.0.1',
        db_local_port='3320',
        db_local_name='informer_db',
        db_local_user='root',
        db_local_password='123456',
        tg_notifications_channel_id=823447412,  # Insert your own channel ID here
        google_credentials_path='credentials/gcloud_api.json',  # You will need download your Google API file here
        google_sheet_name='Informer Notifications'
    )
    informer.init()
    sys.exit(0)

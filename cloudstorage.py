from unicodedata import name
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file (self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BJRMO-PqiGuNQ8OIQ7QPR4u_n9y_TqpjFaHmTz2N7owOL2XWrdmSf-v5QiBS74LFRMlU9EQJs1Kj8Zv_b1gRQlIakqusI9wCZk8t0SfAAlssIo-D0EKnREQxl-ywd_APIUIzIR4"
    transferData = TransferData(access_token)

    file_from = 'age.py'
    file_to = '/test_dropbox/age.py'
    
    transferData.upload_file(file_from, file_to)

main()



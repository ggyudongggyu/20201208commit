from smtplib import SMTP
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os


class MailSender():
    
    def __init__(self, email_address, email_password):
        #メールアドレスとパスワードを使って、ログインをする。
        self.email_address = email_address
        self.email_password = email_password
        self._smtp_login()
        
    #public
    def send(self, to_address, file_path):
        
        #file_pathはフルパス
        #to_addressは送信先メールアドレス
        
        sub = 'Weekly Gift from team member' #メール件名
        body = 'A csv file attached.'  # メール本文
        host, port = 'smtp.gmail.com', 587

        # メールヘッダー
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = self.email_address
        msg['To'] = to_address

        # メール本文
        body = MIMEText(body)
        msg.attach(body)

        # 添付ファイルの設定
        # nameは添付ファイル名。pathは添付ファイルの位置を指定
        attach_file = {'name': os.path.basename(file_path), 'path': file_path}
        
        # テキストファイルの場合
        # attachment = MIMEBase('text', 'plain') 
        # エクセルファイルの場合
        # attachment = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        
        #jsonファイルの場合
        # attachment = MIMEBase('application', 'json')
        
        #csvファイルの場合
        attachment = MIMEBase('text', 'csv')       
        
        file = open(attach_file['path'], 'rb+')
        attachment.set_payload(file.read())
        file.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
        msg.attach(attachment)
        
        #メッセージを送信
        self.gmail.send_message(msg)
        

    #private
    def _smtp_login(self):
        # gmailへ接続(SMTPサーバーとして使用)
        self.gmail=SMTP("smtp.gmail.com", 587)
        self.gmail.starttls() # SMTP通信のコマンドを暗号化し、サーバーアクセスの認証を通す
        self.gmail.login(self.email_address, self.email_password)
        













# gmailを使ったメール送信のサンプルプログラム
def sendGmailAttach():
    sender, password = 'greed.gggg@gmail.com', 'abcd@1234' # 送信元メールアドレスとgmailへのログイン情報 
    to = 'greed.gggg@gmail.com'  # 送信先メールアドレス
    sub = 'Weekly Gift from *****' #メール件名
    body = 'An excel file attached.'  # メール本文
    host, port = 'smtp.gmail.com', 587

    # メールヘッダー
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = to

    # メール本文
    body = MIMEText(body)
    msg.attach(body)

    # 添付ファイルの設定
    attach_file = {'name': 'aaa.xlsx', 'path': './aaa.xlsx'} # nameは添付ファイル名。pathは添付ファイルの位置を指定
    # attachment = MIMEBase('text', 'plain')
    attachment = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    file = open(attach_file['path'], 'rb+')
    attachment.set_payload(file.read())
    file.close()
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=attach_file['name'])
    msg.attach(attachment)

    # gmailへ接続(SMTPサーバーとして使用)
    gmail=SMTP("smtp.gmail.com", 587)
    gmail.starttls() # SMTP通信のコマンドを暗号化し、サーバーアクセスの認証を通す
    gmail.login(sender, password)
    gmail.send_message(msg)

if __name__ == '__main__':
    sendGmailAttach()
    print('メールが送信されました')

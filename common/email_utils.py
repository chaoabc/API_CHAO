import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.localconfig_utils import local_config


class  EmailUtils():
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = local_config.SMTP_SERVER
        self.smtp_sender = local_config.SMTP_SENDER
        self.smtp_password = local_config.SMTP_PASSWORD
        self.smtp_receiver = local_config.SMTP_RECEIVER
        self.smtp_cc = local_config.SMTP_CC
        self.smtp_subject = local_config.SMTP_SUBJECT
        self.smtp_body = smtp_body
        self.smtp_attch = smtp_attch_path


    def email_message_body(self):
        msg=MIMEMultipart()
        msg.attach(MIMEText(open(self.smtp_body,'html','utf-8')))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject

    def send_email(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_password)
        smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',')+self.smtp_cc.split(','), self.email_message_body().as_string())


if  __name__=="__main__":
    reports_path =os.path.dirname(__file__)+"../test_reports/0722"
    EmailUtils('<h3 align="center">自动化测试报告</h3>').send_email()


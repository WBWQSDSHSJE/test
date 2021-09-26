import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

mail_host = 'smtp.qq.com'

mail_user = '1347394976@qq.com'

mail_pass = 'klrbgzrxxdhghfhf'

mail_from = 'rainbird'

mail_to='13552648187@163.com'

mail_title= "rainbird's mac book"

me = mail_from +"<"+mail_user+">"

def file_get_content(file_name):

    with open ('计算器报告.html','r',encoding='utf-8') as f:

     return f.read()

mail_body = '/result_report.html'

mail_att= '/result.html'

msg = MIMEMultipart()

msg['Subject']= mail_title

msg['From']= me

msg['To']= mail_to

msg.attach(MIMEText(file_get_content(mail_body),_subtype='html',_charset='utf8'))

# 邮件附件

att = MIMEText(file_get_content(mail_att), 'base64', 'utf-8')

att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', 'report.html'))

msg.attach(att)

try:

    s= smtplib.SMTP_SSL(host=mail_host,port=465)

    s.connect(mail_host)

    s.login(mail_user,mail_pass)

    s.sendmail(me, mail_to, msg.as_string())

    s.close()

    print('send mail success!')

except Exception as e:

    print(e)


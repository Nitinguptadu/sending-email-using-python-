import smtplib



email_user = 'nitingupta.du2@gmail.com'
email_password = '##########'
email_send = 'laltu.ajay1994@gmail.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

message = "hello world"

server.sendmail(email_user,email_send,message)
server.quit()
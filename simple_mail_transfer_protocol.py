import smtplib

my_email = "test_example@gmail.com"
password = "abcd1234567"
connection = smtplib.SMTP("smtp.gmail.com")
#TLS transport layer security

connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="recipient_email@gmail.com",
                    msg="Subject:Hello\n\nThis is the body of the email")
connection.close()


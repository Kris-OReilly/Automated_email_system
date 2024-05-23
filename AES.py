import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

my_email = input("Enter email address:")
password_key = input("Enter password:")

# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587

# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
    
# Login with your email and password
my_server.login(my_email, password_key)



text_content = """
Hi {Name},
As you may know our restaurant has been purchased by ***.
Please attend our information session on Monday 22nd June 2024.

Thanks,
Kris"""


with open("Family.csv") as csv_file:
    family = csv.reader(csv_file)
    next(family)

    for Name, Email in family:

        message = MIMEMultipart("alternative")
        message["From"] = my_email
        message["To"] = Email
        message["Subject"] = "Information Session"

        email_text = text_content.format(Name=Name)

        message.attach(MIMEText(email_text))

        my_server.sendmail(
            from_addr= my_email,
            to_addrs= Email,
            msg=message.as_string()
        )
        print("Email sent successfully!")
        

my_server.quit()


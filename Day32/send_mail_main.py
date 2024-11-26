import smtplib
import json

with open('config.json', 'r') as config_file: # use with to automatically close the file
    config = json.load(config_file)

my_email = config['email']
my_password = config['password']
receive_email = config['receive_email']

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls() # make it encripted
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receive_email,
        msg="Subject:Hello\n\nThis is the body of my email."
    )
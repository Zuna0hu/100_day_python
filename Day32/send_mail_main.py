import smtplib

my_email = "your_email@gmail.com" # i will use a .env file
password = "yourpassworld"

with smtplib.SMTP("smtp.mail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="your_another_email.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
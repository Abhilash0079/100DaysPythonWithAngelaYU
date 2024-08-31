import smtplib

my_email = "singh.aman130791@gmail.com"
password = "vpqf fumo onac rkrz"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # make the connection secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="singh.aman130791@yahoo.com",
                        msg="Subject:Hello\n\nHi Aman, \nGreetings from Aman.\nRegards,\nAman Singh")

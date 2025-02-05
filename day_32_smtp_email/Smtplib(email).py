import smtplib
# allways allow less secure apps in security settings
my_email = "tshifhiwachedzafordjr@gmail.com"
# go to google account settings, in the settings search "App Password", use the password they give you.
password = "qjba mlqf pfrc ghox"
# if you need to use a different provider search the provider and the smtp info for it
with smtplib.SMTP("smtp.gmail.com", port=587) as connection: #this will close the connection automatically
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="chiedzafordjr@gmail.com",
                        msg="Subject:yo it worked\n\n"
                            "It worked broskie")



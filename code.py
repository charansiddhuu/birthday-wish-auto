from datetime import datetime
import pandas
import smtplib

MY_EMAIL_SMTP_SERVER = "smtp.gmail.com"
MY_EMAIL = "prabhas.tunga@sasi.ac.in"
MY_PASSWORD = "prabhas2k3"
MY_NAME = "ram"

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv(r"C:\Users\Bharath Chandra\OneDrive\credit card processing\Desktop\birth day.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    # Directly include the template content
    template_content = """
    Dear [NAME],

    Wishing you a fantastic birthday! 🎉

    Best regards,
    [MY_NAME]
    """

    try:
        contents = template_content.replace("[NAME]", birthday_person["name"])
        contents = contents.replace("[MY_NAME]", MY_NAME)
    except KeyError:
        print("Error: Missing required data for birthday person.")
    else:
        try:
            with smtplib.SMTP(MY_EMAIL_SMTP_SERVER) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{contents}"
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

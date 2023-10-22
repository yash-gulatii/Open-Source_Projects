import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(subject, body, image_path, recipient_list):
    # Gmail SMTP configuration
    smtp_server = "your email smtp "
    smtp_port = 587
    sender_email = "email id "
    sender_password = "app password if you are using gmail  /password "
    #recipent email to open 
    with open(recipient_list, 'r') as file:
        recipient_list = [line.strip() for line in file]

          # Read email body from the text file
    with open(body, 'r') as file:
        email_body = file.read()

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

  # Attach the image
    with open(image_path, 'rb') as img_file:
        image = MIMEImage(img_file.read(), name=image_path.split("\\")[-1])
        msg.attach(image)

   

    # Connect to the Gmail SMTP server and send the email
    try:
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(sender_email, sender_password)
        for recipient in recipient_list:
            msg['To'] = recipient
            smtp_connection.sendmail(sender_email, recipient, msg.as_string())
        smtp_connection.quit()
        print("Emails sent successfully!")
    except Exception as e:
        print("Error sending emails:", str(e))

if __name__ == "__main__":
    recipients ="recipient_list.txt"
    email_subject = "Your Subject"
    email_body = "body.txt"
    image_path = r"image file path "

    send_email(email_subject, email_body, image_path, recipients)

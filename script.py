import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


"""
in order for this to work with gmail 2 factor authentication must be enabled
and an app password must be generated

generate app password:
https://support.google.com/accounts/answer/185833?hl=en

"""

# set smpt server and port
email_smtp_server = 'smtp.gmail.com'  # can be replaced with desired smtp server
secure_port = 465  # using SSL port


# Create a secure SSL context
context = ssl.create_default_context()


def email_process(email, password, send_to_email):
    with smtplib.SMTP_SSL(email_smtp_server, secure_port, context=context) as server:
        try:
            server.login(email, password)
        except Exception as e:
            print('Unable To Log In', e)
            return e

        print('Log in to gmail')
        # construct email message NOTE: Can also be create into a map function to send out an email an email list
        email_data = email_constructor('Hello this is a text email', 'Test', 'Braulio G', send_to_email)

        # send email
        server.sendmail(email, send_to_email, email_data)
        print("Email Sent")


def email_constructor(msg, msg_subject, send_from, send_to):
    """

    :param msg: email body
    :param msg_subject: email subject
    :param send_from: sender info
    :param send_to: corresponding email
    :return: properly formatted email
    """
    # set msg values
    email_msg = MIMEMultipart()
    email_msg['FROM'] = send_from
    email_msg['TO'] = send_to
    email_msg['SUBJECT'] = msg_subject
    msg_body = MIMEText(msg, 'plain')
    email_msg.attach(msg_body)
    # convert entire msg to send string
    msg_str = email_msg.as_string()
    return msg_str


if __name__ == "__main__":

    # login to email account
    g_email = input('Enter gmail account that will send email: ')
    passwd = input('Enter password: ')
    to_email = input('Enter corresponding email: ')

    # send email
    email_process(g_email, passwd, to_email)

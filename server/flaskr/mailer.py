from sendgrid.helpers.mail import Mail, HtmlContent
from sendgrid import SendGridAPIClient

# Do not need a secure connection
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# SENDGRID API KEY
# Add to variables later

html_text = """
<html>
    <body>
        <h1>Username: Rahul</h4>
        <h1>Password: Rahul</h4>
    </body>
</html>
"""

message = Mail(
    from_email='ra00010@mix.wvu.edu',
    to_emails='ra00010@mix.wvu.edu',
    subject='Account successfully created !!!',
    html_content=HtmlContent(html_text)
)
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)

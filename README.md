# Django SMS Project Using Twilio

This project demonstrates how to send SMS messages from a Django application using the Twilio API.

## Requirements

- Python 3.8 and later
- Django
- Twilio

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS
   venv\Scripts\activate  # On Windows 
   ```

3. **Install required packages:**
   ```bash
   pip install django twilio
   ```

## Configuration

Before running the project, you need to configure your Twilio credentials.

1. **Edit `send_sms.py`:**  
   Open the `send_sms.py` file from the `sms_app` directory and update the following placeholders:

   ```python
   from twilio.rest import Client

   def send_sms(body, to):
       account_sid = ""  # Your Twilio account SID
       auth_token = ""   # Your Twilio authentication token
       client = Client(account_sid, auth_token)

       message = client.messages.create(
           body=body,
           from_="",  # Your Twilio phone number (the number assigned to your account)
           to=to,
       )

       print(message.body)
   ```

   - Replace `""` for `account_sid` and `auth_token` with your actual Twilio Account SID and Authentication Token.
   - Replace `""` for `from_` with your Twilio phone number.

## Running the Project

Make sure your Django server is running, and you can send SMS messages using the Twilio service.

```bash
python manage.py runserver
```

## Notes

- Ensure your Twilio account has sufficient balance for sending SMS.
- If you're using a trial account, the recipient's number must be verified in your Twilio account.

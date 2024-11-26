# Day 32 Send Email (smtplib) and Manage Dates (datetime)

## Sending Emails Using Python and `smtplib`

This guide summarizes the process of sending emails programmatically using Python's `smtplib` module.

---

### How Email Works
1. **Behind the Scenes**:
   - Sender's email (e.g., `angela@gmail.com`) communicates with the sender's mail server (e.g., Gmail Mail Server).
   - The recipient's mail server (e.g., Yahoo Mail Server) stores the email until the recipient retrieves it.
   - **SMTP (Simple Mail Transfer Protocol)** facilitates the movement of emails between mail servers and ensures delivery.

2. **Analogy**:
   - Mail servers = Post offices.
   - SMTP = Postman.

---

### Setting Up Email Sending with Python
1. **Requirements**:
   - Two test email accounts (e.g., one Gmail, one Yahoo) to avoid security risks with your primary accounts.
   - Adjust security settings to allow sending emails using Python.

2. **Python Module**:
   - Use the `smtplib` library for SMTP-based email communication.

---

### Implementation Steps
1. **Set Up an SMTP Connection**:
   - Identify the SMTP server for your email provider:
     - Gmail: `smtp.gmail.com`
     - Yahoo: `smtp.mail.yahoo.com`
     - Hotmail: `smtp.live.com`
   - Example:
     ```python
     connection = smtplib.SMTP("smtp.gmail.com")
     ```

2. **Secure the Connection**:
   - Use `starttls()` to enable **Transport Layer Security (TLS)** for encrypting the connection.
   - Example:
     ```python
     connection.starttls()
     ```

3. **Log In**:
   - Use `connection.login(username, password)` with your email and password.
   - Example:
     ```python
     connection.login("your_email@gmail.com", "your_password")
     ```

4. **Send the Email**:
   - Use `connection.sendmail(from_addr, to_addr, message)` to send the email.
   - Message format:
     - Subject: Add a `Subject:` field.
     - Body: Separate with `\n\n`.
   - Example:
     ```python
     message = "Subject: Hello\n\nThis is the body of the email."
     connection.sendmail("your_email@gmail.com", "recipient_email@yahoo.com", message)
     ```

5. **Close the Connection**:
   - Use `connection.quit()` or the `with` keyword to automatically manage the connection.

---

### Using the `with` Keyword for Better Code
- Simplifies connection handling by automatically closing it after the block:
```python
  with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login("your_email@gmail.com", "your_password")
      connection.sendmail("your_email@gmail.com", "recipient_email@yahoo.com", "Subject: Test\n\nHello!")
```
## Use Configuration Files
Sometimes like in this repo, we need to input our email and password to automate the process of code. It is not recommended to explicitly include your email and password in the code file, but you can use a configuration file and exclude the file from Git so that only you can have access to it.
---
### Implementation Steps
1. **Create a `config.json` File**:
```json
{
    "email": "your_email",
    "password": "your_password"
}
```
2. **Add `config.json` to `.gitignore`**:
```bash
config.json
```
3. **Read it in Python**:
```python
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

email = config['email']
password = config['password']
```
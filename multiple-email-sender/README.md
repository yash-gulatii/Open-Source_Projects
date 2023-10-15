## Welcome to Multiple Email Sender!

This script empowers you to effortlessly send emails to multiple recipients with the same subject, body, and other additional features. It's designed to save you time and streamline your email communication process. Whether you need to share code snippets, important announcements, or even images, this script has got you covered.

### Prerequisites

Before you get started, make sure you have the required module installed. You can install it using the following command:

```bash
pip install secure-smtplib
```

### Getting Started

1. **Prepare your content:**

   Create two text files in the same directory as the script:

   - `body.txt`: This file should contain the body of your email. Write your message here.
   - `recipients.txt`: List all the recipient email addresses, one per line. You can add as many as you need.

2. **Customize the script:**

   Open the script in your favorite code editor and make the following adjustments:

   - Set your email address and password.
   - Modify the subject line if needed.
   - If you want to include an image or other attachments, provide the correct file path.

3. **Running the script:**

   Open a terminal or command prompt and navigate to the directory containing your script.

   Run the script using:

   ```bash
   python your_script_name.py
   ```

   The script will read the content from `body.txt`, fetch recipient addresses from `recipients.txt`, and send the emails.

### Features

- **Effortless customization:** Easily tailor the subject, body, and attachments according to your needs.
- **Bulk email sending:** Reach out to multiple recipients simultaneously.
- **Attachment support:** Send images or other files along with your email.
- **Secure and reliable:** The script uses secure SMTP to ensure the confidentiality of your data.

### Example Use Cases

- Sharing code snippets with your team.
- Notifying clients about updates or changes.
- Sending invitations or event announcements.
  

### Note

Always ensure you have the necessary permissions to send emails from your email account programmatically. Some email providers might require you to enable "Less Secure Apps" or generate an "App Password" for this purpose.
Change the file name to any other name if you encounter email module not found error.

Feel free to explore and modify the script to suit your specific requirements. Happy emailing! 🚀

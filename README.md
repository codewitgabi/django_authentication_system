## Project Description

An authentication system with django. Improved security, email login(verification will be added in the future).
A referral system just for the purpose of using signals.

## Generating Gmail App Password
Google by default, doesn't allow third party packages to have access to your gmail account. Sending email with django or python is obviously a third party thing so a few configurations have to be made to the gmail account to be used.

* visit [!https://myaccount.google.com/lesssecureapps](Allow less secure apps)
Follow the instructions on the page and after you are done go to step 2
* visit [!https://accounts.google.com/b/0/displayunlockcaptcha](Display unlock captcha)
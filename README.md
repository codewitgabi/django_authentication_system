# Description

An authentication system with django. Improved security, email login(verification will be added in the future).
A referral system just for the purpose of using signals.

## Quickstart

To use this project, kindly run the following commands

```
$ pip install -r requirements.txt
```
Once the packages are installed you can then run

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Once you are done, go to your browser and visit this [url](http://localhost:8000/)

## Generating Gmail App Password
Google by default, doesn't allow third party packages to have access to your gmail account. Sending email with django or python is obviously a third party thing so a few configurations have to be made to the gmail account to be used.

* visit [Allow less secure apps](https://myaccount.google.com/lesssecureapps)
Follow the instructions on the page and after you are done go to step 2
* visit [Display unlock captcha](https://accounts.google.com/b/0/displayunlockcaptcha)

### Package Documentation
[Django-Email-Verification](https://pypi.org/project/Django-Verify-Email/)
[Social Login](https://python-social-auth.readthedocs.io/en/latest/configuration/django.html)
* [Facebook Backend](https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html#oauth2)
* [GitHub Backend](https://python-social-auth.readthedocs.io/en/latest/backends/github.html)

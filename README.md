# flask-blog-website
Blogging website created using python flask with login-register functionality. User can create post, delete post, update his own post and view others post. If you forget your password you can use the reset password link which will send you a link to your registered mail to reset the password.

## Set up instructions
Clone the repository using the below command.
```
git clone https://github.com/ugoswami11/flask-blog-website.git
```
Open terminal and navigate inside the flask-blog-website firectory then install the dependencies using pipenv
```
pipenv install
```
To get the app running first activate the virtual environment using below command
```
pipenv shell
```
Execute the run.py file
```
python run.py
```

# Environment variables setup
This is a pre-requisite to run the application. we have to set up few environment variables. To set up environment variable in virtual env the easiest step is to create a ```.env``` file where the pipfile and pipfile.lock are present. Include the below variables in the ```.env``` files.
```
MAIL_USER = ''
MAIL_PASS = ''
SECRET_KEY = 'mysecretkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
```
The ```SQLALCHEMY_DATABASE_URI``` should be as mentioned above, this will connect to the sqlite db.

The ```SECRET_KEY``` should be set to a unique key and can be anything.

The ```MAIL_USER``` and ```MAIL_PASS``` variables are used for the reset email functionality. Here we can provide our mail id and password. We have to also setup ```the MAIL_SERVER``` and ```MAIL_PORT``` in the ```config.py``` file inside the blog directory. It depends on the email provider we are using. I have used zohomail in this case.

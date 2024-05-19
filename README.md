# django-image-upload-app
A simple app to upload images on AWS S3 built with django. Below Process describes how to run this project on an AWS EC2 server. OS used for EC2 server is Ubuntu.

### Setup
Update the System
```bash
sudo apt-get update
```
To get this repository, run the following command inside your git enabled terminal
```bash
git clone ([https://raw.githubusercontent.com/shreys7/django-todo/develop/staticfiles/todoApp.png](https://github.com/crazylot/upload-images-on-s3.git))

You will need django to be installed in you computer to run this app. Head over to https://www.djangoproject.com/download/ for the download guide

Download django usig pip
```bash
sudo apt install python3-pip -y
```
```bash
pip install django
```
Once you have downloaded django, go to the cloned repo directory and run the following command

```bash
python3 manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python3 manage.py migrate
```

One last step and then our todo App will be live. We need to create an admin user to run this App. On the terminal, type the following command and provide username, password and email for the admin user
```bash
python3 manage.py createsuperuser
```

That was pretty simple, right? Now let's make the App live. We just need to start the server now and then we can start using our App. Start the server by following command

```bash
python3 manage.py runserver 0.0.0.0:8000
```

Once the server is hosted, click on the public url of your EC2 machine. You also need to create a security group for your EC2 machine to allow traffic on port 8000 of your EC2 machine.

Cheers and Happy Coding :)

# Micro Blog App

**Features**

* Register / Login user
* Create / Update / Delete post
* Create / Update user profile
* Browse other users' posts

## Example usage

### Classic way

```
git clone https://github.com/akubala/micro-blog.git
cd micro-blog/microblog
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.cfg
python manage.py runserver
```

### Docker way

```
git clone https://github.com/akubala/micro-blog.git
cd micro-blog/microblog
docker-compose up --build
```

**By default, application is available on `localhost:8000` address**

### Available users

* Admin user
  - Username: *akubala*
  - Password: *student*

* Test user
  - Username: *testuser*
  - Password: *testpassword*

### Run basic tests

```
python manage.py test --failfast
```

### About

* Placeholders generated with [hipsum.co](https://hipsum.co/)
* Favicon / Logo made by [Kiranshastry](https://www.flaticon.com/authors/kiranshastry) from
 [Flaticon](https://www.flaticon.com/)
* Inspired by [Corey Schafer](https://github.com/CoreyMSchafer)

### Note

This project is no longer maintained.

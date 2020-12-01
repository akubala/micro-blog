# Micro Blog App

**Features**

* Register / Login user
* Create / Update / Delete post
* Create / Update user profile
* Browse other users' posts

## Example usage

*For presentation purposes the database is not separated and dummy data is already present.*

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
cd micro-blog/microblog
docker build -t micro-blog:1.0.0 .
docker run --rm -p 8000:8000 micro-blog:1.0.0
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

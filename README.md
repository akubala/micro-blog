# Micro Blog App

**Features**

* Register / Login user
* Create / Update / Delete post
* Create / Update user profile
* Browse other users' posts

## Example usage

### Classic way

```
cd ~
git clone https://github.com/akubala/micro-blog.git
cd micro-blog
virtualenv venv -p python3
source ./venv/bin/activate
cd microblog
pip install -r requirements.txt
python manage.py runserver
```

### Docker way

```
cd ~
git clone https://github.com/akubala/micro-blog.git
cd micro-blog/microblog
docker-compose up --build
```

**By default, application is available on  `localhost:8000`**

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

### Note

* Placeholders generated with [hipsum.co](https://hipsum.co/)
* Favicon / Logo made by [Kiranshastry](https://www.flaticon.com/authors/kiranshastry) from
 [Flaticon](https://www.flaticon.com/)
 * Inspired by [Corey Schafer](https://github.com/CoreyMSchafer)

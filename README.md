# django_allauth
using `django-allouth` library for login to django account with social media
<hr>

## for running the project
1. install libraries on `requirements.txt` with this command:
    ```
   pip install -r requirements.txt
   ```
2. create super user with this command:
    ```
   python manage.py createsuperuser
   ```
3. go to admin panel/social applications and create new social app:
    [http://127.0.0.1:8000/admin/socialaccount/socialapp/](http://127.0.0.1:8000/admin/socialaccount/socialapp/)
    
    tipe: get `Client id` and `Secret key` from your github account from this address:
       [https://github.com/settings/developers](https://github.com/settings/developers)
   
    tipe: get `Client id` and `Secret key` from your google account from this address:
       [https://console.cloud.google.com/apis/](https://console.cloud.google.com/apis/)

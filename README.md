# Ex02 Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a student database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![ar](https://user-images.githubusercontent.com/120380280/232228484-a3bf5ed2-6691-4423-b4f8-46e712f029d1.png)


## DESIGN STEPS

### STEP 1:
Clone the repository from github.

### STEP 2:
Create an admin interfacefor Django.

### STEP 3:
Create an app and edit settings.py.

### STEP 4:
Makemigrations and migrate the changes.

### STEP 5:
Create admin user and write pythoncode for admin and models.

### STEP 6:
Make all the  migrations to 'myapp'.

### STEP 7:
Create an student database with 10 feilds using runserver command.


## PROGRAM

```python
admin.py 

from django.contrib import admin
from .models import student,studentAdmin 
admin.site.register(student,studentAdmin)

models.py

from django.db import models
from django.contrib import admin
class student (models.Model):
    sid=models.CharField(max_length=28)
    name=models.CharField(max_length=30)
    regno=models.IntegerField()
    marks=models.IntegerField()
    email=models.EmailField()

class studentAdmin(admin.ModelAdmin):
    list_display=('sid','name','regno','marks','email')


```

## OUTPUT

![ink](https://user-images.githubusercontent.com/120380280/232228509-9d7ad447-5273-4daa-ad2a-f79fbe38ea8d.png)


## RESULT
The program for coressponding on student database using ORM is executed sucessfully.

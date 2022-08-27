## Features of this Project

### A. Admin Users Can
1. Manage all Entities from the admin site

### C. Students Can
1. Register an account.
2. Apply for a Course

### B. Secretary Can
1.See Applies from all Students.
2.Aprove Applies.
3.NOT register (needs admin to create the account)


## How to Install and Run this project Manualy?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

```
$  python3 -m venv venv
```

Activate Virtual Environment

```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/vijaythapa333/django-student-management-system.git
```

Then, Enter the project
```
$  cd django-student-management-system
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```


**7. Login Credentials**

Create Super User (HOD)
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**8. Add initial data**
Command for PC:
```
$  python manage.py loaddata initial_data.json
```

**or Use Default Credentials**

*For HOD /SuperAdmin*
Email: admin@gmail.com
Password: admin

*For Staff*
Email: staff@gmail.com
Password: staff

*For Student*
Email: student@gmail.com
Password: student

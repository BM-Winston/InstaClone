## InstaClone

### 7/06/2022

## Author

[Winston Musasia]

# Description

This is a clone of the website of the popular photo app Instagram.


## Live link


## User Story
The user should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.
## Setup and Installation

##### Clone the repository
```bash
git@github.com/BM-Winston/InstaClone.git
```
##### Install requirements 
```bash
cd Insta-Clone pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv virtual - source virtual/bin/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Tests 
 ```bash 
 python manage.py test 
```

Open application at '127.0.0.1.8000' at your web browser



## Technologies Used

* Python
* Django
* Heroku
* HTML
* CSS

# Known Bugs


## License


Authors Information

[musasiawinston@gmail.com]

Winston Musasia (c) 2022


[Go Back to the top](#InstaClone)



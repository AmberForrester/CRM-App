<a id="readme-top"></a>

<h1 align='center'>Django | CRM Application :briefcase:</h1>

<div align='center'>

This project is a **Customer Relationship Management (CRM)** application built with Django and MySQL. It allows users to create, update, and manage customer records.

<br />

<a href='https://github.com/AmberForrester/CRM-App'><strong>Source Code »</strong></a>
<br />
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    
  </ol>
</details>
<br />



## Features
- User authentication (login, logout, registration)
- Create, update, and delete customer records
- Secure access to customer records with login requirements

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Installation

### Prerequisites
- Python 3.x
- Django 4.x (or latest)
- Virtual Environment (optional but recommended)
- MySQL Download



### Project Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/dcrm.git
   cd dcrm
   ```

2. **Set up a Virtual Environment**(Optional but recommended)
Ensure you have a Python virtual environment to isolate your project dependencies.
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```

3. **Install Required Dependencies** 
Navigate to the project directory and install the dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

4. **Make Database Connection** 
This project uses **MySQL** as the database. Ensure MySQL is installed (option full) and running on your system. Then you will need to create a file in your app called `mydb.py`, and connect the database with the following code:
    ```bash
    #3 - add file: dcrm/mydb.py.

    import mysql.connector #4 - Import the mysql connection.

    dataBase = mysql.connector.connect( #5 - Establish a connection and define your DB.
    
    host = 'localhost',
    user = 'user_created_at_time_of_install',
    passwd = 'password_created_at_time_of_install'
    )

    #6 - Prepare a cursor object.
    cursorObject= dataBase.cursor()

    #7 - Create a DB using mySQL commands
    cursorObject.execute('CREATE DATABASE prefered_db_name')

    print('All Done!!!')
    ```

5. **Configure Database Configuration** 
Update the database credentials in your `settings.py` file:
    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1 - Change DB to mysql.
        'NAME': 'prefered_db_name', #2 - Configure the DB for connection.
        'USER': 'user_created_at_time_of_install',
        'PASSWORD': 'password_created_at_time_of_install',
        'HOST': 'localhost',
        'PORT': '3306',
        }
    }
    ```

6. **Run Migrations to Set Up the Database Schema** 
Run the following commands in terminal:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a Superuser to Access the Django Admin**
    ```bash
    python manage.py createsuperuser
    Hit [Enter] after each prompt below:
    Username:
    Email Address:
    Password: (not visible)
    Password(again): (not visible)
    R/T to Test Environment Bypass Password Validation and create user anyway? [y/N]: y
    ```

8. **Run the Django Development Server** 
Start the server to view the project in your browser:
    ```bash
    python manage.py runserver
    ```

9. **Visit the Application** Open your browser and visit:
    - **Application**: `http://127.0.0.1:8000/`
    - **Django Admin**: `http://127.0.0.1:8000/admin`

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## Contributing

I have learned that contributions are the heart of what makes the open source community such an amazing place! We are constantly able to learn, grow, inspire eachother, and create incredible things. Any contributions you make are **greatly appreciated**, we are so lucky to be here together.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please, don't forget to give the project a :star:! 

I appreciate you!

<p align="right">(<a href="#readme-top">top of page</a>)</p>



## License

Distributed under the MIT License. See `License` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Acknowledgments

Please take some time to check out the links below! 

I found value in each and every one of them, so my hope is that you will to!

* [Codemycom | John Elder](https://youtu.be/t10QcFx7d5k?si=ZKdAA34EEqe5wBFR) - ***Special thanks for the incredible tutorial video!***
* [MySQL Download](https://dev.mysql.com/downloads/file/?id=532678)
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Basic Syntax: Markdown Guide](https://www.markdownguide.org/basic-syntax/#reference-style-links)
* [Formatting Syntax: GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#animal-bug)

<p align="right">(<a href="#readme-top">top of page</a>)</p>
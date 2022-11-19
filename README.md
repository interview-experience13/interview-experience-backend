<!-- Please update value in the {}  -->

<h1 align="center">interview-experience-backend</h1>

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/interview-experience13/interview-experience-backend

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Add the following to your .env file
    SECRET_KEY=<yourSecretKeyHere>
    DEBUG=True # switch to True when in production
    ENV_NAME=dev # switch to prod when in production
    SQL_DATABASE=<yourDatabaseProjectName>
    SQL_USER=<yourDatabaseUsername> 
    SQL_PASSWORD=<yourDatabasePassword>
    SQL_HOST=localhost 
    SQL_PORT=5432

# Run the app
    $ python manage.py runserver
```

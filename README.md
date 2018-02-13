#flash Sacco
*An easy way to manage Saccos*

##How to contribute
### 1. Download
`$ mkvirtualenv --clear projectname`
Now, you need the *django-sample-app* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git://github.com/brianokinyi/flash_sacco projectname && cd projectname

### 2. Requirements
Right there, you will find the *package.json* file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:

`$ npm install`

### 3. Tweaks

#### wsgi.py
`projectname/wsgi.py` file is necessary for WSGI gateways (such as uWSGI) to run your Django application and also required from Django itself. You definitely want to change `{{ project_name }}` value in this file to whatever you name your application (e.g. `bookstore.settings`).

#### SECRET_KEY
Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open your `projectname/settings/default.py`, find `SECRET_KEY` line, paste your secret key.

#### Other settings stuff
It is good idea to make a **find & replace** within this default settings file as there are some "{{ project_name }}" string left such as `ROOT_URLCONF` or `LOCAL_APPS` variables.

#### Main URL root
You also have to config your application URLs, specific to your own needs. For the beginning, the sample app has only one view that you need to modify its namespace from `projectname/urls.py`, where it *imports HomeView*.

#### local.py (development specific) settings file
Copy `projectname/settings/local.template.py` as `local.py` into the same directory and modify necessary changes. **local.py** is always ignored by **.gitignore**, so this is the machine specific settings mostly for development purposes.

#### Initialize the database
First set the database engine (PostgreSQL, MySQL, etc..) in your settings files; `projectname/settings/default.py` and/or `projectname/settings/local.py`. Of course, remember to install necessary database driver for your engine. Then define your credentials as well. Time to finish it up:

`./manage.py migrate`

### Ready? Go!

`./manage.py runserver`

or

`./manage.py runserver_plus` (Requires Werkzeug)
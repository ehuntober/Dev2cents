## Dev2Censt

Dev2cents is a platform where developers(senior,mid-dev) post facts, quote, motivation about development, software engineering,tech etc, which will motivate other developers(newbie) and aid them in their career as a developer

## Features

Users are able to:

1. Create account
2. Make cents

## TECHNOLOGIES USED FOR THE BACKEND

Dev2Cents is built using

- **PYTHON**

  ![PYTHON](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/rsz_python.png)

- **HTML**

  ![HTML](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/rsz_html.png)

- **CSS**

  ![CSS](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/rsz_css.png)

- **DJANGO**
  
  ![DJANGO](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/rsz_django.png)

- **BOOTSTRAP**

  ![BOOTSTRAP](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/bootstrap-transformed.png)

- **MARIA DB (database used)**

  ![MARIADB](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/rsz_mariadb.png)

- **JAVASCRIPT**

  ![JAVASCRIPT](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/rsz_js.png)

### Installation

To run this project on your machine. Make sure you have __python3__ installed on your machine.
Create a virtual environment on your code editor using the command

```virtualenv <name of environment>```

If virtualenv is not installed on your machine. Install it or use this alternative to create a virtual environment

```python -m venv <name of environment>```

After virtual environment has been created. Install all packages listed in the requirements.txt file using the command
below:

```pip install -r requirements.txt```

All packages should install without errors.

After package installation, generate a secret key in your terminal with the command below

```
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

This generates a secret key. Copy the key

Create a ```.env``` file in the product directory

Input ```SECRET_KEY=<secret key copied from terminal>```

Then run the python server with the command

```python3 manage.py runserver```

### Preview

![Dev2cents](https://github.com/ehuntober/Dev2cents/blob/master/static/tools/Screenshot1.png)


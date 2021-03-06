
# NIT_Admission_System

NIT_Admission_System is an online admission system for NITs built with [Python][0] using the [Django Web Framework][1]. The initial version aims to automate the admission procedures at NITK Surathkal.

This project has the following basic apps:

* profiles (manages the profiles of the users)
* accounts (manages accounts (signup, login, etc))
* admissions (manages the admission procedure)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3.4. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3.4 -m venv NIT_Admission_System`
    2. `$ . NIT_Admission_System/bin/activate`

> Sometimes, binaries like pip get installed inside `local/bin/`. So append
> this line to `NIT_Admission_System/bin/activate`:
>
> `PATH="$VIRTUAL_ENV/local/bin:$PATH"`

Now the pip commands should work smoothly. Install all dependencies:

    pip install -r dev-requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for a detailed instructions guide.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/

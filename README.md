Frameable Setup
===============

Installation
============

To begin you can clone this repository and setup Django using the following instructions.

Linux Installation (Debian/Ubuntu)
----------------------------------

Note:

    - The following will assume you are cloning the sourcecode to **~/Projects/frameable**.  If you are cloning to a different location, you will need to adjust these instructions accordingly.
    - A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:alexrybrown/frameable.git

2. Install some required packages::

        $ sudo apt-get install python3 python3-dev python-pip

3.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

4.  Add the following to your **~/.bashrc** or **~/.zshrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your virtualenv (for Python 3)::

        $ mkvirtualenv frameable -p /usr/bin/python3


7.  Add the following to the end of the file **~/.virtualenvs/jdc/bin/postactivate**::

        export DJANGO_SETTINGS_MODULE=frameable.settings.dev
        export PYTHONPATH=~/Projects/frameable

8.  Activate the virtualenv::

        $ workon frameable

9.  Install the required Python libraries (ensure you're within the new virtual environment).::

        (frameable)$ pip install -r ~/Projects/frameable/requirements.pip
        
11.  Start the runserver.::

        (frameable)$ python ~/Projects/frameable/manage.py runserver
        
12.  Open your browser and see your site.::

        http://127.0.0.1:8000/


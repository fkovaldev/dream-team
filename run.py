#!flask/bin/python
# run.py

import os

from app import create_app

config_name = 'development'
app = create_app(config_name)
print("XXX irun.py __name__:{0}".format(__name__))
if __name__ == '__main__':
    app.run()

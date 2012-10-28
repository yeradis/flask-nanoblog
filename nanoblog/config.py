# Flask-Nanoblog Configuration

# MongoEngine configuration params , default None

# MONGODB = db
# MONGODB_USERNAME = username
# MONGODB_PASSWORD = password
# MONGODB_HOST = host
# MONGODB_PORT = port
MONGODB_DB = 'nanoblog'

# Flask configuration params http://flask.pocoo.org/docs/config/

# SECRET_KEY = If a secret key is set, cryptographic components can use this 
# to sign cookies and other things. 
# Set this to a complex random value when you want to use the secure cookie 
# for instance. 
# So when going to production CHANGE 'developmentkey' for a good key xD
SECRET_KEY = 'developmentkey'
DEBUG = True

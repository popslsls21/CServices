import os

# The socket to bind
bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"

# Number of worker processes
workers = 4

# Number of threads per worker
threads = 2

# Timeout in seconds
timeout = 60

# Where to put logs
accesslog = "-"  # stdout
errorlog = "-"   # stderr

# Log level
loglevel = "info"

# Whether to reload when code changes
reload = False  # Set to False for production

# Path to the app
pythonpath = "car_service"

# The WSGI application
wsgi_app = "app:app"
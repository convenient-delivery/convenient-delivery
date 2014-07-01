import multiprocessing


#set to false for production!!
debug = True
reload = True
spew = False # This is the nuclear debug option
daemon = False #Daemonize :P :: We don't do this because we use supervisor to run and monitor the process.

#pidfile = ? #If not set no PID file will be written.

preload = False #This will save ram, however changes in code will require restart of master process.

#worker_tmp_dir = ? #if not set, the default directory will be used.

bind = "127.0.0.1:8005" #Change to Localhost for production with proxy
workers = multiprocessing.cpu_count() * 2 + 1

pythonpath = "/home/convenient/Django/convenient_delivery/"

backlog = 2048

max_requrests = 1000

#user and group to run worker processes as
user = "gunicorn"
#group = ?

secure_scheme_headers = {'X-FORWARDED-PROTOCOL': 'ssl', 'X-FORWARDED-PROTO': 'https', 'X-FORWARDED-SSL': 'on'}
forwarded_allow_ips = "127.0.0.1"

#logs
accesslog = "/home/convenient/Django/convenient_delivery/gunicorn/access.log"
errorlog = "/home/convenient/Django/convenient_delivery/gunicorn/error.log"
loglevel = "debug"
syslog = False #Send logs to syslog


timeout = 30

graceful_timeout = 30

keep_alive = 2

limit_request_line = 4094

limit_request_fields = 100

limit_request_field_size = 8190





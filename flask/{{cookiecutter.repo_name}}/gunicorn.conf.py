import os
import threading, sys, traceback


bind = os.getenv('HOST', '0.0.0.0') + ':' + os.getenv('PORT', '8000')

backlog = 2048

workers = os.cpu_count() * 2

worker_class = 'gevent'

worker_connections = 2048

timeout = 30

keepalive = 2

#   spew - Install a trace function that spews every line of Python
#       that is executed when running the server. This is the
#       nuclear option.
#
#       True or False
#
spew = False

daemon = False

raw_env = []

pidfile = None

umask = 0

user = None

group = None

tmp_upload_dir = None

errorlog = '-'

loglevel = 'info'

accesslog = None

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

proc_name = None

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    pass

def pre_exec(server):
    server.log.info("Forked child, re-executing.")

def when_ready(server):
    server.log.info("Server is ready. Spawning workers")

def worker_int(worker):
    worker.log.info("worker received INT or QUIT signal")

    ## get traceback info
    id2name = {th.ident: th.name for th in threading.enumerate()}
    code = []
    for threadId, stack in sys._current_frames().items():
        code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""),
            threadId))
        for filename, lineno, name, line in traceback.extract_stack(stack):
            code.append('File: "%s", line %d, in %s' % (filename,
                lineno, name))
            if line:
                code.append("  %s" % (line.strip()))
    worker.log.debug("\n".join(code))

def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")

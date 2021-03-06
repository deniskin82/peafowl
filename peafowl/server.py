# -*- coding: utf-8 -*-
import socket, logging, sys, time
from handler import Handler
from collection import QueueCollection

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 21122
DEFAULT_PATH = '/tmp/peafowl/'
DEFAULT_TIMEOUT = 60
DEFAULT_PID = '/var/run/peafowl.pid'
DEFAULT_VERBOSITY = 30

class Server(object):
    def __init__(self, **kwargs):
        """
        Initialize a new Peafowl server, but do not accept connections or
        process requests.
        """
        opts = {'host':DEFAULT_HOST, 'port':DEFAULT_PORT, 'path':DEFAULT_PATH, 'timeout':DEFAULT_TIMEOUT, 'debug':DEFAULT_VERBOSITY}
        opts.update(kwargs)
        if opts.has_key('log'):            
            logging.basicConfig(filename=opts['log'], level=DEFAULT_VERBOSITY - opts['debug'], format='%(asctime)s %(levelname)s %(message)s')
        else:
            logging.basicConfig(level=DEFAULT_VERBOSITY - opts['debug'], format='%(asctime)s %(levelname)s %(message)s')
        self.queue_collection = QueueCollection(opts['path'])
        self.stats = {'bytes_read':0, 'bytes_written':0, 'start_time':time.time(), 'connections':0, 
                      'total_connections':0, 'get_requests':0, 'set_requests':0}
        self.stats['start_time'] = time.time()
        self._bind(opts['host'], opts['port'])
    
    def _bind(self, host, port):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.server.bind((host, port))
            self.server.listen(5)
            logging.info("Listening to %s on port %s" % (host, port))
        except socket.error, e:
            if self.server:
                self.server.close()
            logging.error("Could not open socket: %s" % e.message)
            sys.exit(1)
    
    def run(self):
        while True:
            try:
                self.stats['connections'] += 1
                client, address = self.server.accept()
                Handler(client, self.queue_collection, self.stats).start()
                self.stats['connections'] -= 1
            except socket.error, e:
                sys.exit(1)
    
    def stop(self):
        self.queue_collection.close()
        if self.server:
            self.server.close()
    
    @staticmethod
    def start(**kwargs):
        """
        Start listening and processing requests.
        """
        server = Server(**kwargs)
        server.run()
        return server


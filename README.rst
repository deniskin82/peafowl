Name
====

Peafowl - a light weight server for distributed message passing based on Starling.

Synopsis
========

::

    # Start the Peafowl server as a daemonized process:
    >>> peafowl -H 192.168.1.1 -d

    # Put messages onto a queue:
    >>> from memcache import Client
    >>> peafowl = Client(['192.168.1.1:22122'])
    >>> peafowl.set('my_queue', 12345)

    # Get messages from the queue:
    >>> from memcache import Client
    >>> peafowl = Client(['192.168.1.1:22122'])
    >>> while True:
    >>>     print peafowl.get('my_queue')

Description
===========

Peafowl is a powerful but simple messaging server that enables reliable 
distributed queuing with an absolutely minimal overhead. It speaks the
MemCache protocol for maximum cross-platform compatibility. Any language
that speaks MemCache can take advantage of Peafowl's queue facilities.

Known Issues
============

* Peafowl is a pure port of Starling (written by Blaine Cook), it's only to be use if you can't bear ruby.

Authors
=======

Timothée Peignier <tim@tryphon.org>

Original author
===============

Blaine Cook <romeda@gmail.com>

Copyright
=========

Peafowl is : Copyright 2008 Timothée Peignier <tim@tryphon.org>

Starling is : Copyright 2007 Blaine Cook <blaine@twitter.com>, Twitter Inc.

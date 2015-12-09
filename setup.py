#!/usr/bin/env python

'''A Python-based command-line client for running simple CQL commands on a Cassandra cluster

cqlsh is a Python-based command-line tool, and the most direct way
to run simple CQL commonds on a Cassandra cluster.  This is a simple
re-bundling of the open source tool that comes bundled with Cassandra
to allow for cqlsh to be installed and run inside of virtual
environments.'''

from distutils.core import setup

doclines = __doc__.split("\n")

setup(
    name='cqlsh',
    version='3',
    description=doclines[0],
    long_description='\n'.join(doclines[2:]),
    keywords='python cql cassandra cqlsh',
    maintainer='Anthony Scalisi',
    maintainer_email='scalisi.a@gmail.com',
    url='https://github.com/apache/cassandra',
    platforms=['any'],
    license="http://www.apache.org/licenses/LICENSE-2.0",
    install_requires=['cql', 'simplejson', 'unittest2', 'cassandra-driver >= 3'],
    packages=['cqlshlib'],
    scripts = [
        'cqlsh',
    ]
)

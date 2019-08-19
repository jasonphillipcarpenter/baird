=====
BAIRD
=====

Baird is a system administration tool for simultaneous management of multiple instances through SSH.  Baird utilises tmux_ to create individual panes per instance and facilitate synchronised input.

.. _tmux: https://tmux.github.io/

Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@gitlab.com:boweevil/baird``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Installation
------------

Usage
-----

.. code-block:: bash

  baird [-h] [-t <TITLE>] [-l <LOGIN>] [-i <IDENTITY FILE>]
        [-b <BASTION SERVER>] [-bl <BASTION LOGIN>] [-bi <BASTION ID>]
        <SERVER LIST> [<SERVER LIST> ...]


* Connect with user and key:

.. code-block:: bash

  baird -l user1 -i ~/.ssh/key server1 server2 server3


* Using only a list of servers:

.. code-block:: bash

  baird server1 server2 server3 server4 server5


* Bash globbing:

.. code-block:: bash

  baird server{01..05}


* Using a bastion server:

.. code-block:: bash

  baird --title 'Production' --bastion bastion01 --bastion-login bastionuser --bastion-id ~/.ssh/bastionkey --login serveruser --identityfile ~/.ssh/serverkey server{1..3}


Running Tests
-------------

.. code-block:: bash

  make test

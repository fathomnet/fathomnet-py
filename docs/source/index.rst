.. fathomnet-py documentation master file, created by
   sphinx-quickstart on Tue Sep  7 16:25:28 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

fathomnet-py
============

``fathomnet-py`` is a client-side API to help scientists, researchers, and developers interact with `FathomNet Database`_ data.

.. code-block:: python

   >>> from fathomnet.api import boundingboxes
   >>> boundingboxes.find_concepts()
   ['2G Robotics structured light laser', '55-gallon drum', ...]
   >>> from fathomnet.api import images
   >>> images.find_by_concept('Nanomia')
   [
      AImageDTO(
         id=2274942, 
         uuid='cdbfca66-284f-48ac-a36f-7b2ac2b43533', 
         url='https://database.fathomnet.org/static/m3/framegrabs/MiniROV/images/0056/02_18_37_20.png', 
         ...
      ),
      ...
   ]
   >>> from fathomnet.api import taxa
   >>> taxa.find_children('fathomnet', 'Bathochordaeus')
   [
      Taxa(name='Bathochordaeus stygius', rank='species'), 
      Taxa(name='Bathochordaeus charon', rank='species'), 
      Taxa(name='Bathochordaeus mcnutti', rank='species')
   ]
   >>> from fathomnet.api import xapikey
   >>> xapikey.auth('NuCLjlNUlgHchtgDB01Sp1fABJVcWR')  # your API key here
   AuthHeader(
      type='Bearer', 
      token='eyJhbGciOiJI...'
   )

The ``fathomnet-py`` API offers native Python interaction with the FathomNet REST API, abstracting away the underlying HTTP requests.

.. image:: https://github.com/fathomnet/fathomnet-py/actions/workflows/cicd.yml/badge.svg
   :target: https://github.com/fathomnet/fathomnet-py/actions/workflows/cicd.yml
   :alt: cicd

.. image:: https://readthedocs.org/projects/fathomnet-py/badge/?version=latest
   :target: https://fathomnet-py.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Installing fathomnet-py
-----------------------

``fathomnet-py`` is available on PyPI:

.. code-block:: bash
   
   $ python -m pip install fathomnet


.. toctree::
   :maxdepth: 2
   :caption: API Documentation

   api
   dto
   scripts

.. Indices and tables
.. ==================
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`


.. _FathomNet Database: https://database.fathomnet.org/
API Modules
===========

The ``fathomnet-py`` API is provided via the ``fathomnet.api`` package, and is broken into separate modules for the various FathomNet REST servlets.

----

Bounding Boxes
--------------

.. module:: fathomnet.api.boundingboxes

The ``fathomnet.api.boundingboxes`` module supports bounding box operations.

Create, update, & delete
^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: create_with_dto
.. autofunction:: update
.. autofunction:: delete

Bulk create
^^^^^^^^^^^

.. autofunction:: upload_csv

Find
^^^^

.. autofunction:: find_by_user_defined_key
.. autofunction:: find_by_uuid

List & count
^^^^^^^^^^^^

.. autofunction:: find_concepts
.. autofunction:: find_observers
.. autofunction:: find_all_user_defined_keys
.. autofunction:: count_all
.. autofunction:: count_by_concept
.. autofunction:: count_total_by_concept

Audit
^^^^^

.. autofunction:: audit_by_uuid
.. autofunction:: audit_by_user_defined_key

----

Darwin Core
-----------

.. module:: fathomnet.api.darwincore

The ``fathomnet.api.darwincore`` module supports owner institution darwin core operations.

.. note:: The ``darwincore`` servlet is WIP; This subsection may be updated as new functionality is added.

.. automodule:: fathomnet.api.darwincore
    :members:
    :noindex:

----

Firebase
--------

.. module:: fathomnet.api.firebase

The ``fathomnet.api.firebase`` module supports firebase authentication operations.

.. warning:: The ``firebase`` servlet that this module wraps is designed for application-level authentication. Typical users will not need to use this module.

.. automodule:: fathomnet.api.firebase
    :members:
    :noindex:

----

Geo-images
----------

.. module:: fathomnet.api.geoimages

The ``fathomnet.api.geoimages`` module supports geo-image operations.

.. automodule:: fathomnet.api.geoimages
    :members:
    :noindex:

----

Images
------

.. module:: fathomnet.api.images

The ``fathomnet.api.images`` module supports image operations.

Create, update, & delete
^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: create_if_not_exists
.. autofunction:: update
.. autofunction:: delete

Find
^^^^

.. autofunction:: find
.. autofunction:: find_all
.. autofunction:: find_all_alt
.. autofunction:: find_by_concept
.. autofunction:: find_by_contributors_email
.. autofunction:: find_by_observer
.. autofunction:: find_by_sha256
.. autofunction:: find_by_tag_key
.. autofunction:: find_by_url
.. autofunction:: find_by_uuid
.. autofunction:: find_by_uuid_in_list

List & count
^^^^^^^^^^^^

.. autofunction:: find_distinct_submitter
.. autofunction:: list_imaging_types
.. autofunction:: count_all
.. autofunction:: count_by_submitter

----

Image Set Uploads
-----------------

.. module:: fathomnet.api.imagesetuploads

The ``fathomnet.api.imagesetuploads`` module supports image set upload operations.


Find
^^^^

.. autofunction:: find_collections
.. autofunction:: find_by_image_uuid
.. autofunction:: find_by_contributor
.. autofunction:: find_by_uuid

List & count
^^^^^^^^^^^^

.. autofunction:: find_rejection_reasons
.. autofunction:: find_contributors
.. autofunction:: count_all

Compute stats
^^^^^^^^^^^^^

.. autofunction:: stats

----

Regions
-------

.. module:: fathomnet.api.regions

The ``fathomnet.api.regions`` module supports marine region operations.

.. automodule:: fathomnet.api.regions
    :members:
    :noindex:

----

Stats
-----

.. module:: fathomnet.api.stats

The ``fathomnet.api.stats`` module supports summary statistic operations.

.. automodule:: fathomnet.api.stats
    :members:
    :noindex:

----

Tags
----

.. module:: fathomnet.api.tags

.. note:: Tags API added in v0.4.0

The ``fathomnet.api.tags`` module supports tag operations.

Create, update, & delete
^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: create_with_dto
.. autofunction:: update
.. autofunction:: delete

Find
^^^^

.. autofunction:: find_by_uuid
.. autofunction:: find_by_image_uuid_and_key

----

Taxa
----

.. module:: fathomnet.api.taxa

The ``fathomnet.api.taxa`` module supports taxonomic (phylogenic) lookup operations.

.. automodule:: fathomnet.api.taxa
    :members:
    :noindex:

----

Users
-----

.. module:: fathomnet.api.users

The ``fathomnet.api.users`` module supports user account operations.

Account operations
^^^^^^^^^^^^^^^^^^

.. autofunction:: create_new_api_key
.. autofunction:: delete_api_key
.. autofunction:: update_user_data


List & count
^^^^^^^^^^^^

.. autofunction:: find_all
.. autofunction:: find_by_authentication
.. autofunction:: find_by_email
.. autofunction:: find_by_firebase_uid
.. autofunction:: find_contributors_names
.. autofunction:: find_expertise
.. autofunction:: find_roles
.. autofunction:: count_all

Miscellaneous
^^^^^^^^^^^^^

.. autofunction:: get_api_key
.. autofunction:: verify

Admin only
^^^^^^^^^^

.. autofunction:: disable_by_uuid
.. autofunction:: update_user_data_admin

----

WoRMS
-----

.. module:: fathomnet.api.worms

The ``fathomnet.api.worms`` module supports World Register of Marine Species (WoRMS) lookup operations via the `fast WoRMS name service <https://github.com/fathomnet/worms-server>`_.

.. automodule:: fathomnet.api.worms
    :members:
    :noindex:

----

X-API-Key
---------

.. module:: fathomnet.api.xapikey

The ``fathomnet.api.xapikey`` module supports X-API-Key authentication operations.

.. automodule:: fathomnet.api.xapikey
    :members:
    :noindex:

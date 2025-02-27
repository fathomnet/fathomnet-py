Scripts
=======

This page documents the scripts that are included with ``fathomnet-py``.

----

``fathomnet-generate``
----------------------

The ``fathomnet-generate`` script generates object detection datasets in common formats (COCO, Pascal VOC) from FathomNet data.
It is installed by default with ``fathomnet-py``.

There are two modes of invoking ``fathomnet-generate``: **output** and **count**.

Output
^^^^^^

**Output** mode generates the dataset and writes it to disk. 

Targets
"""""""

For example, to generate a Pascal VOC dataset for the *Abraliopsis* concept, we would run:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts 'Abraliopsis'

This will write Pascal VOC XML files containing all FathomNet bounding boxes for *Abraliopsis* to ``/path/to/output/*.xml``.

If we run the command again with the ``-v`` flag, we can see the progress of the dataset generation:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts 'Abraliopsis' -v

.. code-block:: text

    INFO:root:Successfully parsed flags
    INFO:root:Concept(s) specified:
    INFO:root:- Abraliopsis
    INFO:root:Fetching image records for 1 concept(s)...
    INFO:root:Found 59 unique images with bounding boxes
    INFO:root:Wrote 59 VOC files to /path/to/output

The ``--concepts`` flag accepts a comma-separated list of concepts. For example, if we want both *Abraliopsis* and *Bathochordaeus*:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts 'Abraliopsis,Bathochordaeus' -v

.. code-block:: text

    INFO:root:Successfully parsed flags
    INFO:root:Concept(s) specified:
    INFO:root:- Abraliopsis
    INFO:root:- Bathochordaeus
    INFO:root:Fetching image records for 2 concept(s)...
    INFO:root:Found 1360 unique images with bounding boxes
    INFO:root:Wrote 1360 VOC files to /path/to/output

It's worth noting: **the dataset will only include bounding boxes of the exact concepts you specify.** 
If we want to include the species in both the *Abraliopsis* and *Bathochordaeus* genera, we need to specify a taxonomy provider that will extend the concept list to include the species in those genera.
For example, we can use the ``fathomnet`` taxonomy provider to do this, which includes the World Register of Marine Species (WoRMS) taxonomy and the Monterey Bay Aquarium Research Institute (MBARI) Deep-Sea Guide (DSG) taxonomy:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts 'Abraliopsis,Bathochordaeus' -v --taxa fathomnet

.. code-block:: text

    INFO:root:Successfully parsed flags
    INFO:root:Concept(s) specified:
    INFO:root:- Abraliopsis
    INFO:root:- Abraliopsis (Abraliopsis)
    INFO:root:- Abraliopsis (Abraliopsis) hoylei
    INFO:root:- Abraliopsis (Abraliopsis) morisii
    INFO:root:- Abraliopsis (Abraliopsis) pacificus
    INFO:root:- Abraliopsis (Abraliopsis) tui
    INFO:root:- Abraliopsis (Boreabraliopsis)
    INFO:root:- Abraliopsis (Boreabraliopsis) felis
    INFO:root:- Abraliopsis (Micrabralia)
    INFO:root:- Abraliopsis (Micrabralia) atlantica
    INFO:root:- Abraliopsis (Micrabralia) chuni
    INFO:root:- Abraliopsis (Micrabralia) gilchristi
    INFO:root:- Abraliopsis (Micrabralia) lineata
    INFO:root:- Abraliopsis (Pfefferiteuthis)
    INFO:root:- Abraliopsis (Pfefferiteuthis) affinis
    INFO:root:- Abraliopsis (Pfefferiteuthis) atlantica
    INFO:root:- Abraliopsis (Pfefferiteuthis) chuni
    INFO:root:- Abraliopsis (Pfefferiteuthis) falco
    INFO:root:- Abraliopsis (Watasenia)
    INFO:root:- Abraliopsis (Watasenia) felis
    INFO:root:- Abraliopsis affinis
    INFO:root:- Abraliopsis atlantica
    INFO:root:- Abraliopsis chuni
    INFO:root:- Abraliopsis falco
    INFO:root:- Abraliopsis felis
    INFO:root:- Abraliopsis gilchristi
    INFO:root:- Abraliopsis hoylei
    INFO:root:- Abraliopsis joubini
    INFO:root:- Abraliopsis lineata
    INFO:root:- Abraliopsis morisii
    INFO:root:- Abraliopsis pacificus
    INFO:root:- Abraliopsis pfefferi
    INFO:root:- Abraliopsis scintillans
    INFO:root:- Abraliopsis tui
    INFO:root:- Bathochordaeus
    INFO:root:- Bathochordaeus charon
    INFO:root:- Bathochordaeus mcnutti
    INFO:root:- Bathochordaeus stygius
    INFO:root:Fetching image records for 38 concept(s)...
    INFO:root:Found 3376 unique images with bounding boxes
    INFO:root:Wrote 3376 VOC files to /path/to/output

For larger queries, it's recommended to write a file containing the concepts you want to query, one per line, and pass that file to ``fathomnet-generate`` using the ``--concepts-file`` flag.
For example, we can write a file called ``concepts.txt`` containing the following:

.. code-block:: text

    Bathochordaeus charon
    Bathochordaeus mcnutti
    Bathochordaeus stygius

and then run:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts-file concepts.txt -v --taxa fathomnet

.. code-block:: text

    INFO:root:Successfully parsed flags
    INFO:root:Concept(s) specified:
    INFO:root:- Bathochordaeus charon
    INFO:root:- Bathochordaeus mcnutti
    INFO:root:- Bathochordaeus stygius
    INFO:root:Fetching image records for 3 concept(s)...
    INFO:root:Found 2013 unique images with bounding boxes
    INFO:root:Wrote 2013 VOC files to /path/to/output

In some contexts, we want to gather all of the bounding boxes in each image, instead of only the bounding boxes for our specified concepts. We can do this by passing the ``--all`` flag:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts 'Bathochordaeus' -v --all

If we look at a generated XML file, we can note the inclusion of other concepts:

.. code-block:: xml

    <annotation>
        <folder>3007</folder>
        <filename>00_10_24_26.png</filename>
        <path>https://database.fathomnet.org/static/m3/framegrabs/Ventana/images/3007/00_10_24_26.png</path>
        <source>
            <database>FathomNet</database>
        </source>
        <size>
            <width>720</width>
            <height>368</height>
            <depth>3</depth>
        </size>
        <segmented>0</segmented>
        <object>
            <name>Bathochordaeus inner filter</name>
            <pose>Unspecified</pose>
            <truncated>0</truncated>
            <difficult>0</difficult>
            <occluded>0</occluded>
            <bndbox>
            <xmin>578</xmin>
            <xmax>601</xmax>
            <ymin>158</ymin>
            <ymax>185</ymax>
            </bndbox>
        </object>
        <object>
            <name>Apolemia</name>
            <pose>Unspecified</pose>
            <truncated>0</truncated>
            <difficult>0</difficult>
            <occluded>0</occluded>
            <bndbox>
            <xmin>2</xmin>
            <xmax>516</xmax>
            <ymin>113</ymin>
            <ymax>366</ymax>
            </bndbox>
        </object>
    </annotation>

Output format
"""""""""""""

By default, ``fathomnet-generate`` will output Pascal VOC XML files. This can be changed by passing the ``--format`` flag:

.. code-block:: bash

    fathomnet-generate --output /path/to/output --concepts 'Bathochordaeus' -v --format coco

.. code-block:: text

    INFO:root:Successfully parsed flags
    INFO:root:Concept(s) specified:
    INFO:root:- Bathochordaeus
    INFO:root:Fetching image records for 1 concept(s)...
    INFO:root:Found 1301 unique images with bounding boxes
    INFO:root:Wrote COCO dataset to /path/to/output/dataset.json

The ``--format`` flag currently accepts ``coco`` and ``voc``.

Image downloading
"""""""""""""""""

By default, ``fathomnet-generate`` will not download images. Images can be downloaded to a specified directory by passing the ``--img-download`` option:

.. code-block:: text

    fathomnet-generate --output /path/to/output --img-download /path/to/output/images --concepts 'Abraliopsis' -v

.. code-block:: text
    
    INFO:root:Creating output directory /home/kbarnard/Desktop/test/images
    INFO:root:Successfully parsed flags
    INFO:root:Concept(s) specified:
    INFO:root:- Abraliopsis
    INFO:root:Fetching image records for 1 concept(s)...
    INFO:root:Found 59 unique images with bounding boxes
    INFO:root:Wrote 59 VOC files to /path/to/output
    100% (59 of 59) |################################| Elapsed Time: 0:00:03 Time:  0:00:03
    INFO:root:Downloaded 59 new images to /path/to/output/images

Note that for efficiency, ``fathomnet-generate`` will not re-download images that already exist in the specified directory. Images are renamed according to their FathomNet image UUID.

Constraints
"""""""""""

Once targets are specified, we can further constrain the dataset by passing a variety of flags. These are self-descriptive, and include:

* ``--contributor-email``
* ``--start`` / ``--end`` (`ISO-8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date strings)
* ``--imaging-types`` (comma-separated list of imaging types to include)
* ``--exclude-unverified``
* ``--exclude-verified``
* ``--min-longitude`` / ``--max-longitude``
* ``--min-latitude`` / ``--max-latitude``
* ``--min-depth`` / ``--max-depth``
* ``--institutions`` (comma-separated list of institutions to include)

Count
^^^^^

**Count** mode is effectively a dry run that prints the number of annotations that would be generated for a given query.

For example, to count the number of annotations for the *Bathochordaeus* genus and its descendants:

.. code-block:: bash

    fathomnet-generate --count --concepts 'Bathochordaeus' --taxa fathomnet

.. code-block:: text

    concept                |  # boxes
    -----------------------|---------
    Bathochordaeus         |     1901
    Bathochordaeus charon  |       99
    Bathochordaeus mcnutti |     1259
    Bathochordaeus stygius |     2471

All other flags described in **output** mode are available in **count** mode.

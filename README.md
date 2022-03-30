# fathomnet-py

**`fathomnet-py`** is a client-side API to help scientists, researchers, and developers interact with [FathomNet](https://fathomnet.org/) data.

```python
>>> from fathomnet.api import boundingboxes
>>> boundingboxes.find_concepts()
['2G Robotics structured light laser', '55-gallon drum', ...]
>>> from fathomnet.api import images
>>> images.find_by_concept('Nanomia')
[
    AImageDTO(
        id=2274942, 
        uuid='cdbfca66-284f-48ac-a36f-7b2ac2b43533', 
        url='https://fathomnet.org/static/m3/framegrabs/MiniROV/images/0056/02_18_37_20.png', 
        ...
    ),
    ...
]
>>> from fathomnet.api import taxa
>>> taxa.find_children('mbari', 'Bathochordaeus')
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
```

The `fathomnet-py` API offers native Python interaction with the FathomNet REST API, abstracting away the underlying HTTP requests.

[![tests](https://github.com/fathomnet/fathomnet-py/actions/workflows/tests.yml/badge.svg)](https://github.com/fathomnet/fathomnet-py/actions/workflows/tests.yml)
[![Documentation Status](https://readthedocs.org/projects/fathomnet-py/badge/?version=latest)](https://fathomnet-py.readthedocs.io/en/latest/?badge=latest)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fathomnet/fathomnet-py/blob/main/tutorial.ipynb)
## Installing `fathomnet-py`

`fathomnet-py` is available on PyPI:

```bash
$ python -m pip install fathomnet
```

## API Reference available on [Read the Docs](https://fathomnet-py.readthedocs.io/)

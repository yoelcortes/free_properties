===============
free_properties
===============

.. image:: http://img.shields.io/pypi/v/free_properties.svg?style=flat
   :target: https://pypi.python.org/pypi/free_properties
   :alt: Version_status
.. image:: http://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
   :target: https://free_properties.readthedocs.io/en/latest/
   :alt: Documentation
.. image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/yoelcortes/free_properties/blob/master/LICENSE.txt
   :alt: license


.. contents::

What is free_properties?
------------------------

free_properties is a python package that features the FreeProperty class. A FreePropety object behaves just like its value property, allowing it to be used as a proxy for get, and set calculations like a python property.

Installation
------------

Get the latest version of free_properties from
https://pypi.python.org/pypi/free_properties/

If you have an installation of Python with pip, simple install it with:

    $ pip install free_properties

To get the git version, run:

    $ git clone git://github.com/yoelcortes/free_properties

Documentation
-------------

array_collections's documentation is available on the web:

    http://array_collections.readthedocs.io/

Getting started
---------------

The PropertyFactory is an FreeProperty class creator that functions similar to Python 'property' objects. Use the PropertyFactory to create a Weight class which calculates weight based on density and volume:
    
.. code-block:: python
    
    >>> def getter(self):
    ...    '''Weight (kg) based on volume (m^3).'''
    ...    data = self.data
    ...    rho = data['rho'] # Density (kg/m^3)
    ...    vol = data['vol'] # Volume (m^3)
    ...    return rho * vol
    >>>
    >>> def setter(self, weight):
    ...    data = self.data
    ...    rho = data['rho'] # Density (kg/m^3)
    ...    data['vol'] = weight / rho
    >>>
    >>> # Initialize with a value getter, setter, and the class name.
    >>> Weight = PropertyFactory(getter, setter, 'Weight')
    
It is more convinient to use the PropertyFactory as a decorator:

.. code-block:: python
   
    >>> @PropertyFactory
    >>> def Weight(self):
    ...    '''Weight (kg) based on volume (m^3).'''
    ...    data = self.data
    ...    rho = data['rho'] # Density (kg/m^3)
    ...    vol = data['vol'] # Volume (m^3)
    ...    return rho * vol
    >>>
    >>> @Weight.setter
    >>> def Weight(self, weight):
    ...    data = self.data
    ...    rho = data['rho'] # Density (kg/m^3)
    ...    data['vol'] = weight / rho
   

Create dictionaries of data and initialize new Weight objects:
   
.. code-block:: python
   
   >>> water_data = {'rho': 1000, 'vol': 3}
   >>> ethanol_data = {'rho': 789, 'vol': 3}
   >>> weight_water = Weight('Water', water_data)
   >>> weight_ethanol = Weight('Ethanol', ethanol_data)
   >>> weight_water
   Weight(Water) -> 3000 (kg)
   >>>weight_ethanol
   Weight(Ethanol) -> 2367 (kg)

These properties behave just like their dynamic value:

.. code-block:: python

    >>> weight_water + 30
    3030
    >>> weight_water + weight_ethanol
    5367
    >>> weight_water.bit_length() # A method of the dynamic value
    12
    
Get and set the value through the 'value' attribute:
    
.. code-block:: python

    >>> weight_water.value
    3000
    >>> weight_water.value = 4000 
    >>> weight_water.value
    4000
    >>> water_data # Note that the volume changed too
    {'rho': 1000, 'vol': 4}

In place magic methods will also change the property value:

.. code-block:: python

    >>> weight_water.value -= 1000
    >>> weight_water
    Weight(Water) -> 3000 (kg)
    >>> water_data  # The change also affects the original data
    {'rho': 1000, 'vol': 3}

Latest source code
------------------

The latest development version of free_properties's sources can be obtained at:

    https://github.com/yoelcortes/free_properties


Bug reports
-----------

To report bugs, please use the free_properties' Bug Tracker at:

    https://github.com/yoelcortes/free_properties

License information
-------------------

See ``LICENSE.txt`` for information on the terms & conditions for usage
of this software, and a DISCLAIMER OF ALL WARRANTIES.

Although not required by the free_properties' license, if it is convenient for you,
please cite free_properties if used in your work. Please also consider contributing
any changes you make back, and benefit the community.


Citation
--------

To cite free_properties in publications use::

    Yoel Cortes-Pena (2019). free_properties: Manage properties outside a class.
    https://github.com/yoelcortes/free_properties
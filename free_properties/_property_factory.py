# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:18:27 2019

@author: Guest Group
"""
from ._free_property import metaProperty, FreeProperty

__all__ = ('PropertyFactory',)

# %% Property Factory


def PropertyFactory(fget=None, fset=None, clsname=None, doc=None, units=None,
                    slots=None):
    """Create an FreeProperty subclass with getter and setter functions.
    
    Parameters
    ----------
    fget : function, optional
        Should return value of instances. If not given, a decorator expecting
        fget will be returned.
    
    fset : function, optional
        Should set the value of instances.
    
    clsname : str, optional
        Name of the class. Defaults to the function name of fget.
    
    doc : str, optional
        Docstring of class. Defaults to the docstring of fget.
    
    units : str, optional
        Units of measure.

    slots : tuple[str], optional
        Slots for class.
    
    Examples
    --------
    
    The PropertyFactory is a FreeProperty class creator that functions similar to Python 'property' objects. Use the PropertyFactory to create a Weight class which calculates weight based on density and volume:
    
    .. code-block:: python
        
        >>> from free_properties import PropertyFactory
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
        >>> Weight = PropertyFactory(fget=getter, fset=setter, clsname='Weight', units='kg')
        
    It is more convinient to use the PropertyFactory as a decorator:
    
    .. code-block:: python
       
        >>> @PropertyFactory(units='kg')
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
       <Water: 3000 kg>
       >>> weight_ethanol
       <Ethanol: 2367 kg>
    
    .. Note::
        
       The units are taken from the the function docstring. The first word in parentesis denotes the units.
    
    These properties behave just like their dynamic value:
    
    .. code-block:: python
    
        >>> weight_water + 30
        3030
        >>> weight_water + weight_ethanol
        5367
        
    Get and set the value through the 'value' attribute:
        
    .. code-block:: python
    
        >>> weight_water.value
        3000
        >>> weight_water.value = 4000 
        >>> weight_water.value
        4000.0
        >>> water_data # Note that the volume changed too
        {'rho': 1000, 'vol': 4.0}

    In place magic methods will also change the property value:
    
    .. code-block:: python
    
        >>> weight_water -= 1000
        >>> weight_water
        <Water: 3000 kg>
        >>> water_data  # The change also affects the original data
        {'rho': 1000, 'vol': 3.0}
            
    """       
    if not fget:
        return lambda fget: PropertyFactory(fget, fset, clsname, doc, units, slots)
        
    # Defaults
    if clsname is None: clsname = fget.__name__
    if doc     is None: doc     = fget.__doc__
    
    definitions = {'__doc__': doc,
                   '__slots__': slots or ('name', 'data'),
                   '__module__': fget.__module__,
                   '_units': units,
                   'value': property(fget, fset)}        
    return metaProperty(clsname, (FreeProperty,), definitions)

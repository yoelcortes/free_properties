# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:18:27 2019

@author: Guest Group
"""
from ._free_property import metaProperty, FreeProperty

__all__ = ('PropertyFactory',)

# %% utils

def search_units(doc):
    # Find units
    par1 = doc.find('(')
    par2 = doc.find(')')
    if par1==-1 or par2==-1:
        units = ''
    else:
        units = doc[par1+1:par2]
    return units


# %% Property Factory


def PropertyFactory(fget=None, fset=None, clsname=None, doc=None, units=None,
                    slots=None):
    """Create an FreeProperty subclass with getter and setter functions.
    
    Parameters
    ----------
    
        fget : function
            Should return value of instances.
        
        fset : function
            Should set the value of instances.
        
        clsname : str
            Name of the class. If None, the function name of fget will be used
        
        doc : str
            Docstring of class. If None, the docstring of fget will be used.
        
        units : str
            Units of measure. If None, the docstring will be searched and units of measure in parenthesis will be used.
    
        slots : tuple[str]
            Slots for class.
    
    Examples
    --------
    
    The PropertyFactory is a FreeProperty class creator that functions similar to Python 'property' objects. Use the PropertyFactory to create a Weight class which calculates weight based on density and volume:
    
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
       Weight(Water): 3000 kg
       >>> weight_ethanol
       Weight(Ethanol): 2367 kg
    
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
        4000
        >>> water_data # Note that the volume changed too
        {'rho': 1000, 'vol': 4}

    In place magic methods will also change the property value:
    
    .. code-block:: python
    
        >>> weight_water -= 1000
        >>> weight_water
        Weight(Water): 3000 kg
        >>> water_data  # The change also affects the original data
        {'rho': 1000, 'vol': 3}
            
    """       
    if not fget:
        return lambda fget: PropertyFactory(fget, fset, clsname, doc, units, slots)
        
    # Defaults
    if clsname is None: clsname = fget.__name__
    if doc     is None: doc     = fget.__doc__
    if units   is None: units   = search_units(doc)
    
    definitions = {'__doc__': doc,
                   '__slots__': slots or ('name', 'data'),
                   '__module__': fget.__module__,
                   '_units': units,
                   'value': property(fget, fset)}        
    return metaProperty(clsname, (FreeProperty,), definitions)

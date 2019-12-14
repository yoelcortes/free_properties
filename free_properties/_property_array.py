# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 03:56:02 2019

@author: yoelr
"""
import numpy as np

__all__ = ('property_array',)

ndarray = np.ndarray
isa = isinstance

# %% Property array

class property_array(ndarray):
    """Create an array that allows for array-like manipulation of FreeProperty objects. All entries in a property_array must be instances of FreeProperty. Setting items of a property_array sets values of objects instead.
    
    Parameters
    ----------
        array : array_like[FreeProperty]
            Input data, in any form that can be converted to an array. This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.
    
        order : {'C', 'F'}
            Whether to use row-major (C-style) or column-major (Fortran-style) memory representation. Defaults to ‘C’.
    
    Examples
    --------
        Use the PropertyFactory to create a Weight property class which calculates weight based on density and volume:
    
        .. code-block:: python
        
            >>> from free_property import PropertyFactory, property_array
            >>>
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
           
        Create dictionaries of data and initialize new properties:
       
        .. code-block:: python
       
           >>> water_data = {'rho': 1000, 'vol': 3}
           >>> ethanol_data = {'rho': 789, 'vol': 3}
           >>> weight_water = Weight('Water', water_data)
           >>> weight_ethanol = Weight('Ethanol', ethanol_data)
           >>> weight_water
           <Weight(Water): 3000 kg>
           >>> weight_ethanol
           <Weight(Ethanol): 2367 kg>
          
        Create a property_array from data:
           
        .. code-block:: python
       
           >>> prop_arr = property_array([weight_water, weight_ethanol])
           >>> prop_arr
           property_array([<Water: 3000 kg>, <Ethanol: 2367 kg>], dtype=object)
           
        Changing the values of a property_array changes the value of its properties:
           
        .. code-block:: python
       
           >>> # Addition in place
           >>> prop_arr += 3000
           >>> prop_arr
           property_array([<Water: 6000 kg>, <Ethanol: 5367 kg>], dtype=object)
           >>> # Note how the data also changes
           >>> water_data
           {'rho': 1000, 'vol': 6.0}
           >>> ethanol_data
           {'rho': 789, 'vol': 6.802281368821292}
           >>> # Setting an item changes the property value
           >>> prop_arr[1] = 2367
           >>> ethanol_data
           {'rho': 789, 'vol': 3}
          
        New arrays have no connection to the property_array:
           
        .. code-block:: python
       
           >>> prop_arr - 1000 #  Returns a new array
           array([5000.0, 1367.0], dtype=object)
           >>> water_data #  Data remains unchanged
           {'rho': 1000, 'vol': 6.0}
    
    """
    __slots__ = ()          
    
    def __new__(cls, properties, order='C'):
        return np.asarray(properties, object, order).view(cls)
    
    @property
    def value(self):
        return np.array(self, float)
    
    def __setitem__(self, key, value):
        items = self[key]
        if isa(items, ndarray):
            for i, v in np.nditer((items, value), flags=('refs_ok',)):
                i.item().value = v 
        else:
            items.value = value
    
    def __array_wrap__(self, result):
        if self is result: return self
        else: return result.view(ndarray)
    
    def __iadd__(self, other):
        self[:] = ndarray.__add__(self, other)
        return self
    
    def __isub__(self, other): 
        self[:] = ndarray.__sub__(self, other)
        return self
    
    def __imul__(self, other): 
        self[:] = ndarray.__mul__(self, other)
        return self
    
    def __imatmul__(self, other):
        raise TypeError("in-place matrix multiplication is not (yet) supported")
    
    def __itruediv__(self, other): 
        self[:] = ndarray.__truediv__(self, other)
        return self
    
    def __ifloordiv__(self, other):
        self[:] = ndarray.__floordiv__(self, other)
        return self
    
    def __imod__(self, other): 
        self[:] = ndarray.__mod__(self, other)
        return self
    
    def __ipow__(self, other): 
        self[:] = ndarray.__pow__(self, other)
        return self
    
    def __ilshift__(self, other):
        self[:] = ndarray.__lshift__(self, other)
        return self
    
    def __irshift__(self, other):
        self[:] = ndarray.__rshift__(self, other)
        return self
    
    def __iand__(self, other): 
        self[:] = ndarray.__and__(self, other)
        return self
    
    def __ixor__(self, other): 
        self[:] = ndarray.__xor__(self, other)
        return self
    
    def __ior__(self, other):
        self[:] = ndarray.__or__(self, other)
        return self


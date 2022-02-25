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
    """
    Create an array that allows for array-like manipulation of FreeProperty 
    objects. All entries in a property_array must be instances of FreeProperty.
    Setting items of a property_array sets values of objects instead.
    
    Parameters
    ----------
        properties : array_like[FreeProperty]
    
    Examples
    --------
    Use the PropertyFactory to create a Weight property class which calculates
    weight based on density and volume:

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
       property_array([3000.0, 2367.0])
       
    Changing the values of a property_array changes the value of its properties:
       
    .. code-block:: python
   
       >>> # Addition in place
       >>> prop_arr += 3000
       >>> prop_arr
       property_array([6000.0, 5367.0])
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
       array([5000.0, 1367.0])
       >>> water_data #  Data remains unchanged
       {'rho': 1000, 'vol': 6.0}

    """
    def __new__(cls, properties):
        return np.asarray(properties, dtype=object).view(cls)
    
    @property
    def value(self):
        return np.array(self, float)
    
    def all(self, *args, **kwargs):
        return self.value.all(*args, **kwargs)
    
    def any(self, *args, **kwargs):
        return self.value.any(*args, **kwargs)
    
    def argmax(self, *args, **kwargs):
        return self.value.argmax(*args, **kwargs)
    
    def argmin(self, *args, **kwargs):
        return self.value.argmin(*args, **kwargs)
    
    def argpartition(self, *args, **kwargs):
        return self.value.argpartition(*args, **kwargs)
    
    def argsort(self, *args, **kwargs):
        return self.value.argsort(*args, **kwargs)
    
    def choose(self, *args, **kwargs):
        return self.value.choose(*args, **kwargs)
    
    def clip(self, *args, **kwargs):
        return self.value.clip(*args, **kwargs)
    
    def conj(self):
        return self.value.conj()
    
    def conjugate(self):
        return self.value.conjugate()
    
    def cumprod(self, *args, **kwargs):
        return self.value.cumprod(*args, **kwargs)
    
    def cumsum(self, *args, **kwargs):
        return self.value.cumsum(*args, **kwargs)
    
    def dot(self, *args, **kwargs):
        return self.value.dot(*args, **kwargs)
    
    def max(self, *args, **kwargs):
        return self.value.max(*args, **kwargs)
    
    def mean(self, *args, **kwargs):
        return self.value.mean(*args, **kwargs)
    
    def min(self, *args, **kwargs):
        return self.value.min(*args, **kwargs)
    
    def nonzero(self, *args, **kwargs):
        return self.value.nonzero(*args, **kwargs)
    
    def prod(self, *args, **kwargs):
        return self.value.prod(*args, **kwargs)
    
    def ptp(self, *args, **kwargs):
        return self.value.ptp(*args, **kwargs)
    
    def put(self, *args, **kwargs):
        return self.value.put(*args, **kwargs)
    
    def round(self, *args, **kwargs):
        return self.value.round(*args, **kwargs)
    
    def std(self, *args, **kwargs):
        return self.value.std(*args, **kwargs)
    
    def sum(self, *args, **kwargs):
        return self.value.sum(*args, **kwargs)
    
    def trace(self, *args, **kwargs):
        return self.value.trace(*args, **kwargs)
    
    def var(self, *args, **kwargs):
        return self.value.var(*args, **kwargs)
    
    def __getitem__(self, key):
        item = ndarray.__getitem__(self, key)
        if item.base is None:
            return item.value
        else:
            return item
    
    def __setitem__(self, key, value):
        items = ndarray.__getitem__(self, key)
        if isa(items, ndarray):
            for i, v in np.nditer((items, value), flags=('refs_ok', 'zerosize_ok')):
                i.item().value = v 
        else:
            items.value = value
    
    def __add__(self, other):
        return self.value + other
    
    def __sub__(self, other):
        return self.value - other
    
    def __mul__(self, other):
        return self.value * other
    
    def __matmul__(self, other):
        return self.value @ other
    
    def __truediv__(self, other):
        return self.value / other
    
    def __floordiv__(self, other):
        return self.value // other
    
    def __mod__(self, other):
        return self.value % other
    
    def __pow__(self, other):
        return self.value ** other
    
    def __lshift__(self, other):
        return self.value << other
    
    def __rshift__(self, other):
        return self.value >> other
    
    def __and__(self, other): 
        return self.value & other
    
    def __xor__(self, other): 
        return self.value ^ other
    
    def __or__(self, other):
        return self.value | other
    
    def __radd__(self, other):
        return other + self.value
    
    def __rsub__(self, other):
        return other - self.value
    
    def __rmul__(self, other):
        return other * self.value
    
    def __rmatmul__(self, other):
        return other @ self.value
    
    def __rtruediv__(self, other):
        return other / self.value
    
    def __rfloordiv__(self, other):
        return other // self.value
    
    def __rmod__(self, other):
        return other % self.value
    
    def __rpow__(self, other):
        return other ** self.value
    
    def __rlshift__(self, other):
        return other << self.value 
    
    def __rrshift__(self, other):
        return other >> self.value
    
    def __rand__(self, other):
        return other & self.value
    
    def __rxor__(self, other):
        return other ^ self.value
    
    def __ror__(self, other):
        return other | self.value
    
    def __iadd__(self, other):
        self[:] = self.value + other
        return self
    
    def __isub__(self, other): 
        self[:] = self.value - other
        return self
    
    def __imul__(self, other): 
        self[:] = self.value * other
        return self
    
    def __imatmul__(self, other):
        raise TypeError("in-place matrix multiplication is not (yet) supported")
    
    def __itruediv__(self, other): 
        self[:] = self.value / other
        return self
    
    def __ifloordiv__(self, other):
        self[:] = self.value // other
        return self
    
    def __imod__(self, other): 
        self[:] =self.value % other
        return self
    
    def __ipow__(self, other): 
        self[:] = self.value ** other
        return self
    
    def __ilshift__(self, other):
        self[:] = self.value << other
        return self
    
    def __irshift__(self, other):
        self[:] = self.value >> other
        return self
    
    def __iand__(self, other): 
        self[:] = self & other
        return self
    
    def __ixor__(self, other): 
        self[:] = self.value ^ other
        return self
    
    def __ior__(self, other):
        self[:] = self.value | other
        return self

    def __repr__(self):
        return super().__repr__().replace('dtype=object)', '').rstrip("\n, ") + ')'
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:19:27 2019

@author: Guest Group
"""
from .free_property import FreeProperty

__all__ = ('Item', 'Attribute')


# %% Simple Property Classes                

class Attribute(FreeProperty):
    """Create an Attribute class that acts as a proxy for the value of an attribute.
    
    **Parameters**
    
        **obj:** object the attribute belongs to.
        
        **key:** attribute key.
        
    **Examples**
    
        First we need an object with attributes. So lets create a dummy class for this and initialize it:
        
        .. code-block:: python
        
            >>> class Dummy:
            ...    
            ...     def __init__(self, value):
            ...         self.value = value
            ...     
            ...     def __str__(self):
            ...         return 'dummy'
            ...
            >>> dummy = Dummy(20)
            
        Create an Attribute object with the object and the key:
            
        .. code-block:: python
    
            >>> v = Attribute(dummy, 'value')
            >>> v
            dummy.value -> 20
            
        The attribute object acts as a proxy for getting and setting the value:
        
        .. code-block
            
            >>> dummy.value = 0
            >>> v
            dummy.value -> 0
            >>> v += 40
            >>> dummy.value
            40
    
    """
    
    __slots__ = ('obj', 'key')
    
    def __init__(self, obj, key):
        self.obj = obj
        self.key = key
    
    @property
    def value(self):
        return getattr(self.obj, self.key)
    
    @value.setter
    def value(self, value):
        setattr(self.obj, self.key, value)
    
    def __repr__(self):
        return f'{self.obj}.{self.key} -> {self.value}'
    

class Item(FreeProperty):
    """Create an Item class that acts as a proxy for the value of an item.
    
    **Parameters**
    
        **obj:** object the item belongs to.
        
        **key:** item key.
        
    **Examples**
    
        First we need an object with items. So let's create a dictionary with items:
            
        .. code-block:: python
        
            >>> dummy = {'value': 20}
        
        Create an Item object with the object and the key:
            
        .. code-block:: python
    
            >>> v = Item(dummy, 'value')
            >>> v
            {'value': 20}['value'] -> 20
            
        The attribute object acts as a proxy for getting and setting the value:
        
        .. code-block
            
            >>> dummy['value'] = 0
            >>> v
            {'value': 20}['value'] -> 0
            >>> v += 40
            >>> {'value': 20}['value']
            40
    
    """
    __slots__ = ('obj', 'key')
    
    def __init__(self, obj, key):
        self.obj = obj
        self.key = key
    
    @property
    def value(self):
        return self.obj.__getitem__(self.key)
    
    @value.setter
    def value(self, value):
        self.obj.__setitem__(self.key, value)
    
    def __repr__(self):
        key = self.key
        if isinstance(key, str): key = f"'{key}'"
        return f'{self.obj}[{key}] -> {self.value}'
    
    
    
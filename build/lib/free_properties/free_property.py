# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:19:03 2019

@author: Guest Group
"""

__all__ = ('FreeProperty',)

# %% Functions

def dim(string):
    """Return string with gray ansicolor coding."""
    return '\x1b[37m\x1b[22m' + string + '\x1b[0m'
    

# %% Metaclasses

# Do not include: '__new__', '__init__', '__del__', '__bytes__', '__repr__',
# '__str__', '__getattr__', '__getattribute__', '__hash__',
# '__setattr__', '__delattr__', '__dir__', '__get__', '__set__',
# '__delete__', '__set_name__',

magic_names = ('__str__', '__format__', '__lt__', '__le__', '__eq__', '__ne__', 
               '__gt__', '__ge__',
               '__bool__', '__call__', '__len__', '__getitem__',
               '__setitem__', '__delitem__', '__missing__', '__reversed__',
               '__contains__', '__add__', '__sub__', '__mul__', '__matmul__',
               '__truediv__', '__floordiv__', '__mod__', '__divmod__',
               '__pow__', '__lshift__', '__rshift__', '__and__', '__or__',
               '__radd__', '__rsub__', '__rmul__', '__rmatmul__',
               '__rtruediv__', '__rfloordiv__', '__rmod__', '__rdivmod__',
               '__rpow__', '__rlshift__', '__rrshift__', '__rand__',
               '__rxor__', '__ror__', '__neg__', '__pos__', '__abs__',
               '__float__', '__invert__', '__complex__', '__int__',
               '__index__', '__round__', '__trunc__', '__floor__',
               '__ceil__', '__enter__', '__exit__', '__await__', '__aiter__',
               '__anext__', '__aenter__', '__aexit__', '__div__') 
    
inplace_magic_names = ('__iadd__', '__isub__', '__imul__', '__imatmul__',
                       '__itruediv__', '__idiv__', '__ifloordiv__',
                       '__imod__', '__ipow__', '__ilshift__', '__irshift__',
                       '__iand__', '__ixor__', '__ior__')


class metaProperty(type):
    """Metaclass for FreeProperty and subclasses."""
    
    @property
    def units(cls):
        return cls._units
    
    @units.setter
    def units(cls, units):
        cls._units = units
    
    def getter(cls, fget):
        cls.value = cls.value.getter(fget)
        return cls
    
    def setter(cls, fset):
        cls.value = cls.value.setter(fset)
        return cls
    

class propConstructor(type):
    """Constructor for the FreeProperty class. This constructor creates class instances of metaProperty, not propConstructor."""
    @staticmethod
    def __wrap(name):
        check = isinstance
        def proxy_method(self, *args, **kwargs):
            method = getattr(self.value, name)
            return method(*(i.value if check(i, FreeProperty) else i for i in args),
                          **kwargs)
        return proxy_method
    
    @staticmethod
    def __iwrap(iname):
        name = iname[:2] + iname[3:] # Remove 'i'
        check = isinstance
        def proxy_method(self, *args, **kwargs):
            method = getattr(self.value, name)
            self.value = method(*(i.value if check(i, FreeProperty) else i for i in args),
                                **kwargs)
            return self
        return proxy_method
    
    def __new__(mcl, clsname, superclasses, new_definitions):
        wrap = mcl.__wrap
        for method_name in magic_names:
            method = new_definitions.get(method_name)
            if not method:
                new_definitions[method_name] = wrap(method_name)
        
        iwrap = mcl.__iwrap
        for method_name in inplace_magic_names:
            method = new_definitions.get(method_name)
            if not method:
                new_definitions[method_name] = iwrap(method_name)
                
        return metaProperty(clsname, superclasses, new_definitions) 


# %% Abstract Property Class

class FreeProperty(metaclass=propConstructor):
    """Abstract Property class. Child classes must include a 'value' property."""
    __slots__ = ('name', 'data')
    
    _units = ''
    
    def __init__(self, name, data):
        self.name = name
        self.data = data
    
    def __getattr__(self, key):
        return getattr(self.value, key)
    
    def __repr__(self):
        units = self._units
        if units: units = dim(f' ({units})')
        return f'{type(self).__name__}({self.name}) -> {self.value}{units}'
    
    
    
    
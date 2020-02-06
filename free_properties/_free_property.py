# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:19:03 2019

@author: Guest Group
"""

__all__ = ('FreeProperty',)

# %% Metaclasses

# Do not include: '__new__', '__init__', '__del__', '__bytes__', '__repr__',
# '__str__', '__getattr__', '__getattribute__', '__hash__',
# '__setattr__', '__delattr__', '__dir__', '__get__', '__set__',
# '__delete__', '__set_name__',

self_magic_names = ('__str__', '__format__', '__len__', 
                    '__float__', '__invert__', '__complex__', '__int__',
                    '__index__', '__round__', '__trunc__', '__floor__',
                    '__ceil__', '__enter__', '__exit__', '__await__', '__aiter__',
                    '__anext__', '__aenter__', '__aexit__', '__reversed__',
                    '__neg__', '__pos__', '__abs__')

multi_magic_names = ('__call__',)

other_magic_names = ('__lt__', '__le__', '__eq__', '__ne__', 
                      '__gt__', '__ge__', '__bool__', '__getitem__',
                      '__setitem__', '__delitem__', '__missing__',
                      '__contains__', '__add__', '__sub__', '__mul__', '__matmul__',
                      '__truediv__', '__floordiv__', '__mod__', '__divmod__',
                      '__pow__', '__lshift__', '__rshift__', '__and__', '__or__',
                      '__radd__', '__rsub__', '__rmul__', '__rmatmul__',
                      '__rtruediv__', '__rfloordiv__', '__rmod__', '__rdivmod__',
                      '__rpow__', '__rlshift__', '__rrshift__', '__rand__',
                      '__rxor__', '__ror__') 
    
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


# %% Abstract Property Class

isa = isinstance

class FreeProperty(metaclass=metaProperty):
    """Abstract Property class. Child classes must include a 'value' property."""
    __slots__ = ()
    _units = ''
    
    def __init__(self, *args, **kwargs):
        setfield = setattr
        for i, j in zip(self.__slots__, args): setfield(self, i, j)
        for i, j in kwargs.items(): setfield(self, i, j)
    
    def __call__(self, *args, **kwargs):
        return self.value(*args, **kwargs)
    
    def __len__(self):
        return self.value.__len__()
    
    def __float__(self):
        return self.value.__float__()
    
    def __invert__(self):
        return self.value.__invert__()
    
    def __complex__(self):
        return self.value.__complex__()
    
    def __int__(self):
        return self.value.__int__()
    
    def __index__(self):
        return self.value.__index__()
    
    def __round__(self):
        return self.value.__round__()
    
    def __trunc__(self):
        return self.value.__trunc__()
    
    def __floor__(self):
        return self.value.__floor__()
    
    def __ceil__(self):
        return self.value.__ceil__()
    
    def __enter__(self):
        return self.value.__enter__()
    
    def __exit__(self):
        return self.value.__exit__()
    
    def __await__(self):
        return self.value.__await__()
    
    def __aiter__(self):
        return self.value.__aiter__()
    
    def __anext__(self):
        return self.value.__anext__()
    
    def __aenter__(self):
        return self.value.__aenter__()
    
    def __aexit__(self):
        return self.value.__aexit__()
    
    def __reversed__(self):
        return self.value.__reversed__()
    
    def __neg__(self):
        return self.value.__neg__()
    
    def __pos__(self):
        return self.value.__pos__()
    
    def __abs__(self):
        return self.value.__abs__()
    
    def __bool__(self):
        return self.value.__bool__()
    
    def __format__(self, other):
        return self.value.__format__(other)
    
    def __lt__(self, other):
        return self.value.__lt__(other.value if isa(other, FreeProperty) else other)
    
    def __le__(self, other):
        return self.value.__le__(other.value if isa(other, FreeProperty) else other)
    
    def __eq__(self, other):
        return self.value.__eq__(other.value if isa(other, FreeProperty) else other)
    
    def __ne__(self, other):
        return self.value.__ne__(other.value if isa(other, FreeProperty) else other)
    
    def __gt__(self, other):
        return self.value.__gt__(other.value if isa(other, FreeProperty) else other)
    
    def __ge__(self, other):
        return self.value.__ge__(other.value if isa(other, FreeProperty) else other)
    
    def __getitem__(self, other):
        return self.value.__getitem__(other.value if isa(other, FreeProperty) else other)
    
    def __setitem__(self, other):
        return self.value.__setitem__(other.value if isa(other, FreeProperty) else other)
    
    def __delitem__(self, other):
        return self.value.__delitem__(other.value if isa(other, FreeProperty) else other)
    
    def __missing__(self, other):
        return self.value.__missing__(other.value if isa(other, FreeProperty) else other)
    
    def __contains__(self, other):
        return self.value.__contains__(other.value if isa(other, FreeProperty) else other)
    
    def __add__(self, other):
        return self.value.__add__(other.value if isa(other, FreeProperty) else other)
    
    def __sub__(self, other):
        return self.value.__sub__(other.value if isa(other, FreeProperty) else other)
    
    def __mul__(self, other):
        return self.value.__mul__(other.value if isa(other, FreeProperty) else other)
    
    def __matmul__(self, other):
        return self.value.__matmul__(other.value if isa(other, FreeProperty) else other)
    
    def __truediv__(self, other):
        return self.value.__truediv__(other.value if isa(other, FreeProperty) else other)
    
    def __floordiv__(self, other):
        return self.value.__floordiv__(other.value if isa(other, FreeProperty) else other)
    
    def __mod__(self, other):
        return self.value.__mod__(other.value if isa(other, FreeProperty) else other)
    
    def __divmod__(self, other):
        return self.value.__divmod__(other.value if isa(other, FreeProperty) else other)
    
    def __pow__(self, other):
        return self.value.__pow__(other.value if isa(other, FreeProperty) else other)
    
    def __lshift__(self, other):
        return self.value.__lshift__(other.value if isa(other, FreeProperty) else other)
    
    def __rshift__(self, other):
        return self.value.__rshift__(other.value if isa(other, FreeProperty) else other)
    
    def __and__(self, other):
        return self.value.__and__(other.value if isa(other, FreeProperty) else other)
    
    def __or__(self, other):
        return self.value.__or__(other.value if isa(other, FreeProperty) else other)
    
    def __radd__(self, other):
        return self.value.__radd__(other.value if isa(other, FreeProperty) else other)
    
    def __rsub__(self, other):
        return self.value.__rsub__(other.value if isa(other, FreeProperty) else other)
    
    def __rmul__(self, other):
        return self.value.__rmul__(other.value if isa(other, FreeProperty) else other)
    
    def __rmatmul__(self, other):
        return self.value.__rmatmul__(other.value if isa(other, FreeProperty) else other)
    
    def __rtruediv__(self, other):
        return self.value.__rtruediv__(other.value if isa(other, FreeProperty) else other)
    
    def __rfloordiv__(self, other):
        return self.value.__rfloordiv__(other.value if isa(other, FreeProperty) else other)
    
    def __rmod__(self, other):
        return self.value.__rmod__(other.value if isa(other, FreeProperty) else other)
    
    def __rdivmod__(self, other):
        return self.value.__rdivmod__(other.value if isa(other, FreeProperty) else other)
    
    def __rpow__(self, other):
        return self.value.__rpow__(other.value if isa(other, FreeProperty) else other)
    
    def __rlshift__(self, other):
        return self.value.__rlshift__(other.value if isa(other, FreeProperty) else other)
    
    def __rrshift__(self, other):
        return self.value.__rrshift__(other.value if isa(other, FreeProperty) else other)
    
    def __rand__(self, other):
        return self.value.__rand__(other.value if isa(other, FreeProperty) else other)
    
    def __rxor__(self, other):
        return self.value.__rxor__(other.value if isa(other, FreeProperty) else other)
    
    def __ror__(self, other):
        return self.value.__ror__(other.value if isa(other, FreeProperty) else other)
    
    def __iadd__(self, other):
        self.value = self.value.__add__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __isub__(self, other): 
        self.value = self.value.__sub__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __imul__(self, other): 
        self.value = self.value.__mul__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __imatmul__(self, other):
        self.value = self.value.__matmul__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __itruediv__(self, other): 
        self.value = self.value.__truediv__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __ifloordiv__(self, other):
        self.value = self.value.__floordiv__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __imod__(self, other): 
        self.value = self.value.__mod__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __ipow__(self, other): 
        self.value = self.value.__pow__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __ilshift__(self, other):
        self.value = self.value.__lshift__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __irshift__(self, other):
        self.value = self.value.__rshift__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __iand__(self, other): 
        self.value = self.value.__and__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __ixor__(self, other): 
        self.value = self.value.__xor__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __ior__(self, other):
        self.value = self.value.__or__(other.value if isa(other, FreeProperty) else other)
        return self
    
    def __repr__(self):
        units = self._units
        if units: units = f' {units}'
        value = self.value
        try: value = format(value, '.5g')
        except: pass
        return f'<{self.name}: {value}{units}>'
    
    

import inspect
from dataclasses import dataclass

@dataclass(eq = True, frozen=True)
class Location:
    name : str
    position : str

    def __post_init__(self):
        if self.name == "":
            raise ValueError("Location name cannot be empty")


def auto_repr(cls):
	print(f"Decorating {cls.__name__} with auto_repr")
	members = vars(cls)
	
	if "__repr__" in members:
		raise TypeError(f"{cls.__name__} already defines __repr__")
		
	if "__init__" not in members:
		raise TypeError(f"{cls.__name__} does not overriide __init__")
		
	sig = inspect.signature(cls.__init__)
	parameter_names = list(sig.parameters)[1:]
	print(f"__init__ parameter names: ", parameter_names)
	
	if not all(
		isinstance(members.get(name, None), property)
		for name in parameter_names
	):
		raise TypeError(
			f"Cannot apply auto_repr to {cls.__name__} because not all "
			"__init__ parameters have matching properties"
		)
	
	def synthesized_repr(self):
		return "{typename}({args})".format(
			typename = type(self),
			args = ", ".join(
				"{name}={value!r}".format(
					name=name,
					value=getattr(self, name)
				) for name in parameter_names
			)
		)
		
	setattr(cls, "__repr__", synthesized_repr)
	return cls

# @auto_repr
# class Location:

#     def __init__(self, name, position):
#         self._name = name
#         self._position = position

#     @property
#     def name(self):
#         return self._name

#     @property	
#     def position(self):
#         return self._position

#     @classmethod
#     def foo(cls):
#         print(cls.__init__)
#         return 0
    	
#     def __str__(self):
#         return self.name

#     def __eq__(self, other):
#         if not isinstance(other, type(self)):
#             return NotImplemented
#         return (self.name == other.name) and (self.position == other.position)

#     def __hash__(self):
#         return hash((self.name, self.position))


maracaibo = Location("Maracaibo", "Coordinates of Maracaibo")
rotterdam = Location("Rotterdam", "Coordinates of Rotterdam")
stockholm = Location("Stockholm", "Coordinates of Stockholm")
capetown = Location("Cape Town", "Coordinates of Cape Town")
hongkong = Location("Hong Kong", "Coordinates of Hong Kong")
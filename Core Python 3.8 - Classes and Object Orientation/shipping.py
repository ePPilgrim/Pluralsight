from operator import length_hint
from numpy import lexsort
import iso6346

class ShippingContainer:

    HEIGH_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial=str(serial).zfill(6)
            )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents = [], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents = list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial())

    @property
    def volume_ft(self):
        return self._calculate_volume_ft()

    def _caculate_volume_ft(self):
        return ShippingContainer.HEIGH_FT * ShippingContainer.WIDTH_FT * ShippingContainer.lenght_ft

class RefrigiratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial=str(serial).zfill(6),
            category="R"
            )

    def _calculate_volume_ft(self):
        return super()._caculate_volume_ft()- RefrigiratedShippingContainer.FRIDGE_VOLUME_FT
    
    def _set_celsius(self, value):
        if value > RefrigiratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

class HeatedRefrigiratedShippingContainer(RefrigiratedShippingContainer):

    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if value <= HeatedRefrigiratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature it too cold")
        super()._set_celsius(value)

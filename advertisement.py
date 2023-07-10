from base import BaseClass
from deal import Rent, Sale
from estate import Apartment, House, Store


class ApartmentRent(BaseClass, Apartment, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()


class ApartmentSale(BaseClass, Apartment, Sale):
    def __str__(self):
        return f"apartment:{self.user}\t address:{self.address}"

    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseSale(BaseClass, House, Sale):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreRent(BaseClass, Store, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()


class StoreSale(BaseClass, Store, Sale):
    def show_detail(self):
        self.show_description()
        self.show_price()

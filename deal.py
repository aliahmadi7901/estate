from abc import ABC


class Rent(ABC):
    def __init__(
            self, fixed_amount, monthly_amount, convertible=False,
            discountable=False, *args, **kwargs
    ):
        self.fixed_amount = fixed_amount
        self.monthly_amount = monthly_amount
        self.convertible = convertible
        self.discountable = discountable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"fixed_amount:{self.fixed_amount}\t"
              f" monthly_price:{self.monthly_amount}")


class Sale(ABC):
    def __init__(
            self, price_per_meter, discountable=False,
            convertible=False, *args, **kwargs
    ):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertible = convertible
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price_per_meter:{self.price_per_meter}")

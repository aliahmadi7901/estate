from sample import create_sample
from advertisement import ApartmentSale, ApartmentRent, HouseSale,\
    HouseRent, StoreSale, StoreRent


class Handler:
    ADVERTISEMENT_TYPE = {1: ApartmentSale, 2: ApartmentRent, 3: HouseSale,
                          4: HouseRent, 5: StoreSale, 6: StoreRent}

    SWITCHES = {'r': 'get_report', 's': 'show_all'}

    def get_report(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            print(f"{adv}".ljust(42), f"count: {adv.manager.count()}")

    def show_all(self):
        for adv in self.ADVERTISEMENT_TYPE.values():
            for obj in adv.object_list:
                print(f"{adv}, {obj.show_detail()}\n")

    def run(self):
        print('hello world')

        for key in self.SWITCHES:
            print(f"press:{key}\t for:{self.SWITCHES[key]}")

        user_input = input('please enter your choice:')

        if user_input not in ('r', 's'):
            print('invalid input... please try again.')
            self.run()

        if user_input == 'r':
            self.get_report()

        elif user_input == 's':
            self.show_all()


if __name__ == '__main__':
    create_sample()
    Handler().run()

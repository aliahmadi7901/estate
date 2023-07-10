from random import choice
from region import Region
from user import User
from advertisement import ApartmentSale, ApartmentRent, HouseSale, HouseRent,\
    StoreSale, StoreRent


FIRST_NAME = ['ali', 'reza', 'mohammad', 'ahmad', 'akbar']
LAST_NAME = ['ahmadi', 'rezaei', 'alipor', 'dastgerdi', 'hadadi']
MOBILES = [
    '09165421589', '09165812589', '09212584521',
    '091060605842', '09125821456'
           ]


def create_sample():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.object_list:
        print(f"{user.full_name()}")

    region_1 = Region(name='faz3')
    region_2 = Region(name='shahed')
    region_3 = Region(name='jahad')
    region_4 = Region(name='azadi')

    apartment_sale_1 = ApartmentSale(
        user=User.object_list[0], area=90, rooms_count=2, built_year=1398,
        region=region_1, address='faz3.molavi_1', has_elevator=True,
        has_parking=True, floor=3, price_per_meter='15/000/000'
    )
    apartment_sale_2 = ApartmentSale(
        user=User.object_list[1], area=110, rooms_count=2, built_year=1399,
        region=region_2, address='shahed.danesh5', has_elevator=True,
        has_parking=True, floor=2, price_per_meter='15/000/000'
    )
    apartment_rent_1 = ApartmentRent(
        user=User.object_list[2], area=100, rooms_count=2, built_year=1402,
        region=region_3, address='jahad.2', has_elevator=True,
        has_parking=True, floor=4, fixed_amount='200/000/000',
        monthly_amount='3/000/000'
    )
    apartment_rent_2 = ApartmentRent(
        user=User.object_list[3], area=89, rooms_count=2, built_year=1402,
        region=region_4, address='azadi.2', has_elevator=True,
        has_parking=True, floor=1, fixed_amount='150/000/000',
        monthly_amount='3/000/000'
    )
    house_sale_1 = HouseSale(
        user=User.object_list[4], area=150, rooms_count=3, built_year=1388,
        region=region_1, address='faz3.molavi_2', has_yard=True, floors_count=1,
        price_per_meter='14/000/000'
    )
    house_sale_2 = HouseSale(
        user=User.object_list[0], area=130, rooms_count=2, built_year=1382,
        region=region_2, address='shahed.danesh4', has_yard=True,
        floors_count=1, price_per_meter='13/000/000'
    )
    house_rent_1 = HouseRent(
        user=User.object_list[1], area=120, rooms_count=2, built_year=1392,
        region=region_3, address='jahad.1', has_yard=True, floors_count=1,
        fixed_amount='300/000/000', monthly_amount='2/000/000'
    )
    house_rent_2 = HouseRent(
        user=User.object_list[2], area=160, rooms_count=3, built_year=1380,
        region=region_4, address='azadi.2', has_yard=True, floors_count=1,
        fixed_amount='200/000/000', monthly_amount='2/000/000'
    )
    store_sale_1 = StoreSale(
        user=User.object_list[3], area=40, rooms_count=0,
        built_year=1382, region=region_1, address='faz3.molavi3',
        price_per_meter='100/000/000'
    )
    store_sale_2 = StoreSale(
        user=User.object_list[4], area=50, rooms_count=0,
        built_year=1378, region=region_2, address='shahed.danesh1',
        price_per_meter='110/000/000'
    )
    store_rent_1 = StoreRent(
        user=User.object_list[0], area=30, rooms_count=0,
        built_year=1390, region=region_3, address='jahad.5',
        fixed_amount='100/000/000', monthly_amount='10/000/000'
    )
    store_rent_2 = StoreRent(
        user=User.object_list[1], area=35, rooms_count=0,
        built_year=1400, region=region_4, address='azadi.5',
        fixed_amount='150/000/000', monthly_amount='12/000/000'
    )

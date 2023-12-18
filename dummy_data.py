import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from products.models import Product,Brand,Review
from faker import Faker

def seed_brand(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg']
    for x in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'photo_brand/{images[random.randint(0,8)]}',
        )
def seed_product(n):
    fake=Faker()
    flag_types=['New','Sale','Feature']
    brands=Brand.objects.all()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg']
    for x in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag_types[random.randint(0,2)],
            price=round(random.uniform(5.99,99.99),2),
            image=f'photo_product/{images[random.randint(0,8)]}',
            sku=random.randint(100,1000000),
            subtitle=fake.text(max_nb_chars=3000),
            description=fake.text(max_nb_chars=30000),
            brand=brands[random.randint(0,len(brands)-1)]

        )
#seed_brand(190)
seed_product(1200)




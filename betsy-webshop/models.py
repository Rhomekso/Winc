from peewee import *

database = SqliteDatabase("Betsy.db")

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    name = CharField()
    address  = CharField()
    billing_info = CharField()


class Product(BaseModel):
    name = CharField()
    description = TextField()
    price = DecimalField(decimal_places=2)
    quantity = IntegerField()
    user = ForeignKeyField(User, backref="products")

class Tag(BaseModel):
    name = CharField(unique=True)

class ProductTag(BaseModel):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)


class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref="transactions")
    product = ForeignKeyField(Product)


def initialize_database():
    with database:
        database.create_tables([User, Product, Tag, ProductTag, Transaction])


def populate_test_database():
    # checks if the database already contains any data
    if User.select().count() > 0:
        print("Database contains information.")
        return
    
    with database.atomic():
        # test Users
        user1 = User.create(name="Kratos", address="Midgard woods 50", billing_info="Bitcoin")
        user2 = User.create(name="Steven", address="Brooklynstreet 110", billing_info="Credit Card")
        user3 = User.create(name="Jason", address="Atlantis Avenue 52", billing_info="Paypal")
        user4 = User.create(name="Moana", address="Motunui Island", billing_info="IDEAL")
        user5 = User.create(name="Lara", address="Imperial Boulevard 501", billing_info="Imperial Credits")

        # test Products
        product1 = Product.create(name="Staff", description="Imperial Staff", price=15.99, quantity=12, user=user5)
        product2 = Product.create(name="Shield", description="Vibranium Shield", price=19.99, quantity=5, user=user2)
        product3 = Product.create(name="Bear Cloak", description="Winter Cloak", price=25.99, quantity=6, user=user1)
        product4 = Product.create(name="Sail Boat", description="Traveling Boat", price=45.99, quantity=2, user=user4)
        product5 = Product.create(name="Fish Talker", description="Fish Translator", price=35.99, quantity=7, user=user3)

        # test Tags
        tag_names = ["Weapons", "Gadgets", "Accessories, Vehicles"]
        tags = []
        for name in tag_names:
            try:
                tag = Tag.create(name=name)
            except IntegrityError:
                tag = Tag.get(name=name)
            tags.append(tag)

        # Link Tags with the Products
        for tag in tags:
            if not ProductTag.select().where(ProductTag.product == product1, ProductTag.tag == tag).exists():
                ProductTag.create(product=product1, tag=tag)
            if not ProductTag.select().where(ProductTag.product == product2, ProductTag.tag == tag).exists():
                ProductTag.create(product=product2, tag=tag)
            if not ProductTag.select().where(ProductTag.product == product3, ProductTag.tag == tag).exists():
                ProductTag.create(product=product3, tag=tag)
            if not ProductTag.select().where(ProductTag.product == product4, ProductTag.tag == tag).exists():
                ProductTag.create(product=product4, tag=tag)
            if not ProductTag.select().where(ProductTag.product == product5, ProductTag.tag == tag).exists():
                ProductTag.create(product=product5, tag=tag)

    print("Test Database inserted succesfully.")

if __name__ == "__main__":
    initialize_database()
    populate_test_database()
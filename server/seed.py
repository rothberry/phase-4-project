from app import app
from models import db, Property
from faker import Faker

# db.init_app(app)

with app.app_context():
    
    print("Deleting tables...")
    Property.query.delete()


    p1 = Property(address="1656 E 1700 N", city="Albequerqeue", state="NM", image="image1.png", bedrooms=4, bathrooms=3, floors=2, garage=True, pool=False)
    db.session.add(p1)
    p2 = Property(address="838 Mt. Rd", city="Logan", state="UT", image="image2.png", bedrooms=6, bathrooms=3, floors=2, garage=True, pool=False)
    db.session.add(p2)
    p3 = Property(address="123 E 200 N", city="Welsh", state="WV", image="image3.png", bedrooms=4, bathrooms=2, floors=3, garage=False, pool=False)
    db.session.add(p3)
    
    db.session.commit()

    print("Properties seeded...")
    

    
from sqlalchemy_sample import *

myUser = User(id=100, name="とも", age=3000)
session.add(myUser)
session.commit()

print(myUser)
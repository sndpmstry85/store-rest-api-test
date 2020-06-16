from db import db


class UserModel (db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # ID column is a integer with primary key
    username = db.Column(db.String(80))  # username is a string with max characters 80
    password = db.Column(db.String())  # password is a string with no limit

    def __init__(self, username, password):  # init method we define the username and password properties
        self.username = username  # store these defined in the object
        self.password = password

    def save_to_db(self):  # save to our database adding and commiting
        db.session.add(self)
        db.session.commit()

    @classmethod  # class method to find by username and find by ID
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()  # gets the 1st username

    @classmethod  # class method to find by username and find by ID
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  # gets the first ID


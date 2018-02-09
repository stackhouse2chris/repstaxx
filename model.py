from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///repsource.db', echo=False)
Base = declarative_base(engine)
########################################################################


class Customer(Base):

    """"""
    __tablename__ = 'customers'

    customer_id = Column(String, primary_key=True)
    customer_name = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

    def __init__(self, customer_id, customer_name, address1, address2, city, state, zipcode):
        """"""
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zipcode

    def __repr__(self):
        """"""
        return "{0}: {1}".format(self.customer_id, self.customer_name)


class Vendor(Base):

    """"""
    __tablename__ = 'vendor'

    vendor_id = Column(String, primary_key=True)
    vendor_name = Column(String)
    vendor_contact = Column(String)
    vendor_address1 = Column(String)
    vendor_address2 = Column(String)
    vendor_city = Column(String)
    vendor_state = Column(String)
    vendor_zip = Column(String)
    vendor_phone = Column(String)
    vendor_email = Column(String)
    vendor_fax = Column(String)
    vendor_principal = Column(String)

    def __init__(self, vendor_id, vendor_name, vendor_contact, vendor_address1, vendor_address2, vendor_city,
                 vendor_state, vendor_zip, vendor_phone, vendor_emaail, vendor_fax, vendor_principal):
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.vendor_contact = vendor_contact
        self.vendor_address1 = vendor_address1
        self.vendor_address2 = vendor_address2
        self.vendor_city = vendor_city
        self.vendor_state = vendor_state
        self.vendor_zip = vendor_zip
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_emaail
        self.venndor_fax = vendor_fax
        self.vendor_principal = vendor_principal

    def __repr__(self):
        return "{0}: {1}".format(self.vendor_id, self.vendor_name)


def loadSession():
    """"""
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    session = loadSession()
    res = session.query(Vendor).all()
    print("{0}:\n {1}\n {2}\n {3} {4}, {5}".format(res[200].vendor_id, res[200].vendor_name, res[200].vendor_address1,
                                                   res[200].vendor_city, res[200].vendor_state, res[200].vendor_zip))

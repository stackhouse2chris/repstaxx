import model


class Customer:

    customer = model.Customer
    session = model.loadSession()
    res = session.query(customer).all()

    def __init__(self):
        pass

    @staticmethod
    def get_cust_ids():
        ids = []
        for item in Customer.res:
            ids.append(item.customer_id)
        return ids

    @staticmethod
    def get_cust_info(customer_id):
        session = model.loadSession()
        for result in session.query(model.Customer).filter(model.Customer.customer_id == customer_id):
            return result.customer_name, result.address1, result.address2, result.city, result.state, result.zip
        session.close()

    @staticmethod
    def get_cust_names():
        names = []
        for item in Customer.res:
            names.append(item.customer_name)
        return names


class Vendor:

    vendor = model.Vendor
    session = model.loadSession()
    res = session.query(vendor).all()

    @staticmethod
    def get_principal_vendors():
        principals = []
        for item in Vendor.res:
            if item.vendor_principal == 'TRUE':
                principals.append(item.vendor_name)
        return principals

    @staticmethod
    def get_vendor_ids():
        vendors = []
        for item in Vendor.res:
            vendors.append(item.vendor_id)
        return vendors

    @staticmethod
    def auto_complete(text):
        vendors = []
        selection = Vendor.session.query(Vendor.vendor).filter(Vendor.vendor.vendor_id.like(str(text)))
        for item in selection:
            vendors.append(item)
        return vendors

    @staticmethod
    def get_vendor_info(vendor):
        session = model.loadSession()
        for result in session.query(model.Vendor).filter(model.Vendor.vendor_id == vendor):
            return result.vendor_id, result.vendor_name, result.vendor_address1, result.vendor_address2, result.vendor_city, result.vendor_state, result.vendor_zip
        session.close()


if __name__ == '__main__':
    print(Vendor.get_principal_vendors())

import sqlite3

conn = sqlite3.connect('chinook.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

sql = '''
select FirstName, CustomerId, LastName from customers;
'''

cur.execute(sql)

results = cur.fetchall()
conn.close()


# def get_full_name(obj):
#     return f"{obj['FirstName']} {obj['LastName']}"

#
# for customer in results:
#     print(get_full_name(customer))
    # print(f"{customer['CustomerId']} {customer['FirstName']} {customer['LastName']}")


class Customer:
    def __init__(self, **kwargs):
        # self.first_name = first_name
        # self.last_name = last_name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_full_name(self):
        return f"{self.FirstName} {self.LastName}"

    def save(self):
        conn = sqlite3.connect('chinook.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        sql = f"""
        UPDATE customers
        SET 
            FirstName = '{self.FirstName}', 
            LastName = '{self.LastName}'
        WHERE 
            CustomerId = {self.CustomerId};
        """

        cur.execute(sql)

        conn.commit()
        conn.close()

    def fetch(self):
        pass


customers = [
    Customer(**data) for data in results
]

breakpoint()

for customer in customers:
    print(customer.get_full_name())
# c1 = Customer(first_name='F', last_name='L', age=30)
# print(c1.get_full_name())
# print(c1.first_name)
# print(c1.last_name)
'''
ORM - Object Relational Mapping
'''
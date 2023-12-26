import pandas
from abc import ABC,abstractmethod
df = pandas.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod    #decorator that converts the method to a class where the method is related to a class but not an instance
    def get_hotel_count(cls, data):
        return len(data)
    def __eq__(self,other):     #magic metjod; doesnt do anything to the program here
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):

    @abstractmethod #see note below
    def generate(self):
        pass
class ReservationTicket(Ticket):    #requires to call and execute generate function
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name=name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount*1.2

hotel1=Hotel(hotel_id="188")
hotel2=Hotel(hotel_id="134")

print(hotel1.available())

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="john smith  ",hotel_object=hotel1)
print(ticket.the_customer_name) #the property decorator allows to access as a normal parameter instead of an instance variable
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)

#Abstract classes are used when all the methods require a particular function to generate
#
#




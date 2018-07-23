class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.current_status_message = None

s = Spy("Nitish" , "Mr" , 20 , 4.5)
friend1 = Spy('ram' , 'mr' , 20 , 4.3)
friend2 = Spy('shyam' , 'mr' , 20, 3.4)
friend3 = Spy('akash' , 'mr' , 20 , 4.2)
friends = [friend1 , friend2 , friend3]

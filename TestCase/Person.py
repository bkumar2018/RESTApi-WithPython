
class Person:
    def __init__(self,id1,email,first_name,last_name,avatar):
        self.id1 = id1
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    def getid(self):
        return self.id1
    def getemail(self):
        return self.email
    def getfirst_name(self):
        return self.first_name
    def getlast_name(self):
        return self.last_name
    def getavatar(self):
        return self.avatar

    def getAll(self):
        print("Person Id : "+ str(self.id1))
        print("Person email : "+self.email)
        print("Person FirstName : "+self.first_name)
        print("Person LastName : "+self.last_name)
        print("Person Avatar : "+self.avatar)
        print('....................................')


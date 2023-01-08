class Person:
    number_of_persons = 0
    def __init__(self,first_name,last_name,email_adresse="empty"):
        self.first_name = first_name
        self.last_name = last_name
        self.email_adresse = email_adresse
        self.__class__.number_of_persons+=1

    @classmethod
    def get_number_of_persons(cls):
        print(f"There are {cls.number_of_persons} persons")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

personOne = Person("Ida","Ingrid","Judith.Bornhaupt@hotmail.de")
print(personOne.get_full_name())
print(personOne.email_adresse)
personTwo = Person("Ida","Hallo")
print(personTwo.email_adresse)
Person.get_number_of_persons()



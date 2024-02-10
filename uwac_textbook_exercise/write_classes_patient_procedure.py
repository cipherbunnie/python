# Author: Vam
# Date: 14/01/2024

'''
Write a class named Patient that has attributes for the following data:
    First name
    last name
    Address
    Phone number
    Name and phone number of emergency contact
The Patient class's _init_ method should accept an argument for each attribute. 
The Patient class should also have accessor and mutator methods for each attribute.
Next, write a class named Procedure that represents a medical procedure that has been performed on a patient. 
The Procedure class should have attributes for the following data:
    Name of the procedure
    Date of the procedure
    Name of the practitioner who performed the procedure.
    Charges for the procedure
The Procedure class's _init_ method should accept an argument for each attribute. 
The Procedure class should also have accessor and mutator methods for each attribute.
Next, write a program that creates an instance of the Patient class, initialized with sample data.
Then, create three instances of the Procedure class, initialized with the following data:
Procedure name:    Physical Exam        X-ray               Blood test
Date:              Today's date         Today's date        Today's date
Practitioner:      Dr. Irvine           Dr. Jamison         Dr. Smith
Charge:            240                  650                 320

The program should display the patient's information, information about all three of the procedures,
and the total charges of the three procedures.
'''


'''
Class Patient:
    Method initialize(first_name, last_name, address, phone_number, emergency_contact):
        Set self.first_name to first_name
        Set self.last_name to last_name
        Set self.address to address
        Set self.phone_number to phone_number
        Set self.emergency_contact to emergency_contact

    Method get_first_name():
        Return self.first_name
    Method get_last_name():
        Return self.last_name
    Method get_address():
        Return self.address
    Method get_phone_number():
        Return self.phone_number
    Method get_emergency_contact():
        Return self.emergency_contact
    Method set_first_name(first_name):
        Set self.first_name to first_name
    Method set_last_name(last_name):
        Set self.last_name to last_name
    Method set_address(address):
        Set self.address to address
    Method set_phone_number(phone_number):
        Set self.phone_number to phone_number
    Method set_emergency_contact(emergency_contact):
        Set self.emergency_contact to emergency_contact

Class Procedure:
    Method initialize(name, date, practitioner, charge):
        Set self.name to name
        Set self.date to date
        Set self.practitioner to practitioner
        Set self.charge to charge

    Method get_name():
        Return self.name
    Method get_date():
        Return self.date
    Method get_practitioner():
        Return self.practitioner
    Method get_charge():
        Return self.charge
    Method set_name(name):
        Set self.name to name
    Method set_date(date):
        Set self.date to date
    Method set_practitioner(practitioner):
        Set self.practitioner to practitioner
    Method set_charge(charge):
        Set self.charge to charge
        
# Create an instance of the Patient class
patient = Patient("John", "Doe", "123 Main St", "555-1234", "Jane Doe (555-5678)")

# Create three instances of the Procedure class
procedure1 = Procedure("Physical Exam", "Today's date", "Dr. Irvine", 240)
procedure2 = Procedure("X-ray", "Today's date", "Dr. Jamison", 650)
procedure3 = Procedure("Blood test", "Today's date", "Dr. Smith", 320)

# Display patient information
Output "Patient Information:"
Output "First Name:", patient.get_first_name()
Output "Last Name:", patient.get_last_name()
Output "Address:", patient.get_address()
Output "Phone Number:", patient.get_phone_number()
Output "Emergency Contact:", patient.get_emergency_contact()

# Display information about the three procedures
Output "\nProcedure Information:"
Output "1. Name:", procedure1.get_name()
Output "   Date:", procedure1.get_date()
Output "   Practitioner:", procedure1.get_practitioner()
Output "   Charge:", procedure1.get_charge()

Output "\n2. Name:", procedure2.get_name()
Output "   Date:", procedure2.get_date()
Output "   Practitioner:", procedure2.get_practitioner()
Output "   Charge:", procedure2.get_charge()

Output "\n3. Name:", procedure3.get_name()
Output "   Date:", procedure3.get_date()
Output "   Practitioner:", procedure3.get_practitioner()
Output "   Charge:", procedure3.get_charge()

# Calculate and display total charges
total_charges = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()
Output format("Total Charges for the Three Procedures:" with total_charges)
'''


class Patient:
    # __init__ method
    def __init__(self, first_name, last_name, address, phone_number, emergency_contact):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.emergency_contact = emergency_contact

    # Accessor methods
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_address(self):
        return self.address
    def get_phone_number(self):
        return self.phone_number
    def get_emergency_contact(self):
        return self.emergency_contact

    # Mutator methods
    def set_first_name(self, first_name):
        self.first_name = first_name
    def set_last_name(self, last_name):
        self.last_name = last_name
    def set_address(self, address):
        self.address = address
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    def set_emergency_contact(self, emergency_contact):
        self.emergency_contact = emergency_contact


class Procedure:
    # __init__ method
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # Accessor methods
    def get_name(self):
        return self.name
    def get_date(self):
        return self.date
    def get_practitioner(self):
        return self.practitioner
    def get_charge(self):
        return self.charge

    # Mutator methods
    def set_name(self, name):
        self.name = name
    def set_date(self, date):
        self.date = date
    def set_practitioner(self, practitioner):
        self.practitioner = practitioner
    def set_charge(self, charge):
        self.charge = charge


# Create an instance of the Patient class
patient = Patient("John", "Doe", "123 Main St", "555-1234", "Jane Doe (555-5678)")

# Create three instances of the Procedure class
procedure1 = Procedure("Physical Exam", "Today's date", "Dr. Irvine", 240)
procedure2 = Procedure("X-ray", "Today's date", "Dr. Jamison", 650)
procedure3 = Procedure("Blood test", "Today's date", "Dr. Smith", 320)

# Display patient information
print("Patient Information:")
print("First Name:", patient.get_first_name())
print("Last Name:", patient.get_last_name())
print("Address:", patient.get_address())
print("Phone Number:", patient.get_phone_number())
print("Emergency Contact:", patient.get_emergency_contact())

# Display information about the three procedures
print("\nProcedure Information:")
print("1. Name:", procedure1.get_name())
print("   Date:", procedure1.get_date())
print("   Practitioner:", procedure1.get_practitioner())
print("   Charge:", procedure1.get_charge())

print("\n2. Name:", procedure2.get_name())
print("   Date:", procedure2.get_date())
print("   Practitioner:", procedure2.get_practitioner())
print("   Charge:", procedure2.get_charge())

print("\n3. Name:", procedure3.get_name())
print("   Date:", procedure3.get_date())
print("   Practitioner:", procedure3.get_practitioner())
print("   Charge:", procedure3.get_charge())

# Calculate and display total charges
total_charges = procedure1.get_charge() + procedure2.get_charge() + procedure3.get_charge()
print("\nTotal Charges for the Three Procedures: ${:.2f}".format(total_charges))
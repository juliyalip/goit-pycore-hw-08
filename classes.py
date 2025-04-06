from collections import UserDict
import re
from datetime import datetime, timedelta
from validations import is_valid_date_format
from decorators import contact_error, name_error, InvalidPhoneError, InvalidNameError


class Phone:
    def __init__(self, phone):
        self.value = phone
    
    def is_valid(self):
        pattern = r"^\d{10}$"
        if re.match(pattern, str(self.value)):
            return True
        else:
            return False
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value

#-----------------------------------------------------------------------------------------

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# -------------------------------------------------------------------------------------
class Name:
    def __init__(self, name: str):
        if len(name) < 3:
            raise InvalidNameError("The name must be more than 2 letters.")
        if not name.isalpha():
            raise InvalidNameError("The name must contain only letters.")
        self.value = name
    
    def __str__(self):
        return self.value
    
#-------------------------------------------------

class Birthday(Field):
    def __init__(self, value):
        self.birthday = value 
    
    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, date_str):
        if not is_valid_date_format(date_str):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        day, month, year = date_str.split('.')
       
        try:
            self.__birthday = datetime(int(year), int(month), int(day))
            
        except ValueError:
            raise ValueError("Invalid date. Please write the corect date")
        
    def to_datetime(self):
        return self.__birthday 
    
    def __str__(self):
        return f"{self.__birthday}"
    

# ----------------------------------------------------------------------------------   

class Record: 
    @name_error
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones =[]
        self.birthday=None

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone.is_valid():
           self.phones.append(new_phone)
        else:
        #    print( "The phone mast be 10 letters")
             raise InvalidPhoneError("The phone mast be 10 letters")
            
    def add_birthday(self, br_day):
        try:
            new_br_day = Birthday(br_day)
            self.birthday = new_br_day
            return True
        except ValueError:
          #  print(f"invalid date format")
            return False

   

    def edit_phone(self, old_phone, new_phone):
        valid_new_phone = Phone(new_phone)
        if valid_new_phone.is_valid():
             for phone in self.phones:
                if phone.value == old_phone:
                   phone.value =  new_phone
        else:
          #  print( "The phone mast be 10 letters")
           raise InvalidPhoneError("The phone mast be 10 letters")
         
    def find_phone(self, found_phone):
        for phone in self.phones:
            if phone.value == found_phone:
                 print(f"{self.name.value}: {found_phone}")
                
    def __str__(self):
         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}" 
   
# -------------------------------------------------------------------

class AddressBook(UserDict):
    def __init__(self):
        self.data={}
        

    def add_record(self, record):
        self.data[record.name.value] = record

    
    def find(self, contact_name):
        contact = self.data.get(contact_name)
        return contact if contact else None

    @contact_error          
    def delete(self, contact_name):
        for name, _ in self.data.items():
            if name == contact_name:
                del self.data[name]
                return f"contact {name} was deleted"
            raise KeyError
    
    def __repr__(self):
        if not self.data:
            return "You don't have contacts yet"

        return '\n'.join(f"{name}: {record}" for name, record in self.data.items() )
    

    def get_upcoming_birthdays(self):
        upcoming_birthdays =[]
        current_date = datetime.today().date()
        future_date = current_date + timedelta(days=7)

        for key, record in self.data.items():
            if record.birthday:
                user_birthday = record.birthday.birthday.date()  

                if user_birthday.replace(year=current_date.year) < current_date:
                    user_birthday = user_birthday.replace(year = current_date.year + 1)
                else:
                    user_birthday = user_birthday.replace(year=current_date.year)

                    if current_date <= user_birthday <= future_date:
                        day_of_week = user_birthday.weekday()
                        
                        if day_of_week < 5:
                            congratulation_date = user_birthday
                        else:
                            congratulation_date = user_birthday + timedelta(days=(7-day_of_week))
                        
                        holliday_user = {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                    }
                        upcoming_birthdays.append(holliday_user)     
        return upcoming_birthdays if upcoming_birthdays else "There are no birthdays in the next week."



    
  
  
 
  
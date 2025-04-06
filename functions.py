from decorators import input_error, contact_error, date_error, InvalidNameError, InvalidPhoneError
from classes import AddressBook, Record, Phone, Name

def parse_input(user_input):
    print("Raw user input:", user_input)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    print("Parsed cmd:", cmd)
    print("Parsed args:", args)
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    if not Name(name):
        raise InvalidNameError("The name must be more than 2 letters and only letters")
    if not Phone(phone).is_valid():
        raise InvalidPhoneError ("The phone mast be 10 letters")
        
    record = book.find(name)
    message = "Contact updated."
   
    
    if record is None:
        record = Record(name)
    
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message


@contact_error
def change_contact(args, book: AddressBook):
   if len(args) == 3:
       name, old_number, new_number = args 
   else:
       return "Give me a name, an old and a new numbers, please."
   
   if not Phone(new_number).is_valid():
        raise ValueError    
   record = book.find(name)
   if not record:
        raise KeyError
   if old_number not in [phone.value for phone in record.phones]:
       raise ValueError
   record.edit_phone(old_number, new_number)
   return "Contact updated."


@input_error
@contact_error
def show_phone(args, book: AddressBook):
    name = args[0]
    return book[name] 

@date_error
def add_birthday(args, book: AddressBook):
    if len(args)<2:
        return("Give me a name and a date of birthday, please.")
    name, date_br, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError
    if not record.add_birthday(date_br):
        raise ValueError
    
    return "The date was added"
    
@input_error
@contact_error
def show_birthday(args, book: AddressBook):
    name=args[0]
    if name not in book:
        raise KeyError
    birthday = book[name].birthday
    if birthday:
      birthday =  birthday.to_datetime()
      return birthday.strftime("%d.%m.%Y") 
    else:
        return "The birthday is not set" 
    
@contact_error
def delete_contact(args, book: AddressBook):
    name = args[0] 
    return book.delete(name)



    
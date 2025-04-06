class InvalidPhoneError(ValueError):
    pass


class EmptyFileError(Exception):
    pass

class InvalidNameError(ValueError):
    pass



def name_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidNameError as e:
           print (f"The name has to be more than 2 letters" ) 
           return None
    return inner

   

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidNameError as e:
            return "The name has to be more than 2 letters and only letters"
        except ValueError:
            return "Give me a name and a phone please."
        except InvalidPhoneError as e:
            return "The phone mast be 10 letters"
        
    return inner

def contact_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError: 
            return "The contact is not found"
        except IndexError:
            return "Give a valid name"
        except ValueError:
            return "Give a valid phone number please"
    return inner


def date_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide the correct data. Use DD.MM.YYYY"
        except KeyError:
            return "The contact is not found"
    return inner

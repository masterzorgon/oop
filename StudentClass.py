

class Student:

    # `dob` is formated as "02/07/2001"
    def __init__(self, id, name, dob, classification):
        self.id = id or None
        self.name = name or None
        self.dob = dob or None
        self.classification = classification or None
        self.age = None
        self.registration_date = None
    
    current_year = 24
    
    # calculate age given `dob`
    def set_age(self):
        if self.dob:
            dob_year, dob_month, dob_day = map(int, self.dob.split('/'))
            current_month = 2  # Assuming the current month is February
            current_day = 29  # Assuming the current day is the 29th of February
            age = self.current_year - dob_year
            if dob_month > current_month or (dob_month == current_month and dob_day > current_day):
                age -= 1
            self.age = age
        else:
            return None
    
    def set_registration_date(self):
        if self.classification == "Sr":
            self.registration_date = "4/1 thru 4/3"
        elif self.classification == "Jr":
            self.registration_date = "4/4 thru 4/6"
        elif self.classification == "S":
            self.registration_date = "4/7 thru 4/9"
        else:
            self.registration_date = "4/10 thru 4/12"
    

    def get_age(self):
        return self.age
    
    def get_registration_date(self):
        return self.registration_date
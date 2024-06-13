class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):

        #instantiate band with a name
        if isinstance(name, str) and len(name) > 0:  #names are change-able/mutable strings
            self._name = name
        else:
            raise ValueError("Band name must be a non-empty string")
        
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):

        #instantiate band with a hometown
        if  not isinstance(hometown, str) and len(hometown) > 0:
            raise ValueError('Band homwtown must be a non-empty string')  #hometowns are unchange-able/immutable strings
        if hasattr(self, '_hometown'):
            raise AttributeError('Band hometown cannot be changed')
        self._hometown = hometown


    def concerts(self):

        #concert must be a type of concert
        return [concert for concert in Concert.all if concert.band == self]

    def venues(self):
        return list({concert.venue for concert in self.concerts()})

    def play_in_venue(self, venue, date):

        #create and return a new concert for a band"
        return Concert(date, self, venue)

    def all_introductions(self):

        #return all instructions for the band
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    all = []

    #initializing a concert by date
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):

        #dates are mutable/change-able strings
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Concert date must be a non-empty string")
        
    @property
    def venue(self):
        return self._venue
    
    @venue.setter

    #initialize a concert with a venue
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise ValueError("Concert venue must be of type Venue")
        self._venue = venue

    @property
    def band(self):
        return self._band
    
    @band.setter

    #initializing concert with a band
    def band(self, band):
        if not isinstance(band, Band):
            raise ValueError("Concert band must be of type Band")
        self._band = band

    def hometown_show(self):

        #return True if concert is in band's hometown, False if otherwise
        return self.band.hometown == self.venue.city

    def introduction(self):

        #return a string with the band's introduction for this concert
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
         
         #venue is instantiated witha name
         if isinstance(name, str) and len(name) > 0:
            self._name = name
         else:
            raise ValueError("Venue name must be a non-empty string")
         
    @property
    def city(self):
        return self._city
    
    #cities are mutable/change-able strings

    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city) > 0:
            self._city = city
        else:
            raise ValueError("City name must be a non-empty string")

    def concerts(self):

        #concerts must be of type concerts
        return [concert for concert in Concert.all if concert.venue == self]

    def bands(self):

        #venue has many bands
        return list({concert.band for concert in self.concerts()})
    
    def concert_on(self, date):

        #return the first concert on that date or None if no concerts exist
        return next((concert for concert in self.concerts() if concert.date == date), None)
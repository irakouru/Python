class Band:

    def __init__(self, band_name, music_genre, active):
        self.band_name = band_name
        self.music_genre = music_genre
        self.active = active
        self.number_of_gold_records = 5
        self.number_of_platinum_records = 0

    
    def __str__(self):
        return f"The name of the band is {self.band_name}. The music genre of the band is {self.music_genre}."

    def is_active(self):
        if self.active == True:
            print(f"{self.band_name} is active.")
        elif self.active == False:
            print(f"{self.band_name} is not active.")
        else:
            print("The value given to the attribute 'active' is not boolean.")


band = Band("ABBA", "Pop", False)
print(band.__str__())
band.is_active()

'''    def set_number_of_gold_records(self, number_of_gold_records):
        self.number_of_gold_records = number_of_gold_records

    
    def set_number_of_platinum_records(self, number_of_platinum_records):
        self.number_of_platinum_records = number_of_platinum_records


class CoverBand(Band):

    def __init__(self, band_name, music_genre, active, covered_bands_and_performers):
        super().__init__(band_name, music_genre, active)
        self.covered_bands_and_performers = covered_bands_and_performers

    def get_list_of_covered_artists(self):
        list_of_covered_bands = []
        for band in self.covered_bands_and_performers:
            list_of_covered_bands.append(band.band_name)
        return list_of_covered_bands

adele = Band("Adele", "Pop", True)
abba = Band("ABBA", "Pop", False)
metallica = Band("Metallica", "Heavy metal", True)

cover_band = CoverBand("Cats", "Pop", True, [adele, abba, metallica])
print(cover_band.__str__())
cover_band.is_active()
covered_bands = cover_band.get_list_of_covered_artists()

print(f"The covered bands and performers are: {covered_bands}")


    def get_list_of_covered_artists(self):
        #print("Covered bands and performers:")
        #for i in self.covered_bands_and_performers:
            #print(i)
        return self.covered_bands_and_performers'''

"""band = Band("ABBA", "Pop", False)
band.set_number_of_gold_records(3)
band.set_number_of_platinum_records(2)
print(f"The number of gold records: {band.number_of_gold_records}")
print(f"The number of platinum records: {band.number_of_platinum_records}")"""



"""print(band.band_name)
print(band.music_genre)
print(band.__str__())
band.is_active()

new_band = Band("Slipknot", "Nu metal", True)
print(new_band.__str__())
new_band.is_active()"""


"""def describe_band(self):
    print(f"The name of the band is {self.band_name}.")
    print(f"The music genre of the band is {self.music_genre}.")"""
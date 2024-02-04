"""Please write a class named Series with the following functionality:

The constructor should take the title, the number of seasons and a list of genres for the series as 
its arguments.

Hint: whenever you need to produce a string from a list containing strings, with a separating character 
of your choice in between the entries, you can use the join method as follows:

Please implement the method rate(rating: int) which lets you add a rating between 0 and 5 to any series 
object. You will also need to adjust the __str__ method so that in case there are ratings, the method 
prints out the number of ratings added, and their average rounded to one decimal point.

Please implement these two functions which allow you to search through a list of series: 
minimum_grade(rating: float, series_list: list) and includes_genre(genre: str, series_list: list)."""

class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.rate_average = 0 

    def __str__(self):
        genre_string = ", ".join(self.genres)
        rating_sum = 0
        rating_counter = 0
        if len(self.ratings) != 0:
            for rating in self.ratings:
                rating_sum += rating
                rating_counter += 1
            average = rating_sum / rating_counter
            return f"{self.title} ({self.seasons} seasons)\nGenres: {genre_string}\n{rating_counter} ratings, average {average} points" 
        else:
            return f"{self.title} ({self.seasons} seasons)\nGenres: {genre_string}\nno ratings"
    
    def get_average(self):
        rating_sum = 0
        rating_counter = 0
        if len(self.ratings) != 0:
            for rating in self.ratings:
                rating_sum += rating
                rating_counter += 1
            self.rate_average = rating_sum / rating_counter
            return self.rate_average
        else:
            print("No ratings.")

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Please enter a value between 0 and 5.")

def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:
        if series.get_average() >= rating:
            result.append(series)
    return result


def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genres:
            result.append(series)
    return result


dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
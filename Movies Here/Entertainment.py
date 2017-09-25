import fresh_tomatoes
import media

Despicable = media.Movie("Despicable Me","Despicable Me is a 2010 American 3D computer-animated comedy film from Universal Pictures and Illumination Entertainment that was released on July 9, 2010, in the United States.","https://www.uphe.com/sites/default/files/2015/04/Despicable-Me-Gallery-20.jpg","https://www.youtube.com/watch?v=TZkAcKCFIVo")
Gardians = media.Movie("Guardians of the Galaxy","Guardians of the Galaxy is a 2014 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios","https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=d96cjJhvlMA")
IceAge =  media.Movie("Ice Age: Collision Course","Manny, Sid and Diego and the rest of the gang team up with Buck to prevent asteroids from striking the Earth after Scrat accidentally sets off a chain of events in space.","https://image.tmdb.org/t/p/w500/zpaQwR0YViPd83bx1e559QyZ35i.jpg","https://www.youtube.com/watch?v=HyLquKn3Swc")

movies = [Despicable,Gardians,IceAge]
fresh_tomatoes.open_movies_page(movies)
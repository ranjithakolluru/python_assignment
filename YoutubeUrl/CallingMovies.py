import MoviesClass
import openhtml

Bahubali=MoviesClass.movies("Bahubali",'story of war love','https://www.youtube.com/watch?v=qD-6d8Wo3do','https://www.desiretrees.in/wp-content/uploads/2017/02/Baahubali-2-New-Poster-Maha-Shivaratri.jpg')
Antman=MoviesClass.movies("Antman","story of the man becoming a marvel hero","https://www.youtube.com/watch?v=IEVE3KSKQ0o","http://cdn2-www.superherohype.com/assets/uploads/2015/05/antman.jpg")

movies = [Bahubali,Antman]

openhtml.open_movies_page(movies)
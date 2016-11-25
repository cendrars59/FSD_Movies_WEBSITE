

# Dependecies import 
import movie 
import fresh_tomatoes


# Movies initialization 
ghost = movie.Movie ("Ghost in the shell","Weird story .....","https://youtu.be/G4VmJcZR0Yg","http://www.journaldugeek.com/wp-content/blogs.dir/1/files/2016/01/ghost-in-the-shell.jpg")
blade = movie.Movie ("Balde Runner","Story of ....","https://youtu.be/NoAzpa1x7jU","http://www.ecranlarge.com/uploads/image/000/945/blade-runner-photo-affiche-blade-runner-945067.jpg")
tron  = movie.Movie ("Tron","A story of a guy lost in a computer","https://youtu.be/3efV2wqEjEY","http://fr.web.img3.acsta.net/medias/nmedia/18/68/46/16/19028526.jpg")

# Creating the movies list 
movies = [ghost,blade,tron]


# launching the opening of the website 
fresh_tomatoes.open_movies_page(movies)



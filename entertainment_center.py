import media
import fresh_tomatoes
#
#   Wizard of Oz
#
wizard_of_oz = media.Movie("Wizard of Oz",
        "Young girl and dog's adventures in the Land of Oz",
        "http://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Wizard_of_Oz_FilmPoster.jpeg/220px-Wizard_of_Oz_FilmPoster.jpeg",
        "https://www.youtube.com/watch?v=VNugTWHnSfw")
#
#   From Russia With Love
#
fromrussiawithlove = media.Movie("From Russia With Love",
                     "James Bond and female Russian agent fight Spectre",
                     "http://upload.wikimedia.org/wikipedia/en/a/ad/From_Russia_with_Love_%E2%80%93_UK_cinema_poster.jpg",
                    "https://www.youtube.com/watch?v=VqAOf66o1Wg")
#
#   Interstellar
#
interstellar = media.Movie("Interstellar",
        "A crew of astronauts travel through a wormhole in search of new home for humanity",
        "http://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
        "https://www.youtube.com/watch?v=zSWdZVtXT7E")
#
#   Babe
#
babe = media.Movie("Babe",
                     "Story of a pig who wants to be a sheepdog",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Babe_ver1.jpg/215px-Babe_ver1.jpg",
                    "https://www.youtube.com/watch?v=yuzXPzgBDvo")
#
#   Tarzan and his mate
#
tarzan_and_his_mate = media.Movie("Tarzan and His Mate",
                     "Men of a safari try to convice Tarzan's mate to return to civilization",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/6/68/Tarzan_and_His_Mate.jpg/220px-Tarzan_and_His_Mate.jpg",
                    "https://www.youtube.com/watch?v=DzfmnGMlzFA")
#
#   Sound of Music
#
sound_of_music = media.Movie("The Sound of Music",
                  "Austrian woman studying to be a nun becomes governess to 7 children of naval officer",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/c/c6/Sound_of_music.jpg/220px-Sound_of_music.jpg",
                  "https://www.youtube.com/watch?v=KuWsQSntFf0")
#
#   Star Trek
#
star_trek = media.Movie("Star Trek",
                  "USS Enterprise faces Nero",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/2/29/Startrekposter.jpg/220px-Startrekposter.jpg",
                  "https://www.youtube.com/watch?v=4cZCCsW94LY")
#
#   Casablanca
#
casablanca = media.Movie("Casablanca",
                  "American expatriate falls in love with wife of Czech Resistence leader",
                  "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/CasablancaPoster-Gold.jpg/225px-CasablancaPoster-Gold.jpg",
                  "https://www.youtube.com/watch?v=BZtWRRa_8I0")
movies = [wizard_of_oz, fromrussiawithlove,interstellar,babe,tarzan_and_his_mate,
          sound_of_music,star_trek,casablanca]
fresh_tomatoes.open_movies_page(movies)

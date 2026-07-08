from enum import Enum
from dataclasses import dataclass

class Genres(Enum):
    Action = 1
    Adventure = 2
    Comedy = 3
    Mystery = 4
    Fantasy = 5
    Horror = 6
    Romance = 7
    Sci_Fi = 8
    Isekai = 9
    Slice_of_Life = 10
    Mecha = 11
    Yaoi = 12
    Yuri = 13
    Harem = 14
    Hentai = 99

class Rating(Enum):
    Dogshit = 0
    Meh = 1
    Mid = 2
    Not_Bad = 3
    Great = 4
    Amazing = 5
    Off_the_charts = 6

@dataclass
class AnimeObject:
    "Just a simple way to store Anime info. NO DON'T YOU DARE TAKE THIS OUT OF CONTEXT!"
    def __init__(
        self,
        name: str,
        genres: list[Genres],
        rating: Rating,
        episodes: int,
        comments: str
    ):
        """Still just a Init function..."""
        self.name = name
        self.genres = genres
        self.rating = rating
        self.episodes = episodes
        self.comments = comments
    
    def __repr__(self) -> str:
        """Easy way to just print out all of the info. If your are lazy."""
        genre_string = ", ".join(g.name for g in self.genres)
        return (
            f"Anime: {self.name}\n"
            f"Genres: {genre_string}\n"
            f"Rating: {self.rating.name}\n"
            f"Episodes: {self.episodes}\n"
            f"Comments: {self.comments}"
        )
    
class Anime:
    """Man... Don't ask me why I made this..."""
    def __init__(self) -> None:
        """What do you think a Init function will do?"""
        self.genres = Genres
        self.rating = Rating
        self.animes: dict[str, AnimeObject] = {}
    
    def create(self, name:str, genres:list[Genres], rating:Rating, episodes:int, comments:str):
        """
        Creates a Anime Object that is stored in a list and is referenceable later. It's that simple.
        Args:
            name: The title of the anime, dumbass.
            genres: A list of Genres enums describing the anime, please no hentai 🙏.
            rating: Your rating of the anime. Be honest about it, no one is going to see it anyways.
            episodes: The total number of episodes, don't you DARE put zero or negative episodes.
            comments: Additional notes or comments about the anime, you can put whatever here.
        Returns:
            AnimeObject: The newly created anime object. Don't take this out of context.
        Raises:
            ValueError: If an anime with the same name already exists or if you decided to put no or negative episodes.
            TypeError: If any argument has an invalid type.      
        """
        if episodes <= 0:
            raise ValueError("DUDE! I told you no zero or negative episodes.")
        if not isinstance(rating, Rating):
            raise TypeError("rating must be a Rating enum, and don't go creating your own.")
        if not all(isinstance(g, Genres) for g in genres):
            raise TypeError("genres must contain only Genres enums. Why are you getting enums wrong anyways?")
        if name in self.animes:
            raise ValueError(f'"{name}" already exists. Unfortunately no two anime can have the same name')
        anime = AnimeObject(name, genres, rating, episodes, comments)
        self.animes[name] = anime
        return anime
    
    def get(self, name: str) -> AnimeObject:
        """
        Gets a created AnimeObject. What more do you expect?

        Args:
            name: The anime to look up.

        Returns:
            AnimeObject: Btw, It just gives you all of the info listed-style.

        Raises:
            KeyError: If the anime doesn't exist. But with enough time, anything can be real!
        """
        return self.animes[name]
    
    def delete(self, name:str) -> None:
        """
        Deletes the AnimeObject specified. Goodbye soldier.

        Args:
            name: The anime to be execut- I mean deleted. 

        Returns:
            None: Dude the Anime is GONE. What you want to be returned?

        Raises:
            KeyError: If the anime doesn't exist. You can't delete what doesn't exist. Nice try.
        """
        if name not in self.animes:
            raise KeyError(
                f'"{name}" does not exist. You cannot delete what was never created.'
            )
        del self.animes[name]


anime = Anime()

anime.create("Yes", [Genres.Harem, Genres.Romance], Rating.Meh, 12, "tspmo man...")
print(anime.get("Yes"))

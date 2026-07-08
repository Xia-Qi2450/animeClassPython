# animeClassPython

Because I ran out of coding ideas.

## Features

- Create anime objects
- Retrieve anime objects
- Delete anime objects
- Type-safe enums for genres and ratings
- Input validation
- Passive-aggressive error messages

## Example

```python
anime = Anime()

anime.Create(
    "The Quintessential Quintuplets",
    [Genres.Romance, Genres.Comedy],
    Rating.Off_the_charts,
    24,
    "Miku supremacy."
)

print(anime.Get("The Quintessential Quintuplets"))

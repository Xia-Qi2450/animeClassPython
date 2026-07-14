# animeClassPython

> "I ran out of coding ideas."
>
> So I made an anime database library instead.

A small object-oriented Python library for creating, managing, and organizing anime entries. It started as a random coding project and somehow turned into a proper CRUD library.

## Features

- 📺 Create anime entries
- 🔍 Retrieve anime entries by name
- ✏️ Update existing entries
- 🗑️ Delete anime entries
- 🏷️ Strongly typed `Genres` and `Rating` enums
- ✅ Input validation with descriptive (and occasionally sarcastic) error messages
- 📝 Custom string representation for easy printing

## Example

```python
from main import Anime, Genres, Rating

library = Anime()

library.Create(
    name="The Quintessential Quintuplets",
    genres=[Genres.Romance, Genres.Comedy],
    rating=Rating.Off_the_charts,
    episodes=24,
    comments="Miku supremacy."
)

print(library.Get("The Quintessential Quintuplets"))

library.Update(
    "The Quintessential Quintuplets",
    rating=Rating.Amazing
)

library.delete("The Quintessential Quintuplets")
```

## Available Genres

| Genre |
|-------|
| Action |
| Adventure |
| Comedy |
| Mystery |
| Fantasy |
| Horror |
| Romance |
| Sci_Fi |
| Isekai |
| Slice_of_Life |
| Mecha |
| Yaoi |
| Yuri |
| Harem |
| Hentai *(You're on your own.)* |

## Ratings

| Rating | Meaning |
|---------|---------|
| Dogshit | Avoid at all costs. |
| Meh | Exists. |
| Mid | Perfectly average. |
| Not_Bad | Worth watching. |
| Great | Easy recommendation. |
| Amazing | Fantastic. |
| Off_the_charts | Certified peak fiction. |

## Current API

- `Create()`
- `Get()`
- `Update()`
- `Delete()`

## Roadmap

- [x] Create anime
- [x] Get anime
- [x] Update anime
- [x] Delete anime
- [ ] Search by genre
- [ ] Search by rating
- [ ] Save library to JSON
- [ ] Load library from JSON
- [ ] Statistics
- [ ] Random anime picker
- [ ] CLI interface

## Why?

Mostly because I wanted to practice object-oriented programming, enums, type hints, validation, and API design in Python.

Also because I genuinely ran out of project ideas.

## License

This project is licensed under the MIT License.
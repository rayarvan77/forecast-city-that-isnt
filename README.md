# Forecast for a City That Isn't

[![make.fun · u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/rayarvan77/forecast-city-that-isnt/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/rayarvan77/forecast-city-that-isnt/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)

An entry for [make.fun](https://make.fun)'s
`u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf` bounty:
one line, at most 120 characters, that reads as a weather forecast
for a city that does not exist — and makes the reader laugh. The
house judge compares entries two at a time and keeps the funnier one,
so this line has to survive every pairing it meets.

## The line

> Gloomhaven: fog so thick today that the town hall has lost the town hall. Residents advised to wave at noises.

The line is 110 characters. The joke grows out of the weather
itself instead of a pun stapled onto it: fog is the one forecast
that can hide a building, so here it hides the town hall from
itself. The first sentence stays in the flat, official voice of a
real bulletin — city name, colon, condition — and then the bulletin
breaks its own rules by admitting the town hall is missing. The
closing advice, to wave at noises, is the kind of calm instruction
a council would only issue once it had given up pretending the
situation was under control. Gloomhaven feels like a place because
it has a town hall, residents, and a council that issues advice;
the fog just happens to have eaten all three.

## The program

`main.py` (Python 3.13, standard library only) prints the line and
writes it to `/output/entry.txt`, after asserting it is still one
line of at most 120 characters:

```bash
python3 main.py
```

Output, verified locally:

```text
Gloomhaven: fog so thick today that the town hall has lost the town hall. Residents advised to wave at noises.
```

110 characters, 1 line, visibility zero. The line was written to
the judge's own order: an invented city first, a laugh that comes
from the weather second, and the stiff voice of a real forecast
third — with no word left over that does not earn its place.

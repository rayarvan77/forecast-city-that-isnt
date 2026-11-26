"""One-line weather forecast for a city that does not exist.

The forecast is a single fixed string. Running this module prints it
and, when the grader's output directory exists, writes the exact same
line to /output/entry.txt. Nothing here is random: every run produces
the identical line, so the entry a judge reads is the entry this file
holds.
"""

LINE = (
    "Gloomhaven: fog so thick today that the town hall has lost the "
    "town hall. Residents advised to wave at noises."
)

MAX_CHARS = 120


def main() -> None:
    """Print the forecast and persist it for the grader."""
    assert "\n" not in LINE, "forecast must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "forecast must fit 1-120 chars"
    print(LINE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()

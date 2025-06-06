import sys

sys.path.insert(0, "src/")
from pixelsparser import utils  # noqa: E402
from datetime import datetime  # noqa: E402


def test_load():
    pixels = utils.load("tests/test_data/test_diary.json")

    assert len(pixels) == 4
    assert pixels[0].date == datetime.strptime("2022-09-20", "%Y-%m-%d")
    assert pixels[0].pixelType == "Mood"
    assert pixels[0].scores == [2]
    assert (
        pixels[0].notes == "I accidentally ate a whole bag of chips today."
        " It slipped into my mouth. I swear!"
    )
    assert pixels[0].tags == [
        {"type": "Emotions", "entries": ["joy", "sadness", "fear", "disgust"]}
    ]
    assert pixels[0].score == 2
    assert pixels[0].mood == 2

    assert pixels[1].date == datetime.strptime("2022-09-21", "%Y-%m-%d")
    assert pixels[1].pixelType == "Mood"
    assert pixels[1].scores == [3]
    assert (
        pixels[1].notes == "I'm feeling pretty good today. I'm going to"
        " try to eat better."
    )
    assert pixels[1].tags == [{"type": "Emotions", "entries": ["joy", "disgust"]}]
    assert pixels[1].score == 3
    assert pixels[1].mood == 3

import sys
sys.path.insert(0, "src/")
from datetime import datetime  # noqa: E402
from pixelsparser import Pixel  # noqa: E402


def test_pixel_creation():
    date_str = "2023-06-29"
    pixel_type = "Mood"
    scores = [4]
    notes = "Woke up and had breakfast, went to work, had a good day"
    tags = [{"type": "Emotions", "entries": ["sad", "tired"]}]

    pixel = Pixel(date_str, pixel_type, scores, notes, tags)

    assert pixel.date == datetime.strptime(date_str, "%Y-%m-%d")
    assert pixel.pixelType == pixel_type
    assert pixel.scores == scores
    assert pixel.notes == notes
    assert pixel.tags == tags
    assert pixel.score == scores[0]
    assert pixel.mood == scores[0]


def test_pixel_string_representation():
    date_str = "2023-06-29"
    pixel_type = "Mood"
    scores = [3]
    notes = "Woke up and had breakfast, went to work, had a good day"
    tags = [{"type": "Emotions", "entries": ["sad", "tired"]}]

    pixel = Pixel(date_str, pixel_type, scores, notes, tags)

    expected_string = "Pixel(date=2023-06-29 00:00:00, type=Mood," + \
        "score=3, mood=3, notes=Woke up and had breakfast, went to work, " + \
        "had a good day,tags=[{'type': 'Emotions', 'entries': ['sad'," + \
        " 'tired']}])"

    print(str(pixel))

    assert str(pixel) == expected_string


def test_pixel_equality():
    date_str = "2023-06-29"
    pixel_type = "Mood"
    scores = [3]
    notes = "Woke up and had breakfast, went to work, had a good day"
    tags = [{"type": "Emotions", "entries": ["sad", "tired"]}]

    pixel1 = Pixel(date_str, pixel_type, scores, notes, tags)
    pixel2 = Pixel(date_str, pixel_type, scores, notes, tags)
    pixel3 = Pixel(date_str, "Food", scores, notes, tags)

    assert pixel1 == pixel2
    assert pixel1 != pixel3


def test_pixel_equality_with_different_date():
    date_str = "2023-06-29"
    pixel_type = "Mood"
    scores = [3]
    notes = "Woke up and had breakfast, went to work, had a good day"
    tags = [{"type": "Emotions", "entries": ["sad", "tired"]}]

    pixel1 = Pixel(date_str, pixel_type, scores, notes, tags)
    pixel2 = Pixel("2023-06-30", pixel_type,
                   scores, notes, tags)

    assert pixel1 != pixel2


if __name__ == "__main__":
    test_pixel_creation()
    test_pixel_string_representation()
    test_pixel_equality()

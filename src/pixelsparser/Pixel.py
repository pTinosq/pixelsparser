from datetime import datetime


class Pixel:
    """ Pixel class

    Keyword arguments:
    date -- date of the pixel
    mood -- mood value of the pixel
    notes -- notes of the pixel
    isHighlighted -- is the pixel highlighted
    tags -- tags of the pixel

    Return: Pixel object
    """

    def __init__(self, date: datetime, entries: list):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.mood = entries[0]['value']
        self.notes = entries[0]['notes']
        self.isHighlighted = entries[0]['isHighlighted']

        # If no tags are present, set tags to an empty list
        if len(entries[0]['tags']) == 0:
            self.tags = []
        else:
            self.tags = entries[0]['tags'][0]['entries']

    def __str__(self):
        return f"Pixel({self.date}, {self.mood}, {self.notes}, {self.isHighlighted}, {self.tags})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

from datetime import datetime


class Pixel:
    """ Pixel class

    Keyword arguments:
    date -- date of the pixel
    type -- type of the pixel
    scores -- list of scores
    notes -- notes of the pixel
    tags -- list of tag categories

    Return: Pixel object
    """

    def __init__(self, date: datetime, type: str, scores: list, notes: str, tags: list):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.pixelType = type
        self.notes = notes
        self.tags = tags

        # Multiple scores not yet implemented in the app
        self.scores = scores
        self.score = scores[0]
        self.mood = scores[0]


    def __str__(self):
        return f"Pixel(date={self.date}, type={self.pixelType}, score={self.score}, mood={self.mood}, notes={self.notes}, tags={self.tags})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

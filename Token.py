class Token:
    def __init__(self, name, score, count, candidates):
        self.name = name
        self.count = count
        self.score = score
        self.candidates = candidates


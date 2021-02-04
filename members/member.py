class Members:
    members = []

class Member:
    def __init__(self, values):
        self.tag = None
        self.name = None
        self.date_joined = None
        self.hit_attacks = 0
        self.missed_attacks = 0
        self.total_attacks = 0
        self.total_stars = 0
        self.total_destruction = 0.0

    def reliability(self):
        total_attacks = self.hit_attacks + self.missed_attacks
        return self.missed_attacks/total_attacks

    def average_stars(self):
        total_attacks = self.hit_attacks + self.missed_attacks
        return self.total_stars/total_attacks

    def average_destruction(self):
        total_attacks = self.hit_attacks + self.missed_attacks
        return self.total_destruction/total_attacks

def manage_members():
    J = Member(['tadf', 'J', '2020', 10,])
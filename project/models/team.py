from project import db


class TeamModel(db.Model):
    __tablename__ = 'championship'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(80))
    spi = db.Column(db.Float(precision=1))
    off = db.Column(db.Float(precision=1))
    defi = db.Column(db.Float(precision=1))
    goal_dif = db.Column(db.Integer)
    pts = db.Column(db.Integer)
    relegated = db.Column(db.Integer)
    make_from_playoffs = db.Column(db.Integer)
    promoted = db.Column(db.Integer)
    win_championship = db.Column(db.Integer)

    def __init__(self, team_name, spi=None, off=None, defi=None,
    goal_dif=None,pts=None,relegated=None,make_from_playoffs=None,
    promoted=None,win_championship=None):
        self.team_name = team_name
        self.spi = spi
        self.off = off
        self.defi = defi
        self.goal_dif = goal_dif
        self.pts = pts
        self.relegated = relegated
        self.make_from_playoffs = make_from_playoffs
        self.promoted = promoted
        self.win_championship = win_championship

    def json(self):
        return {'id': self.id,
        'team_name': self.team_name,
        'spi': self.spi,
        'off': self.off,
        'defi': self.defi,
        'goal_dif': self.goal_dif,
        'pts': self.pts,
        'relegated': self.relegated,
        'make_from_playoffs': self.make_from_playoffs,
        'promoted': self.promoted,
        'win_championship': self.win_championship}


    @classmethod
    def find_all(cls):
        return cls.query.all()


    @classmethod
    def find_by_name(cls, team_name):
        return cls.query.filter_by(team_name=team_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

from sqlalchemy import String, cast, or_

from project.models.match import MatchModel
from project.utils import utils


def find_by_squad_name(session, squad_name=None, round_name=None):
    query = session.query(MatchModel.match_id,
                          cast(MatchModel.match_date, String),
                          MatchModel.round_name,
                          MatchModel.first_squad_name,
                          MatchModel.first_squad_score,
                          MatchModel.first_squad_points,
                          MatchModel.second_squad_name,
                          MatchModel.second_squad_score,
                          MatchModel.second_squad_points)
    if squad_name:
        if '-' in squad_name:
            new_name = squad_name.replace('-', ' ')
            query = query.filter(or_(MatchModel.first_squad_name == new_name,
                                 MatchModel.second_squad_name == new_name))\
                     .all()
        else:
            query = query.filter(or_(MatchModel.first_squad_name == squad_name,
                                 MatchModel.second_squad_name == squad_name))\
                     .all()

    if round_name:
        query = query.filter(MatchModel.round_name == round_name).all()
    return utils.result_as_dict_matches(query)

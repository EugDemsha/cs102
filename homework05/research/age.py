import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    now = dt.datetime.now()
    year = float(now.year)
    items = get_friends(user_id=user_id, fields="bdate").items

    age = [year - float(i["bdate"][-4:]) for i in items if "bdate" in i and len(i["bdate"]) >= 9]
    av_age = statistics.mean(age) if age else None
    return av_age
    # response.json()['response']['items'][0]['first_name']

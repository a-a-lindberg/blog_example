import flask
from flask import jsonify

from data import db_session
from data.news import News

blueprint = flask.Blueprint('news_api', __name__, template_folder='templates')


@blueprint.route('/api/news')
def get_news():
    session = db_session.create_session()
    # TODO: Проверить авторизацию пользователя
    news = session.query(News).all()

    return jsonify(
        {
            'news': [
                item.to_dict(
                    only=('title', 'content', 'user.name')
                ) for item in news
            ]
        }
    )

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


@blueprint.route('/api/news/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    session = db_session.create_session()
    # TODO: Проверить авторизацию пользователя
    news = session.query(News).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': news.to_dict(
                only=('title', 'content', 'user_id', 'is_private')
            )
        }
    )

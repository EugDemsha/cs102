from bayes import NaiveBayesClassifier
from bottle import redirect, request, route, run, template
from db import News, session
from scraputils import get_news


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template("news_template", rows=rows)


@route("/add_label/")
def add_label():
    s = session()
    label = request.query.label
    id = request.query.id
    row = s.query(News).filter(News.id == id).one()
    row.label = label
    s.add(row)
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    s = session()
    new = get_news("https://news.ycombinator.com/newest", 3)
    for post in new:
        if not (
            s.query(News)
            .filter(News.title == post["title"] and News.author == post["author"])
            .first()
        ):
            el = News(
                title=post["title"],
                author=post["author"],
                url=post["url"],
                comments=post["comments"],
                points=post["points"],
                label=None,
            )
            s.add(el)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s = session()
    classifier = NaiveBayesClassifier()
    X_train = [r.title for r in s.query(News).filter(News.label != None).all()][0:300]
    y_train = [r.label for r in s.query(News).filter(News.label != None).all()][0:300]
    predict_db = s.query(News).filter(News.label == None).all()
    X_predict = [r.title for r in predict_db][0:100]
    classifier.fit(X_train, y_train)
    labels = classifier.predict(X_predict)
    for i in range(100):
        predict_db[i].label = labels[i]
    classified = [x for x in predict_db if x.label == "good"]
    classified.extend([x for x in predict_db if x.label == "maybe"])
    classified.extend([x for x in predict_db if x.label == "never"])
    return template("news_recs.tpl", rows=classified)


if __name__ == "__main__":
    run(host="localhost", port=8080, reloader=True)

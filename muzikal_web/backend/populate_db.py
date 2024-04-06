from models import *
import database
from app import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        for new in database.ImageList.imgs:
            news = Image(
                image=new.img,
                alt=new.alt,
                credit=new.credit,
            )
            db.session.add(news)

        db.session.commit()

from flask import Flask, render_template
from flask_app.models import db, migrate

def create_app():
    app = Flask(__name__) 
    ##db info setting 
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://qhilcsts:1POKik9TwGsb7ObtAflarchaFlRYWIXB@rosie.db.elephantsql.com:5432/qhilcsts" 
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자에게 정보 전달완료하면 teadown. 그 때마다 커밋=DB반영
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다
    app.secret_key = "secret_key"

    db.init_app(app)
    migrate.init_app(app, db) 

    from flask_app.routes import main_route
    app.register_blueprint(main_route.bp)

    return app

if __name__  == "__main__":
    app = create_app()
    app.run(debug=True)

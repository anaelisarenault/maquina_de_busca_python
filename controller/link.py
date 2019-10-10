from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Link(db.Model):
    
    __tablename__ = 'link'
    
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String)
    #ultimaColeta = db.Column(db.String)
    
    def __init__(self, url):
        self.url = url
        #self.ultimaColeta = ultimaColeta
        
db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrarLink")
def link():
    return render_template("cadastrarLink.html")

@app.route("/cadastrarLink", methods=['GET', 'POST'])
def cadastrarLink():
    if request.method == "POST":
        url = request.form.get("url")
        #ultimaColeta = request.form.get("ultimaColeta")
    
        if url:
            objLink = Link(url)
            db.session.add(objLink)
            db.session.commit()

    return redirect(url_for("index"))

@app.route("/listarLink")
def listarLink():
    links = Link.query.all()
    return render_template("listarLink.html", links=links)

@app.route("/excluir/<int:id>")
def excluir(id):
    link = Link.query.filter_by(_id=id).first()

    db.session.delete(link)
    db.session.commit()

    links = Link.query.all()
    return render_template("listarLink.html", links=links)

@app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    link = Link.query.filter_by(_id=id).first()

    if request.method == "POST":
        url = request.form.get("url")
        #ultimaColeta = request.form.get("ultimaColeta")

        if url:
            link.url = url
            
            db.session.commit()

            return redirect(url_for("/listarLink"))
    return render_template("atualizar.html", link=link)
    
def voltar():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
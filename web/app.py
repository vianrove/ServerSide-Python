from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']

    for p in model:
        if p.id_person == id_person:
            return render_template('person_exists.html')

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/person_update/<pid>', methods=['GET'])
def person_update(pid):
    return render_template('person_update.html', pid=pid)


@app.route('/update_confirmation/', methods=['POST'])
def update_confirmation():
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    for p in model:
        if p.id_person == request.form['id_person']:
            p.name = first_name
            p.last_name = last_name
            return render_template('update_confirmation.html')
        else:
            return render_template('person_doesnot_exist.html')


@app.route('/person_delete/<pid>')
def person_delete(pid):
    for p in model:
        if p.id_person == pid:
            model.remove(p)
    return render_template('person_delete.html')


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


if __name__ == '__main__':
    app.run()

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_app.models import Users, db, Medicine, User_medicine, get_medicinelist, zero_to_none, get_um


bp = Blueprint('main', __name__)

@bp.route("/")
def home():
  return render_template('home.html')


@bp.route("/signup", methods=['GET','POST'])
def signup():
  if request.method == 'POST':
    new_user = Users(
        email=request.form['email'],
        password=request.form['password'],
        username=request.form['username'],
        age=request.form['age'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.login'), code=200)
  return render_template('signup.html')


@bp.route("/login", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    data = Users.query.filter_by(email=email, password=password).first()
    if data is not None:
      session['email'] = email
      return redirect(url_for('main.home'), code=200)
    else:
      return "[ERROR!] 'email' 또는 'password'가 일치하지 않습니다"
  return render_template('login.html')


@bp.route("/logout", methods=['GET'])
def logout():
  session.pop('email', None)
  return redirect('/')
     

@bp.route('/medicine', methods=['GET', 'POST'])
def medicine_index():
    title = "의약품"
    sub_title = "어떤 의약품들이 있는지 확인해보세요"
    if request.method == 'POST':
        search = zero_to_none(request.form.get('search'))
        check_query = request.form.get('check_query', type=int)
        try:
            medicine_list = get_medicinelist(check_query=check_query, search=search)
        except:
            medicine_list = get_medicinelist()
    else:
        medicine_list = get_medicinelist()
    return render_template('medicine.html', medicine_list=medicine_list, title=title, sub_title=sub_title)


@bp.route('/user', methods=["GET", "POST"])
def user_medicine_index():
  title = '의약품 관리'
  sub_title = '의약품 관리에 오신 것을 환영합니다!'
  
  if request.method == 'POST':
    new_user_medicine = User_medicine(
        medicine_id=request.form['medicine_id'],
        user_itemname=request.form['user_itemname'],
        user_efcyqesitm=request.form['user_efcyqesitm'],
        user_usemethodqesitm=request.form['user_usemethodqesitm'])
    db.session.add(new_user_medicine)
    db.session.commit()
    
  else:
    user_medicine_list=get_um()

  return render_template('user.html', user_medicine_list=user_medicine_list, title=title, sub_title=sub_title)



@bp.route("/delete/<int:user_target_id>")
def delete(user_target_id):
    s = User_medicine.query.get(user_target_id)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for("main.user_medicine_index"))
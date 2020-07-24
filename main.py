from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    dets = User.query.filter_by(username=current_user.username).first()
    return render_template('profile.html', name=current_user.name,w1=dets.w1,w2=dets.w2,w3=dets.w3,w4=dets.w4,w5=dets.w5,w6=dets.w6,w7=dets.w7,w8=dets.w8,w9=dets.w9,w10=dets.w10,w11=dets.w11,w12=dets.w12,w13=dets.w13,w14=dets.w14,w15=dets.w15,w16=dets.w16,w17=dets.w17,w18=dets.w18,w19=dets.w19,w20=dets.w20,w21=dets.w21,w22=dets.w22,w23=dets.w23,w24=dets.w24)


@main.route('/word_session1', methods=["GET","POST"])
@login_required
def word_session1():
    return render_template('word_session1.html')

@main.route('/word_session2', methods=["GET","POST"])
@login_required
def word_session2():
    return render_template('word_session2.html')

@main.route('/word_session3', methods=["GET","POST"])
@login_required
def word_session3():
    return render_template('word_session3.html')

@main.route('/word_session4', methods=["GET","POST"])
@login_required
def word_session4():
    return render_template('word_session4.html')

@main.route('/word_session5', methods=["GET","POST"])
@login_required
def word_session5():
    return render_template('word_session5.html')

@main.route('/word_session6', methods=["GET","POST"])
@login_required
def word_session6():
    return render_template('word_session6.html')

@main.route('/word_session7', methods=["GET","POST"])
@login_required
def word_session7():
    return render_template('word_session7.html')

@main.route('/word_session8', methods=["GET","POST"])
@login_required
def word_session8():
    return render_template('word_session8.html')

@main.route('/word_session9', methods=["GET","POST"])
@login_required
def word_session9():
    return render_template('word_session9.html')

@main.route('/word_session10', methods=["GET","POST"])
@login_required
def word_session10():
    return render_template('word_session10.html')

@main.route('/word_session11', methods=["GET","POST"])
@login_required
def word_session11():
    return render_template('word_session11.html')

@main.route('/word_session12', methods=["GET","POST"])
@login_required
def word_session12():
    return render_template('word_session12.html')

@main.route('/word_session13', methods=["GET","POST"])
@login_required
def word_session13():
    return render_template('word_session13.html')

@main.route('/word_session14', methods=["GET","POST"])
@login_required
def word_session14():
    return render_template('word_session14.html')

@main.route('/word_session15', methods=["GET","POST"])
@login_required
def word_session15():
    return render_template('word_session15.html')

@main.route('/word_session16', methods=["GET","POST"])
@login_required
def word_session16():
    return render_template('word_session16.html')

@main.route('/word_session17', methods=["GET","POST"])
@login_required
def word_session17():
    return render_template('word_session17.html')

@main.route('/word_session18', methods=["GET","POST"])
@login_required
def word_session18():
    return render_template('word_session18.html')

@main.route('/word_session19', methods=["GET","POST"])
@login_required
def word_session19():
    return render_template('word_session19.html')

@main.route('/word_session20', methods=["GET","POST"])
@login_required
def word_session20():
    return render_template('word_session20.html')

@main.route('/word_session21', methods=["GET","POST"])
@login_required
def word_session21():
    return render_template('word_session21.html')


@main.route('/word_session22', methods=["GET","POST"])
@login_required
def word_session22():
    return render_template('word_session22.html')

@main.route('/word_session23', methods=["GET","POST"])
@login_required
def word_session23():
    return render_template('word_session23.html')

@main.route('/word_session24', methods=["GET","POST"])
@login_required
def word_session24():
    return render_template('word_session24.html')




@main.route('/saveprogress', methods=["POST"])
@login_required
def save_progress():
    correct = request.form.get("correct")
    incorrect = request.form.get("incorrect")
    wnumber = request.form.get("session")
    username=current_user.username
    per = ((int(correct))/(int(incorrect)+int(correct)))*100
    per_round = round(per,2)
    per_str = str(per_round)
    updateme = User.query.filter_by(username=current_user.username).first()
    if(wnumber=="1"):
        updateme.w1=per_str
    elif(wnumber=="2"):
        updateme.w2=per_str
    elif(wnumber=="3"):
        updateme.w3=per_str
    elif(wnumber=="4"):
        updateme.w4=per_str
    elif(wnumber=="5"):
        updateme.w5=per_str
    elif(wnumber=="6"):
        updateme.w6=per_str
    elif(wnumber=="7"):
        updateme.w7=per_str
    elif(wnumber=="8"):
        updateme.w8=per_str
    elif(wnumber=="9"):
        updateme.w9=per_str
    elif(wnumber=="10"):
        updateme.w10=per_str
    elif(wnumber=="11"):
        updateme.w11=per_str
    elif(wnumber=="12"):
        updateme.w12=per_str
    elif(wnumber=="13"):
        updateme.w13=per_str
    elif(wnumber=="14"):
        updateme.w14=per_str
    elif(wnumber=="15"):
        updateme.w15=per_str
    elif(wnumber=="16"):
        updateme.w16=per_str
    elif(wnumber=="17"):
        updateme.w17=per_str
    elif(wnumber=="18"):
        updateme.w18=per_str
    elif(wnumber=="19"):
        updateme.w19=per_str
    elif(wnumber=="20"):
        updateme.w20=per_str
    elif(wnumber=="21"):
        updateme.w21=per_str
    elif(wnumber=="22"):
        updateme.w22=per_str
    elif(wnumber=="23"):
        updateme.w23=per_str
    elif(wnumber=="24"):
        updateme.w24=per_str
    
    db.session.commit()
    return render_template('saveprogress.html')

@main.route('/testyourself', methods=["GET","POST"])
@login_required
def testyourself():
    return render_template('testyourself.html')

@main.route('/contact', methods=["GET"])
def contact():
    return render_template('contact.html')

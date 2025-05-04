from flask import*
from database import*
import uuid

doctor=Blueprint('doctor',__name__)

@doctor.route('/doctor_home')
def doctor_home():
    data={}
    a="select * from doctor where doctor_id='%s'"%(session['doctor'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('doctor_home.html',data=data)


@doctor.route('/doc_view_user')
def doc_view_user():
    data={}
    a="select * from appointment inner join user using(user_id) where doctor_id='%s'"%(session['doctor'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('doc_view_user.html',data=data)

@doctor.route('/doctor_view_appointment')
def doctor_view_appointment():
    data={}
    a="SELECT * FROM appointment INNER JOIN USER USING(user_id)  where doctor_id='%s'"%(session['doctor'])
    b=select(a)
    if b:
        data['view']=b
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'accept':
            c="update appointment set appointment_status='Accept' where appointment_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("ACCEPTED");window.location='/doctor_view_appointment'</script>'''
        if action == 'reject':
            e="update appointment set appointment_status='Reject' where appointment_id='%s'"%(id)
            f=update(e)
            if f:
                return'''<script>alert("REJECTED");window.location='/doctor_view_appointment'</script>'''
    
    return render_template('doctor_view_appointment.html',data=data)

@doctor.route('/doctor_add_slot',methods=['post','get'])
def doctor_add_slot():
    id=request.args['id']
    if 'submit' in request.form:
        date=request.form['date']
        time=request.form['time']
        a="insert into slot values(null,'%s','%s','%s')"%(id,date,time)
        b=insert(a)
        if b:
            return'''<script>alert("TIME SLOT IS ADDED 👏");window.location='/doctor_view_appointment'</script>'''
    return render_template('doctor_add_slot.html')

@doctor.route('/doctor_add_fees',methods=['post','get'])
def doctor_add_fees():
    if 'submit' in request.form:
        fees=request.form['fees']
        a="insert into fees values(null,'%s','%s',curdate())"%(session['doctor'],fees)
        b=insert(a)
        if b:
            return'''<script>alert("FEES ADDED 👏");window.location='/doctor_add_fees'</script>'''
        
    data={}
    c="select * from fees where doctor_id='%s'"%(session['doctor'])
    d=select(c)
    if d:
        data['view']=d
        
        if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'update':
                c="select * from fees where fees_id='%s'"%(id)
                d=select(c)
                if d:
                    data['up']=d
                    if 'update' in request.form:
                        fees=request.form['fees']
                        e="update fees set fees='%s',fees_date=curdate() where fees_id='%s'"%(fees,id)
                        f=update(e)
                        if f:
                            return'''<script>alert("SUCCESFULLY UPDATED");window.location='/doctor_add_fees'</script>'''

    return render_template('doctor_add_fees.html',data=data)

@doctor.route('/doctor_view_payment')
def doctor_view_payment():
    data={}
    a="select * from doctor_payment inner join user using(user_id) where doctor_id='%s'"%(session['doctor'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('doctor_view_payment.html',data=data)

@doctor.route('/doctor_view_users')
def doctor_view_users():
    data={}
    qry="select * from user inner join user using(user_id) where doctor_id='%s'"%(session['doctor'])
    res=select(qry)
    if res:
        data['view']=res
    return render_template("doctor_view_users.html",data=data)

@doctor.route('/doctor_view_message',methods=['POST','GET'])
def doctor_view_message():
    data={}
    name=''
    uid=None
    if 'action' in request.args:
        action=request.args['action']
        session['id']=request.args['id']
        c="select * from user where login_id='%s'"%(session['id'])
        d=select(c)
        uid=d[0]['user_id']
        name=request.args['name']

    else:
        action=None
    
    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY chat_date , chat_time"%(uid,session['doctor'],session['doctor'],uid)
    rg=select(f)
    print(rg)
    data['rg']=rg

    if 'submit' in request.form:
        chat=request.form['chat']
        print(chat,"000000000000000000000000000000000000000000000000")
        a="insert into chat values(null,'%s','doctor','%s','user','%s',curdate(),curtime())"%(session['doctor'],uid,chat)
        insert(a)
        return redirect(url_for('doctor.doctor_view_message',id=session['id'],name=name,action='chat'))
    return render_template("doctor_view_message.html",data=data,name=name)

@doctor.route('/doctor_manage_profile',methods=['post','get'])
def doctor_manage_profile():
    data={}
    a="select * from doctor where doctor_id='%s'"%(session['doctor'])
    b=select(a)
    if b:
        data['view']=b
        if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'update':
                c="select * from doctor where doctor_id='%s'"%(id)
                d=select(c)
                if d:
                    data['up']=d
                    if 'submit' in request.form:
                        fname=request.form['fname']
                        lname=request.form['lname']
                        email=request.form['email']
                        phone=request.form['phone']
                        place=request.form['place']
                        qualification=request.form['qualification']
                        certificate=request.files['certificate']
                        experience=request.form['experience']
                        path1='static/'+str(uuid.uuid4())+certificate.filename
                        certificate.save(path1)
                        e="update doctor set doctor_fname='%s',doctor_lname='%s',doctor_email='%s',doctor_phone='%s',doctor_place='%s',doctor_qualification='%s',doctor_certificate='%s',doctor_experience='%s' where doctor_id='%s'"%(fname,lname,email,phone,place,qualification,path1,experience,id)
                        f=update(e)
                        if f:
                            return'''<script>alert("SUCCESFULLY UPDATED");window.location='/doctor_manage_profile'</script>'''

        
    return render_template('doctor_manage_profile.html',data=data)


@doctor.route('/doctor_manage_schedule', methods=['post', 'get'])
def doctor_manage_schedule():
    id = request.args['id']
    if 'submit' in request.form:
        start_day = request.form['start_day']
        end_day = request.form['end_day']
        stime = request.form['stime']
        etime = request.form['etime']
        # Combine start_day and end_day into a single string
        day_range = f"{start_day}-{end_day}"
        a = "insert into schedule values(null,'%s','%s','%s','%s')" % (id, day_range, stime, etime)
        b = insert(a)
        if b:
            return '''<script>alert("Schedule Added Successfully");window.location='/doctor_manage_profile'</script>'''
        
    data = {}
    c = "select * from schedule where doctor_id='%s'" % (session['doctor'])
    d = select(c)
    if d:
        data['view'] = d
    
    if 'action' in request.args:
        act=request.args['action']
        id=request.args['id']
    else:
        act=None
    
    if act=='update':
        x="select * from schedule where schedule_id='%s'"%(id)
        data['up']=select(x)
    
    if 'upd' in request.form:
        start_day = request.form['start_day']
        end_day = request.form['end_day']
        stime = request.form['stime']
        etime = request.form['etime']
        # Combine start_day and end_day into a single string
        day_range = f"{start_day}-{end_day}"

        x="update schedule set day='%s',start_time='%s',end_time='%s' where schedule_id='%s'"%(day_range,stime,etime,id)
        update(x) 
        return '''<script>alert("Schedule Added Successfully");window.location='/doctor_manage_profile'</script>'''

    

    return render_template('doctor_manage_schedule.html', data=data)
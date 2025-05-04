from flask import*
from database import*
import uuid

pet_sitting=Blueprint('pet_sitting',__name__)

@pet_sitting.route('/pet_sitting_home')
def pet_sitting_home():
    data={}
    a="select * from pet_sitting where petsitting_id='%s'"%(session['petsitting'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('pet_sitting_home.html',data=data)


@pet_sitting.route('/pet_sitting_facility',methods=['post','get'])
def pet_sitting_facility():
    if 'submit' in request.form:
        service=request.form['service']
        des=request.form['des']
        img=request.files['img']
        path1='static/'+str(uuid.uuid4())+img.filename
        img.save(path1)
        a="insert into facility values(null,'%s','%s','%s','%s')"%(session['petsitting'],service,des,path1)
        b=insert(a)
        if b:
            return'''<script>alert("FACILITY ADDED 👏");window.location='/pet_sitting_facility'</script>'''
        
    data={}
    c="select * from facility where petsitting_id='%s'"%(session['petsitting'])
    d=select(c)
    if d:
        data['view']=d
        
        if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
            if action == 'update':
                c="select * from facility where facility_id='%s'"%(id)
                d=select(c)
                if d:
                    data['up']=d
                    if 'update' in request.form:
                        service=request.form['service']
                        des=request.form['des']
                        img=request.files['img']
                        path1='static/'+str(uuid.uuid4())+img.filename
                        img.save(path1)
                        e="update facility set service='%s',facility_des='%s',facility_image='%s' where facility_id='%s'"%(service,des,path1,id)
                        f=update(e)
                        if f:
                            return'''<script>alert("SUCCESFULLY UPDATED");window.location='/pet_sitting_facility'</script>'''
            if action == 'delete':
                g="delete from facility where facility_id='%s'"%(id)
                h=delete(g)
                if h:
                    return'''<script>alert("SUCCESFULLY DLETED");window.location='/pet_sitting_facility'</script>'''


    return render_template('pet_sitting_facility.html',data=data)

@pet_sitting.route('/pet_sitting_view_request')
def pet_sitting_view_request():
    data={}
    a="select * from request inner join user using(user_id) where petsitting_id='%s'"%(session['petsitting'])
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'accept':
            c="update request set request_status='accept' where request_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("ACCEPTED");window.location='/pet_sitting_view_request'</script>'''
        if action == 'reject':
            c="update request set request_status='reject' where request_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("REJECTED");window.location='/pet_sitting_view_request'</script>'''
    return render_template('pet_sitting_view_request.html',data=data)


@pet_sitting.route('/pet_sitting_proposal',methods=['post','get'])
def pet_sitting_proposal():
    id=request.args['id']
    if 'submit' in request.form:
        amt=request.form['amt']
        a="insert into proposal values(null,'%s','%s','pending',curdate())"%(id,amt)
        b=insert(a)
        if b:
            return'''<script>alert("PROPOSAL SEND SUCCESSFULLY");window.location='/pet_sitting_view_request'</script>'''
        
    data={}
    c="select * from proposal where request_id='%s'"%(id)
    d=select(c)
    if d:
        data['view']=d

    
    return render_template('pet_sitting_proposal.html',data=data)

@pet_sitting.route('/pet_sitting_view_payment')
def pet_sitting_view_payment():
    id=request.args['id']
    data={}
    a="select * from proposal_payment where proposal_id='%s'"%(id)
    b=select(a)
    if b:
        data['view']=b
    return render_template('pet_sitting_view_payment.html',data=data)


@pet_sitting.route('/pet_sitting_complaint',methods=['post','get'])
def pet_sitting_complaint():
    if 'submit' in request.form:
        comp=request.form['comp']
        a="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['log'],comp)
        b=insert(a)
        if b:
             return'''<script>alert("COMPLAINT SEND SUCCESSFULLY");window.location='/pet_sitting_complaint'</script>'''
        
    data={}
    c="select * from complaint where login_id='%s'"%(session['log'])
    d=select(c)
    if d:
        data['view']=d

    
    return render_template('pet_sitting_complaint.html',data=data)

@pet_sitting.route('/pet_sitting_view_user')
def pet_sitting_view_user():
    data={}
    # a="SELECT * FROM USER "
    a="select * from user inner join request using(user_id) where petsitting_id='%s'"%(session['petsitting'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('pet_sitting_view_user.html',data=data)

@pet_sitting.route('/pet_sitting_chat',methods=['post','get'])
def pet_sitting_chat():
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
        print(name,"999999999999999999999999999999")

    else:
        action=None
    
    f="SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY chat_date , chat_time"%(session['id'],session['log'],session['log'],session['id'])
    rg=select(f)
    print(rg)
    data['rg']=rg

    if 'submit' in request.form:
        chat=request.form['chat']
        print(chat,"000000000000000000000000000000000000000000000000")
        a="insert into chat values(null,'%s','pet_sitting','%s','user','%s',curdate(),curtime())"%(session['log'],session['id'],chat)
        insert(a)
        return redirect(url_for('pet_sitting.pet_sitting_chat',id=session['id'],name=name,action='chat'))
    
    return render_template('pet_sitting_chat.html',data=data,name=name)

@pet_sitting.route("/pet_sitting_profile")
def pet_sitting_profile():
    data={}
    a="select * from pet_sitting where petsitting_id='%s'"%(session['petsitting'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('pet_sitting_profile.html',data=data)

@pet_sitting.route('/pet_sitting_edit_profile',methods=['post','get'])
def pet_sitting_edit_profile():
    data={}
    a="select * from pet_sitting where petsitting_id='%s'"%(session['petsitting'])
    b=select(a)
    if b:
        data['up']=b
    
    if 'submit' in request.form:
        name=request.form['name']
        owname=request.form['oname']
      
        estd=request.form['date']
        email=request.form['email']
        phone=request.form['phone']
        address=request.form['add']
        city=request.form['city']
        state=request.form['state']
        d="update pet_sitting set petsitting_name='%s',owner_name='%s',established_date='%s',petsitting_email='%s',petsitting_phone='%s',street_address='%s',petsitting_city='%s',petsitting_state='%s' where petsitting_id='%s'"%(name,owname,estd,email,phone,address,city,state,session['petsitting'])
        e=update(d)
        if e:
            return'''<script>alert("UPDATED SUCCESSFULLY");window.location='/pet_sitting_profile'</script>'''



    return render_template('pet_sitting_edit_profile.html',data=data)



from flask import*
from database import*
import uuid

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['post','get'])
def login():
    if 'submit' in request.form:
        uname=request.form['uname']
        password=request.form['password']
        a="select * from login where user_name='%s' and password='%s'"%(uname,password)
        b=select(a)
        if b:
            session['log'] = b[0]['login_id']
            if b[0]['user_type']== 'admin':
                return redirect(url_for('admin.admin_home'))
            if b[0]['user_type']== 'shop':
                c="select * from pet_shop where login_id='%s'"%(session['log'])
                d=select(c)
                if d:
                    session['shop'] = d[0]['pet_shop_id']
                    return redirect(url_for('petshop.petshop_home'))
            if b[0]['user_type']== 'doctor':
                c="select * from doctor where login_id='%s'"%(session['log'])
                d=select(c)
                if d:
                    session['doctor'] = d[0]['doctor_id']
                    return redirect(url_for('doctor.doctor_home'))
                
            if b[0]['user_type']== 'pet_sitting':
                cx="select * from pet_sitting where login_id='%s'"%(session['log'])
                dx=select(cx)
                if dx:
                    session['petsitting'] = dx[0]['petsitting_id']
                    return redirect(url_for('pet_sitting.pet_sitting_home'))
    return render_template('login.html')

@public.route('/pet_shop',methods=['post','get'])
def pet_shop():
    
    if 'submit' in request.form:
        sname=request.form['sname']
        email=request.form['email']
        phone=request.form['phone']
        place=request.form['place']
        address=request.form['address']
        lisenceno=request.form['lisenceno']
        lisence=request.files['lisence']
        uname=request.form['uname']
        password=request.form['password']
        path1='static/'+str(uuid.uuid4())+lisence.filename
        lisence.save(path1)
        qry="select * from pet_shop where shop_email='%s'"%(email)
        res=select(qry)
        if res:
            return'''<script>alert("Email already registered. Please chose another email");window.location.back()</script>'''
        
        qry="select * from doctor where doctor_email='%s'"%(email)
        res=select(qry)    
        if res:
            return'''<script>alert("Email already registered. Please chose another email");window.location.back()</script>'''
        
        qry="select * from pet_sitting where petsitting_email='%s'"%(email)
        res=select(qry)    
        if res:
            return'''<script>alert("Email already registered. Please chose another email");window.location.back()</script>'''
        
        else:
            a="insert into login values(null,'%s','%s','pending')"%(uname,password)
            b=insert(a)
            c="insert into pet_shop values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(b,sname,email,phone,place,address,lisenceno,path1)
            d=insert(c)
            if d:
                return'''<script>alert("Registration Completed");window.location='/'</script>'''
        
    return render_template('pet_shop.html')

@public.route('/doctor',methods=['post','get'])
def doctor():
    
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        phone=request.form['phone']
        place=request.form['place']
        qualification=request.form['qualification']
        certificate=request.files['certificate']
        experience=request.form['experience']
        uname=request.form['uname']
        password=request.form['password']
        path1='static/'+str(uuid.uuid4())+certificate.filename
        certificate.save(path1)

        qry="select * from pet_shop where shop_email='%s'"%(email)
        res=select(qry)
        if res:
            return'''<script>alert("Email already registered. Please chose another email");window.location.back()</script>'''
        
        qry="select * from doctor where doctor_email='%s'"%(email)
        res=select(qry)    
        if res:
            return'''<script>alert("Email already registered. Please chose another email");window.location.back()</script>'''
        
        qry="select * from pet_sitting where petsitting_email='%s'"%(email)
        res=select(qry)    
        if res:
            return'''<script>alert("Email already registered. Please chose another email");window.location.back()</script>'''
        
        else:
            a="insert into login values(null,'%s','%s','pending')"%(uname,password)
            b=insert(a)
            c="insert into doctor values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,fname,lname,email,phone,place,qualification,experience,path1)
            d=insert(c)
            if d:
                return'''<script>alert("Registration Completed");window.location='/'</script>'''
        
    return render_template('doctor.html')

@public.route('/pet_sitting',methods=['post','get'])
def pet_sitting():
    
    if 'submit' in request.form:
        psname=request.form['psname']
        owname=request.form['owname']
        lsnc=request.files['lisence']
        estd=request.form['estd']
        email=request.form['email']
        phone=request.form['phone']
        address=request.form['address']
        city=request.form['city']
        state=request.form['state']
        uname=request.form['uname']
        password=request.form['password']
        path1='static/'+str(uuid.uuid4())+lsnc.filename
        lsnc.save(path1)
        qry="select * from pet_shop where shop_email='%s'"%(email)
        res=select(qry)
        if res:
            return'''<script>alert("Email already registered. Please chose another email");history.back()</script>'''
        
        qry="select * from doctor where doctor_email='%s'"%(email)
        res=select(qry)    
        if res:
            return'''<script>alert("Email already registered. Please chose another email");history.back()</script>'''
        
        qry="select * from pet_sitting where petsitting_email='%s'"%(email)
        res=select(qry)    
        if res:
            return'''<script>alert("Email already registered. Please chose another email");history.back()</script>'''
        
        else:
            a="insert into login values(null,'%s','%s','pending')"%(uname,password)
            b=insert(a)
            c="insert into pet_sitting values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(b,psname,owname,path1,estd,email,phone,address,city,state)
            d=insert(c)
            if d:
                return'''<script>alert("Registration Completed");window.location='/'</script>'''
            
    return render_template('pet_sitting.html')


@public.route('/forgot_password', methods=['POST', 'GET'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        # List of tables and their respective email fields
        tables = {
            "pet_shop": "shop_email",
            "doctor": "doctor_email",
            "pet_sitting": "petsitting_email"
        }

        for table, email_column in tables.items():
            qry = f"SELECT login_id FROM {table} WHERE {email_column} = '%s'"%(email)
            res = select(qry)  # Using parameterized query
            if res:
                flash("Email Verified! Please reset your password.", "success")
                return redirect(f"/newpassword?id={res[0]['login_id']}")

        flash("Email not found. Please enter a registered email.", "danger")

    return render_template('forgot_password.html')


@public.route('/newpassword',methods=['POST','GET'])
def newpassword():
    id=request.args['id']
    if 'submit' in request.form:
        npassword=request.form['password1']
        cpassword=request.form['password2']

        if npassword==cpassword:
            qry="update login set password='%s' where login_id='%s'"%(npassword,id)
            update(qry)
            return'''<script>alert("Password Updated");window.location='/login'</script>'''
        else:
           return'''<script>alert("Passwords does not match");history.back()</script>''' 

    return render_template('newpassword.html')
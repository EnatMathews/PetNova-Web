from flask import*
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@admin.route('/admin_verify_shop')
def admin_verify_shop():
    data={}
    a="select * from pet_shop inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'accept':
            c="update login set user_type='shop' where login_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("ACCEPTED");window.location='/admin_verify_shop'</script>'''
        if action == 'reject':
            c="update login set user_type='reject' where login_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("REJECTED");window.location='/admin_verify_shop'</script>'''
    return render_template('admin_verify_shop.html',data=data)


@admin.route('/admin_verify_petsitting')
def admin_verify_petsitting():
    data={}
    a="select * from pet_sitting inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'accept':
            c="update login set user_type='pet_sitting' where login_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("ACCEPTED");window.location='/admin_verify_petsitting'</script>'''
        if action == 'reject':
            c="update login set user_type='reject' where login_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("REJECTED");window.location='/admin_verify_petsitting'</script>'''
    return render_template('admin_verify_petsitting.html',data=data)


@admin.route('/admin_verify_doctor')
def admin_verify_doctor():
    data={}
    a="select * from doctor inner join login using(login_id)"
    b=select(a)
    if b:
        data['view']=b
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        if action == 'accept':
            c="update login set user_type='doctor' where login_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("ACCEPTED");window.location='/admin_verify_doctor'</script>'''
        if action == 'reject':
            c="update login set user_type='reject' where login_id='%s'"%(id)
            d=update(c)
            if d:
                return'''<script>alert("REJECTED");window.location='/admin_verify_doctor'</script>'''
    return render_template('admin_verify_doctor.html',data=data)

@admin.route('/admin_view_user')
def admin_view_user():
    data={}
    a="select * from user"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_user.html',data=data)

@admin.route('/admin_view_pet')
def admin_view_pet():
    data={}
    a="select * from pet inner join pet_shop using(pet_shop_id)"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_pet.html',data=data)

@admin.route('/admin_view_product')
def admin_view_product():
    data={}
    a="select * from product"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_product.html',data=data)

@admin.route('/admin_view_pet_order')
def admin_view_pet_order():
    data={}
    a="SELECT * FROM `pet_master` INNER JOIN `pet_child` USING(pet_master_id)INNER JOIN `pet` USING(pet_id)"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_pet_order.html',data=data)

@admin.route('/admin_view_product_order')
def admin_view_product_order():
    data={}
    a="SELECT * FROM `product_master` INNER JOIN `product_child` USING(product_master_id)INNER JOIN `product` USING(product_id)"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_product_order.html',data=data)

@admin.route('/admin_view_complaint',methods=['post','get'])
def admin_view_complaint():
    data={}
    # a="SELECT * FROM complaint INNER JOIN `login` USING (login_id) INNER JOIN `user` USING(login_id)"
    a="""
SELECT 
    c.complaint_id, 
    c.login_id, 
    c.complaint, 
    c.complaint_reply, 
    c.complaint_date,
    COALESCE(u.user_fname, p.petsitting_name) AS sender_name,
    COALESCE(u.user_phone, p.petsitting_phone) AS sender_phone,
    COALESCE(u.user_email, p.petsitting_email) AS sender_email,
    COALESCE(u.user_place, p.petsitting_city) AS sender_city,
    COALESCE(u.user_address, p.street_address) AS sender_address,
    CASE 
        WHEN u.login_id IS NOT NULL THEN 'User' 
        WHEN p.login_id IS NOT NULL THEN 'Pet Sitting Service' 
        ELSE 'Unknown' 
    END AS sender_type
FROM complaint c
LEFT JOIN USER u ON c.login_id = u.login_id
LEFT JOIN pet_sitting p ON c.login_id = p.login_id;
"""
    b=select(a)
    if b:
        data['view']=b

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
        if action == 'reply':
            c="select * from complaint where complaint_id='%s'"%(id)
            d=select(c)
            if d:
                data['up']=d
                if 'submit' in request.form:
                    reply=request.form['reply']
                    e="update complaint set complaint_reply='%s' where complaint_id='%s'"%(reply,id)
                    f=update(e)
                    if f:
                        return'''<script>alert("REPLY SEND SUCCESSFULLY ✅");window.location='/admin_view_complaint'</script>'''
    return render_template('admin_view_complaint.html',data=data)


@admin.route('/admin_view_feedback')
def admin_view_feedback():
    data={}
    a="SELECT * FROM feedback INNER JOIN `login` USING (login_id) INNER JOIN `user` USING(login_id)"
    b=select(a)
    if b:
        data['view']=b
    return render_template('admin_view_feedback.html',data=data)
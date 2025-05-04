from flask import*
from database import*
import uuid
import qrcode

petshop=Blueprint('petshop',__name__)

@petshop.route('/petshop_home')
def petshop_home():
    data={}
    a="select * from pet_shop where pet_shop_id='%s'"%(session['shop'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_home.html',data=data)

@petshop.route('/petshop_manage_pet',methods=['post','get'])
def petshop_manage_pet():
    if 'submit' in request.form:
        pname=request.form['pname']
        type=request.form['type']
        breed=request.form['breed']
        age=request.form['age']
        gender=request.form['gender']
        status=request.form['status']
        img=request.files['image']
        price=request.form['price']
        stock=request.form['stock']
        path='static/'+str(uuid.uuid4())+img.filename
        img.save(path)
        a="insert into pet values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(session['shop'],pname,type,breed,age,gender,status,path,price,stock)
        b=insert(a)
        if b:
            return'''<script>alert("SUCCESFULLY ADDED");window.location='/petshop_manage_pet'</script>'''
    data={}
    c="select * from pet where pet_shop_id='%s'"%(session['shop'])
    d=select(c)
    if d:
        data['view']=d

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
        if action == 'update':
            e="select * from pet where pet_id='%s'"%(id)
            f=select(e)
            if f:
                data['up']=f
                if 'update' in request.form:
                    pname1=request.form['pname']
                    type1=request.form['type']
                    breed1=request.form['breed']
                    age1=request.form['age']
                    gender1=request.form['gender']
                    status1=request.form['status']
                    img1=request.files['image']
                    price1=request.form['price']
                    stock1=request.form['stock']
                    path1='static/'+str(uuid.uuid4())+img1.filename
                    img1.save(path1)
                    g="update pet set pet_name='%s',pet_type='%s',pet_breed='%s',pet_age='%s',pet_gender='%s',pet_vaccination_status='%s',pet_image='%s',pet_price='%s',pet_stock='%s' where pet_id='%s'"%(pname1,type1,breed1,age1,gender1,status1,path1,price1,stock1,id)
                    h=update(g)
                    if g:
                        return'''<script>alert("SUCCESFULLY UPDATED");window.location='/petshop_manage_pet'</script>'''
        if action == 'delete':
            h="delete from pet where pet_id='%s'"%(id)
            i=delete(h)
            if i:
                return'''<script>alert("SUCCESFULLY DELETED");window.location='/petshop_manage_pet'</script>'''
    return render_template('petshop_manage_pet.html',data=data)

@petshop.route('/petshop_manage_product',methods=['post','get'])
def petshop_manage_product():
    if 'submit' in request.form:
        pname=request.form['pname']
        price=request.form['price']
        stock=request.form['stock']
        img=request.files['image']
        path='static/'+str(uuid.uuid4())+img.filename
        img.save(path)
        a="insert into product values(null,'%s','%s','%s','%s','%s')"%(pname,price,stock,path,session['shop'])
        b=insert(a)
        if b:
            return'''<script>alert("SUCCESFULLY ADDED");window.location='/petshop_manage_product'</script>'''
    data={}
    c="select * from product where pet_shop_id='%s'"%(session['shop'])
    d=select(c)
    if d:
        data['view']=d

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
        if action == 'update':
            e="select * from product where product_id='%s'"%(id)
            f=select(e)
            if f:
                data['up']=f
                if 'update' in request.form:
                    pname=request.form['pname']
                    price=request.form['price']
                    stock=request.form['stock']
                    img=request.files['image']
                    path='static/'+str(uuid.uuid4())+img.filename
                    img.save(path)
                    g="update product set product_name='%s',product_price='%s',product_stock='%s',product_image='%s' where product_id='%s'"%(pname,price,stock,path,id)
                    h=update(g)
                    if g:
                        return'''<script>alert("SUCCESFULLY UPDATED");window.location='/petshop_manage_product'</script>'''
        if action == 'delete':
            h="delete from product where product_id='%s'"%(id)
            i=delete(h)
            if i:
                return'''<script>alert("SUCCESFULLY DELETED");window.location='/petshop_manage_product'</script>'''
    return render_template('petshop_manage_product.html',data=data)

@petshop.route('/petshop_view_pet_order')
def petshop_view_pet_order():
    data={}
    a="SELECT * FROM `pet_master` INNER JOIN `pet_child` USING(pet_master_id) INNER JOIN pet USING(pet_id) WHERE pet_shop_id='%s'"%(session['shop'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_view_pet_order.html',data=data)

@petshop.route('/petshop_view_pet_order_user')
def petshop_view_pet_order_user():
    id=request.args['id']
    data={}
    a="SELECT * FROM `user` INNER JOIN `pet_master` USING(user_id) WHERE pet_master_id='%s'"%(id)
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_view_pet_order_user.html',data=data)

@petshop.route('/petshop_view_pet_payment')
def petshop_view_pet_payment():
    id=request.args['id']
    data={}
    a="SELECT * FROM pet_payment WHERE pet_master_id='%s'"%(id)
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_view_pet_payment.html',data=data)


@petshop.route('/petshop_view_product_order')
def petshop_view_product_order():
    data={}
    a="SELECT * FROM `product_master` INNER JOIN `product_child` USING(product_master_id) INNER JOIN product USING(product_id) WHERE pet_shop_id='%s'"%(session['shop'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_view_product_order.html',data=data)

@petshop.route('/petshop_view_product_order_user')
def petshop_view_product_order_user():
    data={}
    a="SELECT * FROM `user` INNER JOIN `pet_master` USING(user_id) WHERE pet_master_id='%s'"%(session['shop'])
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_view_product_order_user.html',data=data)

@petshop.route('/petshop_view_product_payment')
def petshop_view_product_payment():
    id=request.args['id']
    data={}
    a="SELECT * FROM product_payment WHERE product_master_id='%s'"%(id)
    b=select(a)
    if b:
        data['view']=b
    return render_template('petshop_view_product_payment.html',data=data)

from datetime import datetime

@petshop.route('/petshop_add_show', methods=['post', 'get'])
def petshop_add_show():
    if 'submit' in request.form:
        show = request.form['show']
        cat = request.form['cat']
        place = request.form['place']
        date = request.form['date']
        time = request.form['time']
        a = "insert into pet_show values(null,'%s','%s','%s','%s','%s','%s','Pending')" % (session['shop'], show, cat, place, date, time)
        b = insert(a)
        if b:
            return '''<script>alert("SUCCESFULLY ADDED");window.location='/petshop_add_show'</script>'''

    data = {}
    current_date = datetime.now().strftime('%Y-%m-%d')
    # Fixed the query: replaced second 'where' with 'AND' and used 'pet_show_id'
    c = "SELECT * FROM pet_show WHERE show_date >= '%s' AND show_id='%s'" % (current_date, session['shop'])
    d = select(c)
    if d:
        data['view'] = d

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
        if action == 'update':
            e = "select * from pet_show where pet_show_id='%s'" % (id)
            f = select(e)
            if f:
                data['up'] = f
                if 'update' in request.form:
                    show = request.form['show']
                    cat = request.form['cat']
                    place = request.form['place']
                    date = request.form['date']
                    time = request.form['time']
                    g = "update pet_show set show_name='%s', show_participation='%s', show_place='%s', show_date='%s', show_time='%s' where pet_show_id='%s'" % (show, cat, place, date, time, id)
                    h = update(g)
                    # Fixed: Check 'h' instead of 'g' for update success
                    if h:
                        return '''<script>alert("SUCCESFULLY UPDATED");window.location='/petshop_add_show'</script>'''
        if action == 'delete':
            h = "delete from pet_show where pet_show_id='%s'" % (id)
            i = delete(h)
            if i:
                return '''<script>alert("SUCCESFULLY DELETED");window.location='/petshop_add_show'</script>'''
    return render_template('petshop_add_show.html', data=data)

@petshop.route('/petshop_add_show_pet',methods=['post','get'])
def petshop_add_show_pet():
    id=request.args['id']
    if 'submit' in request.form:
        name=request.form['name']
        type=request.form['type']
        breed=request.form['breed']
        age=request.form['age']
        gender=request.form['gender']
        color=request.form['color']
        size=request.form['size']
        weight=request.form['weight']
        coat=request.form['coat']
        feature=request.form['feature']
        owner=request.form['owner']
        img=request.files['img']
        path='static/'+str(uuid.uuid4())+img.filename
        img.save(path)
      
        a="insert into pet_show_pet values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','0','%s','%s')"%(id,breed,age,gender,color,size,weight,coat,feature,owner,path,name,type)
        b=insert(a)
        if b:
            o="select * from pet_show_pet where pet_show_pet_id='%s'"%(b) 
            e=select(o) 
            if e: 
                session['name']=e[0]['show_pet_breed'] 
            qr = qrcode.QRCode( 
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=10, 
            border=4, 
            ) 
            qr.add_data(b) 
            qr.make(fit=True) 
 
            # Create an image of the QR code 
            img = qr.make_image(fill_color="black", back_color="white") 
            rr="static/qrcode/"+ session['name'] +".png" # Save the QR code image to a file 
            img.save(rr) 
             
            up="update pet_show_pet set show_qr_code='%s' where pet_show_pet_id='%s'"%(rr,b) 
            update(up)

            return'''<script>alert("SUCCESFULLY ADDED");window.location='/petshop_add_show'</script>'''
    data={}
    c="select * from pet_show_pet where pet_show_id='%s'"%(id)
    d=select(c)
    if d:
        data['view']=d

    if 'action' in request.args:
        action = request.args['action']
        idd = request.args['id']
        if action == 'update':
            e="select * from pet_show_pet where pet_show_pet_id='%s'"%(idd)
            f=select(e)
            if f:
                data['up']=f
                if 'update' in request.form:
                    name=request.form['name']
                    type=request.form['type']
                    breed=request.form['breed']
                    age=request.form['age']
                    gender=request.form['gender']
                    color=request.form['color']
                    size=request.form['size']
                    weight=request.form['weight']
                    coat=request.form['coat']
                    feature=request.form['feature']
                    owner=request.form['owner']
                    img=request.files['img']
                    path='static/'+str(uuid.uuid4())+img.filename
                    img.save(path)
                    g="update pet_show_pet set show_pet_name='%s',show_pet_type='%s',show_pet_breed='%s',show_pet_age='%s',show_pet_gender='%s', show_pet_color_pattern='%s',show_pet_size='%s',show_pet_weight='%s',show_pet_coat_type='%s',show_pet_feature='%s',show_pet_owner_name='%s',show_pet_image='%s' where pet_show_pet_id='%s' "%(name,type,breed,age,gender,color,size,weight,coat,feature,owner,path,idd)
                    h=update(g)
                    if g:
                        return'''<script>alert("SUCCESFULLY UPDATED");window.location='/petshop_add_show'</script>'''
        if action == 'delete':
            h="delete from pet_show_pet where pet_show_pet_id='%s'"%(idd)
            i=delete(h)
            if i:
                return'''<script>alert("SUCCESFULLY DELETED");window.location='/petshop_add_show'</script>'''
    return render_template('petshop_add_show_pet.html',data=data)





# if res: 
#      o="select * from stock where stock_id='%s'"%(res) 
#      e=select(o) 
#      if e: 
#       session['name']=e[0]['stock'] 
#      qr = qrcode.QRCode( 
#      version=1, 
#      error_correction=qrcode.constants.ERROR_CORRECT_L, 
#      box_size=10, 
#      border=4, 
#      ) 
#      qr.add_data(res) 
#      qr.make(fit=True) 
 
#      # Create an image of the QR code 
#      img = qr.make_image(fill_color="black", back_color="white") 
#      rr="static/qrcode/"+ session['name'] +".png" # Save the QR code image to a file 
#      img.save(rr) 
      
#      up="update stock set qr_code='%s' where stock_id='%s'"%(rr,res) 
#      update(up)


@petshop.route('/petshop_manage_profile', methods=['post', 'get'])
def petshop_manage_profile():
    data = {}
    a = "select * from pet_shop where pet_shop_id='%s'" % (session['shop'])
    b = select(a)
    if b:
        data['view'] = b
    
    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
        if action == 'update':
            c = "select * from pet_shop where pet_shop_id='%s'" % (id)
            d = select(c)
            if d:
                data['up'] = d
                if 'submit' in request.form:
                    sname = request.form['sname']
                    email = request.form['email']
                    phone = request.form['phone']
                    place = request.form['place']
                    address = request.form['address']
                    e = "update pet_shop set shop_name='%s', shop_email='%s', shop_phone='%s', shop_place='%s', shop_address='%s' where pet_shop_id='%s'" % (sname, email, phone, place, address, id)
                    f = update(e)
                    if f:
                        return '''<script>alert("SUCCESFULLY UPDATED");window.location='/petshop_manage_profile'</script>'''

    return render_template('petshop_manage_profile.html', data=data)
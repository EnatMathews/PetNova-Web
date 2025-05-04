from flask import*
from database import*

api=Blueprint('api',__name__)


@api.route('/loginapi', methods=['POST'])
def login():
    data = {}
    uname = request.form['username']  # Match Flutter's 'username'
    password = request.form['password']  # Match Flutter's 'password']
    query = "SELECT * FROM login WHERE user_name='%s' AND password='%s'" %(uname, password)
    result = select(query)
    print(result,"//////////////")
    
    if result:
        data['status'] = 'user'
        data['lid'] = result[0]['login_id']  # Assuming 'login_id' is the column name for lid
    else:
        data['status'] = 'failed'
    
    return jsonify(data)  # Return proper JSON



@api.route('/user_view_pets')
def user_view_pets():
    data = {}

    a = "SELECT * FROM pet"
    b = select(a)  # Assuming `select` returns a list of dictionaries

    if b:
        data['status'] = 'success'
        data['data'] = b  
    else:
        data['status'] = 'failed'
        data['data'] = []  # Always return a list to avoid Flutter errors

    return jsonify(data)  # ✅ Ensure response is JSON



@api.route('/user_view_petsittings')
def user_view_petsittings():
    data = {}

    a = "SELECT * FROM pet_sitting inner join login using(login_id) where user_type='pet_sitting'"
    b = select(a)  # Assuming `select` returns a list of dictionaries

    if b:
        data['status'] = 'success'
        data['data'] = b  
    else:
        data['status'] = 'failed'
        data['data'] = []  # Always return a list to avoid Flutter errors

    return jsonify(data)  # ✅ Ensure response is JSON


@api.route('/user_view_facility')
def user_view_facility():
    data = {}
    
    id=request.args['id']

    a = "SELECT * FROM facility where petsitting_id='%s'"%(id)
    b = select(a)  # Assuming `select` returns a list of dictionaries

    if b:
        data['status'] = 'success'
        data['data'] = b  
    else:
        data['status'] = 'failed'
        data['data'] = []  # Always return a list to avoid Flutter errors

    return jsonify(data)  # ✅ Ensure response is JSON


@api.route('/user_send_request')
def user_send_request():
    data = {}
    
    pet_sitting_id=request.args['id']
    lid=request.args['lid']
    stype=request.args['stype']
    rdes=request.args['rdes']
    
    c="select * from user where login_id='%s'"%(lid)
    d=select(c)
    uid=d[0]['user_id']
    a="insert into request values(null,'%s','%s','%s',curdate(),'pending','%s')"%(uid,stype,rdes,pet_sitting_id)
    bb=insert(a)
    

    if bb:
        data['status'] = 'success'
   
    else:
        data['status'] = 'failed'
   

    return jsonify(data)  # ✅ Ensure response is JSON


@api.route('/user_view_sent_requests')
def user_view_sent_requests():
    data = {}
    lid = request.args['lid']  # Login ID
    
    a = "SELECT * FROM request INNER JOIN pet_sitting USING(petsitting_id) WHERE user_id=(SELECT user_id FROM user WHERE login_id='%s')" % (lid)
    b = select(a)
    if b:
        data['status'] = 'success'
        data['data'] = b
    else:
        data['status'] = 'failed'
        data['data'] = []
    return jsonify(data)  # Assuming JSON response for consistency


@api.route('/user_view_proposal')
def user_view_proposal():
    data = {}
    request_id = request.args['rid']  # Login ID
    
    a="select * from proposal where request_id='%s'"%(request_id)
    b=select(a)
    
    if b:
        data['status'] = 'success'
        data['data'] = b
    else:
        data['status'] = 'failed'
        data['data'] = []
    return jsonify(data)  # Assuming JSON response for consistency



@api.route('/pay_proposal')
def pay_proposal():
    data = {}
    proposal_id = request.args['pid']  # Login ID
    amount = request.args['amount']  # Login ID
    
    a="insert into proposal_payment values(null,'%s','%s','paid',curdate())"%(proposal_id,amount)
    b=insert(a)
    
    z="update proposal set proposal_status='paid' where proposal_id='%s'"%(proposal_id)
    y=update(z)
    
    
 
    
    if b:
        data['status'] = 'success'
  
    else:
        data['status'] = 'failed'
    
    return jsonify(data)  # Assuming JSON response for consistency




@api.route('/user_addtocart')
def user_addtocart():
    data={}
    id=request.args['id']
    qty=request.args['qty']
    price=request.args['price']
    stock=request.args['stock']
    pid=request.args['pid']

    print(qty,stock,"///////////")

    if int(qty)>int(stock):
        print("out///")
        data['status']='Out Of Stock'

    else :
        print("/////")


        total=int(price)*int(qty)

        p="select * from user where login_id='%s'"%(id)
        q=select(p)
        if q:
            uid=q[0]['user_id']
            email = q[0]['user_email']

            x="select * from pet_master where pet_master_status='pending' and user_id='%s'"%(uid)
            y=select(x)
            if y:
                pmid=y[0]['pet_master_id']
                tamt=y[0]['pet_master_total']
                cartamt=int(total)+int(tamt)
                h="update pet_master set pet_master_total='%s' where pet_master_id='%s'"%(cartamt,pmid)
                update(h)
                xz="insert into pet_child values(null,'%s','%s','%s','%s')"%(pmid,pid,qty,price)
                yy=insert(xz)

            else:
                xx="insert into pet_master values(null,'%s','%s',curdate(),'pending')"%(uid,total)
                xy=insert(xx)

                xz="insert into pet_child values(null,'%s','%s','%s','%s')"%(xy,pid,qty,price)
                yy=insert(xz)


            
        
        if yy:
            data['status']='success'
            send_email_pet_cart(email)
            print(email,'///////////////////////')
        else:
            data['status']='failed'
    return str(data)


def send_email_pet_cart(to_email):
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('hariharan0987pp@gmail.com', 'rjcbcumvkpqynpep')

        msg = MIMEMultipart()
        msg['From'] = 'hariharan0987pp@gmail.com'
        msg['To'] = to_email
        msg['Subject'] = 'Registration Successful'

        body = 'Your item has been successfully added to your shopping cart. Happy shopping!'
        msg.attach(MIMEText(body, 'plain'))

        gmail.send_message(msg)
        gmail.quit()
        print("Email sent successfully")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise



@api.route('/user_view_products')
def user_view_products():
    data={}
    
    a="SELECT * FROM product"
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return jsonify(data)



@api.route('/user_addtocart_product',methods=['post','get'])
def user_addtocart_product():
    data = {}
    id = request.args['id']
    qty = request.args['qty']
    price = request.args['price']
    stock = request.args['stock']
    pid = request.args['pid']

    print(f"Received - ID: {id}, Qty: {qty}, Price: {price}, Stock: {stock}, Product ID: {pid}")

    if int(qty) > int(stock):
        print("Out of Stock!")
        data['status'] = 'Out Of Stock'
    else:
        total = int(price) * int(qty)

        # Fetch user details
        p = "SELECT * FROM user WHERE login_id='%s'" % (id)
        q = select(p)
        if q:
            uid = q[0]['user_id']
            email = q[0]['user_email']

            # Check if product_master entry exists for this user
            x = "SELECT * FROM product_master WHERE product_master_status='pending' AND user_id='%s'" % (uid)
            y = select(x)
            
            if y:
                pmid = y[0]['product_master_id']
                tamt = y[0]['product_master_total']
                cartamt = int(total) + int(tamt)

                h = "UPDATE product_master SET product_master_total='%s' WHERE product_master_id='%s'" % (cartamt, pmid)
                update(h)
                print(f"Updated product_master total: {cartamt} for PMID: {pmid}")

                xz = "INSERT INTO product_child VALUES(null,'%s','%s','%s','%s')" % (pmid, pid, qty, price)
                yy = insert(xz)
                print(f"Inserted into product_child: {yy}")

            else:
                xx = "INSERT INTO product_master VALUES(null,'%s','%s',CURDATE(),'pending')" % (uid, total)
                xy = insert(xx)
                print(f"New product_master created: {xy}")

                xz = "INSERT INTO product_child VALUES(null,'%s','%s','%s','%s')" % (xy, pid, qty, price)
                yy = insert(xz)
                print(f"Inserted into product_child: {yy}")

            if yy:
                data['status'] = 'success'
                send_email(email)
                print(f"Email sent to: {email}")
            else:
                data['status'] = 'failed'
    return jsonify(data)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask_mail import Mail, Message
import random
import string
import smtplib
from email.mime.text import MIMEText

def send_email(to_email):
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('hariharan0987pp@gmail.com', 'rjcbcumvkpqynpep')

        msg = MIMEMultipart()
        msg['From'] = 'hariharan0987pp@gmail.com'
        msg['To'] = to_email
        msg['Subject'] = 'successfully added to your shopping cart'

        body = 'Your item has been successfully added to your shopping cart. Happy shopping!'
        msg.attach(MIMEText(body, 'plain'))

        gmail.send_message(msg)
        gmail.quit()
        print("Email sent successfully")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise

@api.route('/user_view_pet_cart')
def user_view_pet_cart():
    data={}
    id=request.args['id']
    
    
    a="SELECT * FROM `pet_master` INNER JOIN `pet_child` USING(pet_master_id) INNER JOIN pet USING(pet_id) WHERE user_id=(select user_id from user where login_id='%s') AND pet_master_status='pending'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)


@api.route('/user_view_pet_order')
def user_view_pet_order():
    data={}
    id=request.args['id']
    
    
    a="SELECT * FROM `pet_master` INNER JOIN `pet_child` USING(pet_master_id) INNER JOIN pet USING(pet_id) WHERE user_id=(select user_id from user where login_id='%s') AND pet_master_status='paid'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)


@api.route('/user_view_product_order')
def user_view_product_order():
    data={}
    id=request.args['id']
    
    
    a="SELECT * FROM `product_master` INNER JOIN `product_child` USING (product_master_id) INNER JOIN product USING(product_id) WHERE user_id=(select user_id from user where login_id='%s') AND product_master_status='paid'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return jsonify(data)




@api.route('/user_view_product_cart')
def user_view_product_cart():
    data={}
    id=request.args['id']
    
    
    a="SELECT * FROM `product_master` INNER JOIN `product_child` USING (product_master_id) INNER JOIN product USING(product_id) WHERE user_id=(select user_id from user where login_id='%s') AND product_master_status='pending'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return jsonify(data)
@api.route('/pet_payment')
def pet_payment():
    data = {}
    
    # Get login_id from request arguments
    id = request.args.get('id')  # Fetch 'id' parameter (login_id)
    if not id:
        data['status'] = 'failed'
        data['message'] = 'Missing login ID'
        return str(data)

    # Fetch user email
    p = "SELECT * FROM user WHERE login_id='%s'" % (id)
    q = select(p)
    email = None  # Initialize email to avoid unbound error
    if q:
        email = q[0]['user_email']
    else:
        data['status'] = 'failed'
        data['message'] = 'User not found'
        return str(data)
   
    # Get other parameters
    amount = request.args.get('amount')
    bmid = request.args.get('pmid')

    if not amount or not bmid:
        data['status'] = 'failed'
        data['message'] = 'Missing amount or pet master ID'
        return str(data)

    # Insert payment record
    c = "INSERT INTO pet_payment VALUES (null, '%s', '%s', CURDATE())" % (bmid, amount)
    d = insert(c)
    
    if d:
        # Update pet master status
        stat = "UPDATE pet_master SET pet_master_status='paid' WHERE pet_master_id='%s'" % (bmid)
        update(stat)

        # Update pet stock
        e = "SELECT * FROM pet_child INNER JOIN pet_master USING(pet_master_id) INNER JOIN pet USING(pet_id) WHERE pet_master_id='%s'" % (bmid)
        f = select(e)

        for i in f:
            petid = i['pet_id']
            stk = i['pet_stock']
            pcqty = i['pet_child_quantity']
            upstock = int(stk) - int(pcqty)
            g = "UPDATE pet SET pet_stock='%s' WHERE pet_id='%s'" % (upstock, petid)
            update(g)

        data['status'] = 'success'
        send_email_pet_payment(email)  # Safe to use email here since it's set if we reach this point
        print(email, '///////////////////')
    else:
        data['status'] = 'failed'
        data['message'] = 'Failed to insert payment record'
    
    return str(data)


def send_email_pet_payment(to_email):
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('hariharan0987pp@gmail.com', 'rjcbcumvkpqynpep')

        msg = MIMEMultipart()
        msg['From'] = 'hariharan0987pp@gmail.com'
        msg['To'] = to_email
        msg['Subject'] = 'Payment Successful'

        body = 'Thank you for the purchase! Your order has been placed successfully. Happy shopping!'
        msg.attach(MIMEText(body, 'plain'))

        gmail.send_message(msg)
        gmail.quit()
        print("Email sent successfully")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise
    
    
@api.route('/remove_from_pet_cart')
def remove_from_pet_cart():
    data = {}
    id = request.args.get('id')  # pet_child_id
    
    # Fetch pet_child details before deletion
    child_query = "SELECT pet_master_id, pet_child_amount, pet_child_quantity FROM pet_child WHERE pet_child_id = %s" % (id)
    child_result = select(child_query)
    
    if not child_result:
        data['status'] = 'failed'
        data['message'] = 'Pet child item not found'
        return json.dumps(data)
    
    pmid = child_result[0]['pet_master_id']
    price_per_unit = float(child_result[0]['pet_child_amount'])  # Price per unit
    quantity = int(child_result[0]['pet_child_quantity'])  # Quantity
    amount_to_remove = price_per_unit * quantity  # Total cost to remove
    
    # Delete from pet_child
    delete_query = "DELETE FROM pet_child WHERE pet_child_id = %s" % (id)
    delete(delete_query)
    
    # Update pet_master_total
    total_query = "SELECT pet_master_total FROM pet_master WHERE pet_master_id = %s" % (pmid)
    total_result = select(total_query)
    
    if total_result:
        current_total = float(total_result[0]['pet_master_total'])
        new_total = max(0, current_total - amount_to_remove)
        
        if new_total > 0:
            update_query = "UPDATE pet_master SET pet_master_total = %s WHERE pet_master_id = %s" % (new_total, pmid)
            update(update_query)
        else:
            delete_master_query = "DELETE FROM pet_master WHERE pet_master_id = %s" % (pmid)
            delete(delete_master_query)
        
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
        data['message'] = 'Pet master not found'
    
    return json.dumps(data)


@api.route('/remove_from_product_cart')
def remove_from_product_cart():
    data = {}
    id = request.args.get('id')  # product_child_id
    
    # Fetch product_child details before deletion
    child_query = "SELECT product_master_id, product_child_amount, product_child_quantity FROM product_child WHERE product_child_id = %s" % (id)
    child_result = select(child_query)
    
    if not child_result:
        data['status'] = 'failed'
        data['message'] = 'Product child item not found'
        return json.dumps(data)
    
    pmid = child_result[0]['product_master_id']
    price_per_unit = float(child_result[0]['product_child_amount'])  # Price per unit
    quantity = int(child_result[0]['product_child_quantity'])  # Quantity
    amount_to_remove = price_per_unit * quantity  # Total cost to remove
    
    # Delete from product_child
    delete_query = "DELETE FROM product_child WHERE product_child_id = %s" % (id)
    delete(delete_query)
    
    # Update product_master_total
    total_query = "SELECT product_master_total FROM product_master WHERE product_master_id = %s" % (pmid)
    total_result = select(total_query)
    
    if total_result:
        current_total = float(total_result[0]['product_master_total'])
        new_total = max(0, current_total - amount_to_remove)
        
        if new_total > 0:
            update_query = "UPDATE product_master SET product_master_total = %s WHERE product_master_id = %s" % (new_total, pmid)
            update(update_query)
        else:
            delete_master_query = "DELETE FROM product_master WHERE product_master_id = %s" % (pmid)
            delete(delete_master_query)
        
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
        data['message'] = 'Product master not found'
    
    return json.dumps(data)

@api.route('/get_cart_total')
def get_cart_total():
    data = {}
    id = request.args.get('id')
    
    print(f"Received get_cart_total request for login_id: {id}")
    
    if not id:
        print("Error: No login_id provided")
        data["total"] = "0"
        return json.dumps(data)
    
    z = "SELECT * FROM user WHERE login_id = %s"%(id)
    y = select(z)
    if y and len(y) > 0:
        uid = y[0]['user_id']
        print(f"Found user_id: {uid} for login_id: {id}")
    else:
        print(f"No user found for login_id: {id}")
        data["total"] = "0"
        return json.dumps(data)
       
    query = "SELECT product_master_id, product_master_total FROM product_master WHERE user_id = %s AND product_master_status = 'pending'"%(uid,)
    result = select(query)
    print(f"Product master query result: {result}")

    if result and len(result) > 0:
        print(result)
        data["product_master_id"] = result[0]['product_master_id']
        data["total"] = result[0]['product_master_total']
        print(f"Returning total: {data['total']} with master_id: {data['product_master_id']}")
    else:
        print(f"No pending products found for user_id: {uid}")
        data["total"] = "0"
        

    response_json = json.dumps(data)
    print(f"Returning response: {response_json}")
    return response_json


@api.route('/get_pet_cart_total')
def get_pet_cart_total():
    data = {}
    id = request.args.get('id')
    
    print(f"Received get_pet_cart_total request for login_id: {id}")
    
    if not id:
        print("Error: No login_id provided")
        data["total"] = "0"
        return json.dumps(data)
    
    z = "SELECT * FROM user WHERE login_id = %s" % (id)
    y = select(z)
    if y and len(y) > 0:
        uid = y[0]['user_id']
        print(f"Found user_id: {uid} for login_id: {id}")
    else:
        print(f"No user found for login_id: {id}")
        data["total"] = "0"
        return json.dumps(data)
       
    query = "SELECT pet_master_id, pet_master_total FROM pet_master WHERE user_id = %s AND pet_master_status = 'pending'" % (uid,)
    result = select(query)
    print(f"Pet master query result: {result}")

    if result and len(result) > 0:
        print(result)
        data["pet_master_id"] = result[0]['pet_master_id']
        data["total"] = result[0]['pet_master_total']
        print(f"Returning total: {data['total']} with master_id: {data['pet_master_id']}")
    else:
        print(f"No pending pets found for user_id: {uid}")
        data["total"] = "0"
        
    response_json = json.dumps(data)
    print(f"Returning response: {response_json}")
    return response_json

@api.route('/product_payment')
def product_payment():
    data = {}
    
    amount = request.args.get('amount')
    pmid = request.args.get('pmid')
    print(f"Received payment confirmation - Amount: {amount}, Master ID: {pmid}")
    
    if not amount or not pmid:
        print("Error: Missing amount or master ID")
        data["status"] = "failed"
        return json.dumps(data)
    
    user_query = "SELECT user_id FROM product_master WHERE product_master_id = %s"%(pmid,)
    user_result = select(user_query)
    
    if not user_result or len(user_result) == 0:
        print(f"No product master found with ID: {pmid}")
        data["status"] = "failed"
        return json.dumps(data)
    
    user_id = user_result[0]['user_id']
    
    email_query = "SELECT user_email FROM user WHERE user_id = %s"%(user_id,)
    email_result = select(email_query)
    
    if email_result and len(email_result) > 0:
        email = email_result[0]['user_email']
        print(f"Found email: {email} for user_id: {user_id}")
    else:
        print(f"No email found for user_id: {user_id}")
        email = None
    
    try:
        c = "INSERT INTO product_payment VALUES (null, %s, %s, CURDATE())"% (pmid, amount)
        d = insert(c)
        
        if d:
            stat = "UPDATE product_master SET product_master_status = 'paid' WHERE product_master_id = %s"%(pmid,)
            update(stat)
            print(f"Updated product_master status to 'paid' for ID: {pmid}")
            
            e = "SELECT * FROM product_child INNER JOIN product_master USING(product_master_id) INNER JOIN product USING(product_id) WHERE product_master_id = %s"% (pmid,)
            f = select(e)
            
            for i in f:
                proid = i['product_id']
                stk = i['product_stock']
                pcqty = i['product_child_quantity']
                upstock = int(stk) - int(pcqty)
                
                g = "UPDATE product SET product_stock = %s WHERE product_id = %s"% (upstock, proid)
                update(g)
                print(f"Updated stock for product_id: {proid} from {stk} to {upstock}")
            
            if email:
                try:
                    send_email_product_payment(email)
                    print(f"Confirmation email sent to: {email}")
                except Exception as e:
                    print(f"Failed to send email: {str(e)}")
            
            data['status'] = 'success'
        else:
            data['status'] = 'failed'
            print("Failed to insert payment record")
    
    except Exception as e:
        print(f"Error processing payment: {str(e)}")
        data['status'] = 'failed'
    
    response_json = json.dumps(data)
    print(f"Returning payment response: {response_json}")
    return response_json


def send_email_product_payment(to_email):
    try:
        print("Sending confirmation email to:", to_email)
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login('hariharan0987pp@gmail.com', 'rjcbcumvkpqynpep')

        msg = MIMEMultipart()
        msg['From'] = 'hariharan0987pp@gmail.com'
        msg['To'] = to_email
        msg['Subject'] = 'Payment Successful'

        body = 'Thank you for the purchase! Your order has been placed successfully. Happy shopping!'
        msg.attach(MIMEText(body, 'plain'))

        gmail.send_message(msg)
        gmail.quit()
        print("Email sent successfully")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        raise


@api.route('/user_view_doctor')
def user_view_doctor():
    data={}
    
    a="SELECT * FROM doctor inner join fees using(doctor_id)"
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return jsonify(data)


@api.route('/user_doctor_chat')
def user_doctor_chat():
    data={}
    sender_id=request.args['sender_id']
    receiver_id=request.args['receiver_id']
    details=request.args['details']


    a="insert into chat values(null,'%s' ,'user','%s','doctor','%s',curdate(),curtime())"%(sender_id,receiver_id,details)
    res=insert(a)
    if res:
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="chat"

    return str(data)

@api.route('/doctor_chat_details')
def doctor_chat_details():
    data={}
    sender_id=request.args['sender_id']
    receiver_id=request.args['receiver_id']

    f="SELECT * FROM chat WHERE sender_id='%s'  AND receiver_id='%s' UNION SELECT * FROM chat WHERE sender_id='%s' AND receiver_id='%s' ORDER BY chat_date , chat_time"%(sender_id,receiver_id,receiver_id,sender_id)
    rg=select(f)
    if rg:
        data['status']="success"
        data['data']=rg
    else:
        data['status']="failed"
    data['method']="chatdetail"
    return str(data)


@api.route('/doc_schedule')
def doc_schedule():
    data={}
   
    did=request.args['docid']
    a="select * from schedule where doctor_id='%s'"%(did)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
  
    return str(data)

@api.route('/book_appointment')
def book_appointment():
    data={}
    id=request.args['id']
    did=request.args['docid']
    a="insert into appointment values(null,(select user_id from user where login_id='%s'),curdate(),curtime(),'pending','%s')"%(id,did)
    b=insert(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='send'
    return str(data)

from flask import jsonify  # Ensure this is imported

@api.route('/user_view_appointment')
def user_view_appointment():
    data = {}
    id = request.args['id']
    
    a = "SELECT * FROM `appointment` INNER JOIN `doctor` USING(doctor_id) INNER JOIN `fees` USING(doctor_id) WHERE user_id=(select user_id from user where login_id='%s') group by appointment_id" % (id)
    b = select(a)
    if b:
        data['status'] = 'success'
        data['data'] = b  
    else:
        data['status'] = 'failed'
    data['method'] = 'view'
    return jsonify(data)  # Use jsonify instead of str

@api.route('/user_view_slot')
def user_view_slot():
    data={}
    id=request.args['id']
    
    a="SELECT * FROM slot where appointment_id='%s'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)


@api.route('/appointment_payment')
def appointment_payment():
    data={}
    id=request.args['id']
    amount=request.args['amount']
    did=request.args['did']
    apid=request.args['apid']

    c="insert into doctor_payment values(null,'%s','%s',curdate(),(select user_id from user where login_id='%s'))"%(did,amount,id)
    d=insert(c)
    if d:
        e="update appointment set appointment_status='Paid' where appointment_id='%s'"%(apid)
        update(e)
    if d:
        data['status']='success'
    else:
        data['status']='failed'

    return str(data)

from flask import request, jsonify
from database import insert, select  # Ensure correct import based on your setup

@api.route('/user_send_complaint', methods=['GET'])
def user_send_complaint():
    data = {}
    
    # Ensure required parameters exist
    if 'id' not in request.args or 'complaint' not in request.args:
        return jsonify({'status': 'failed', 'message': 'Missing parameters'})

    try:
        id = request.args['id']
        complaint = request.args['complaint']

        # Use parameterized query to prevent SQL injection
        query = "INSERT INTO complaint (login_id, complaint, complaint_reply, complaint_date) VALUES ('%s', '%s', 'pending', CURDATE())"%(id, complaint)
        result = insert(query)

        if result:
            data['status'] = 'success'
        else:
            data['status'] = 'failed'
    except Exception as e:
        data['status'] = 'error'
        data['message'] = str(e)
        
        print(e)

    return jsonify(data)

@api.route('/user_view_reply', methods=['GET'])
def user_view_reply():
    data = {}

    if 'id' not in request.args:
        return jsonify({'status': 'failed', 'message': 'Missing ID parameter'})

    try:
        id = request.args['id']
        query = "SELECT * FROM complaint WHERE login_id = %s"% (id)
        result = select(query)

        if result:
            data['status'] = 'success'
            data['data'] = result
        else:
            data['status'] = 'failed'
    except Exception as e:
        data['status'] = 'error'
        data['message'] = str(e)

    return jsonify(data)


@api.route('/user_send_feedback')
def user_send_feedback():
    data={}
    id=request.args['id']
    feedback=request.args['feedback']
    a="insert into feedback values(null,'%s','%s',curdate())"%(id,feedback)
    b=insert(a)
    if b:
        data['status']='success'
        data['data']=b
    else:
        data['status']='failed'
    return jsonify(data)


@api.route('/user_register')
def user_register():
    data = {}
    fname = request.args['fname']
    lname = request.args['lname']
    phone = request.args['phone']
    email = request.args['email']
    place = request.args['place']
    address = request.args['address']
    uname = request.args['uname']
    password = request.args['pwd']
   
    a = "insert into login values(null,'%s','%s','user')" % (uname, password)
    b = insert(a)
    c = "insert into user values(null,'%s','%s','%s','%s','%s','%s','%s')" % (b, fname, lname, phone, email, place, address)
    d = insert(c)

    if d:
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    
    return jsonify(data)  # Return JSON instead of str(data)
from datetime import datetime
@api.route('/user_viwe_petshow')
def user_viwe_petshow():
    data={}
    current_date = datetime.now().strftime('%Y-%m-%d')
    a="SELECT * FROM pet_show WHERE show_date >= '%s'"%(current_date)
    b=select(a)
    print(b)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return jsonify(data)

@api.route('/user_view_show_pet')
def user_view_show_pet():
    data={}
    id=request.args['id']
    a="SELECT * FROM pet_show_pet where pet_show_id='%s'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)


import uuid
from test import predicts
@api.route('/api/share_illness/',methods=['get','post'])
def share_illness():
    data={}
    
    image=request.files['image']
    path1="static/predict/"+str(uuid.uuid4())+image.filename
    image.save(path1)

    print(path1,"///////////")

    a=predicts(path1)

    print(a,"////////////////////////////////////////////////")

    if a:

        data['status']='success'
        data['data']=a
    else:
        data['status']='failed'

    return str(data)


from predict import*
@api.route('/predict_symptoms')
def predict_symptoms():
    data={}
    type=request.args['type']
    breed=request.args['breed']
    age=request.args['age']
    gender=request.args['gender']
    weight=request.args['weight']
    sym1=request.args['sym1']
    sym2=request.args['sym2']
    sym3=request.args['sym3']
    sym4=request.args['sym4']
    durat=request.args['durat']
    apploss=request.args['apploss']
    vomiting=request.args['vomiting']
    diarrhea=request.args['diarrhea']
    coughing=request.args['coughing']
    breathing=request.args['breathing']
    lameness=request.args['lameness']
    skin=request.args['skin']
    naseldis=request.args['naseldis']
    eyedis=request.args['eyedis']
    tempr=request.args['tempr']
    hrate=request.args['hrate']

    print(type,breed,age,gender,weight,sym1,sym2,sym3,sym4,durat,apploss,vomiting,diarrhea,coughing,breathing,lameness,skin,naseldis,eyedis,tempr,hrate)
    a=predict_disease_from_input(type,breed,age,gender,weight,sym1,sym2,sym3,sym4,durat,apploss,vomiting,diarrhea,coughing,breathing,lameness,skin,naseldis,eyedis,tempr,hrate)
    print(a)
  
    if a:
        data['status']='success'
        data['result']=a
    else:
        data['status']='failed'
    return str(data)


@api.route('/user_view_scanner_result')
def user_view_scanner_result():
    data={}
    id=request.args['id']
    a="SELECT * FROM pet_show_pet where pet_show_pet_id='%s'"%(id)
    b=select(a)
    if b:
        data['status']='success'
        data['data']=b  
    else:
        data['status']='failed'
    data['method']='view'
    return str(data)

# ********************************************************************


@api.route('/user_view_chat')
def user_view_chat():
    data = {}
    lid = request.args['lid']  # Login ID
    pid = request.args['pid']  # Pet Sitting ID
    
    # Fetch user_id from login_id
    u_query = "SELECT user_id FROM user WHERE login_id='%s'" % (lid)
    u_result = select(u_query)
    if not u_result:
        data['status'] = 'failed'
        data['message'] = 'User not found'
        return jsonify(data)
    user_id = u_result[0]['user_id']


    x="select * from pet_sitting where petsitting_id='%s'"%(pid)
    bb=select(x)
    plid=bb[0]['login_id']
    
    # Fetch chat messages
    a = "SELECT * FROM chat WHERE (sender_id='%s' AND sender_type='user' AND receiver_id='%s' AND receiver_type='pet_sitting') OR (sender_id='%s' AND sender_type='pet_sitting' AND receiver_id='%s' AND receiver_type='user')" % (lid, plid, plid, lid)
    b = select(a)
    if b:
        data['status'] = 'success'
        data['data'] = b
    else:
        data['status'] = 'success'  # Still success if no messages
        data['data'] = []
    return jsonify(data)


@api.route('/user_send_chat')
def user_send_chat():
    data = {}
    lid = request.args['lid']  # Login ID
    pid = request.args['pid']  # Pet Sitting ID
    msg = request.args['msg']  # Message

    x="select * from pet_sitting where petsitting_id='%s'"%(pid)
    bb=select(x)
    plid=bb[0]['login_id']
    
    # Fetch user_id from login_id
    u_query = "SELECT user_id FROM user WHERE login_id='%s'" % (lid)
    u_result = select(u_query)
    if not u_result:
        data['status'] = 'failed'
        data['message'] = 'User not found'
        return jsonify(data)
    user_id = u_result[0]['user_id']
    
    # Insert chat message
    a = "INSERT INTO chat VALUES (null, '%s', 'user', '%s', 'pet_sitting', '%s', CURDATE(), CURTIME())" % (lid, plid, msg)
    b = insert(a)
    if b:
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    return jsonify(data)




@api.route('/user_view_doctor_chat')
def user_view_doctor_chat():
    data = {}
    lid = request.args['lid']  # Login ID
    did = request.args['did']  # Doctor ID
    
    # Fetch user_id from login_id
    u_query = "SELECT user_id FROM user WHERE login_id='%s'" % (lid)
    u_result = select(u_query)
    if not u_result:
        data['status'] = 'failed'
        data['message'] = 'User not found'
        return jsonify(data)
    user_id = u_result[0]['user_id']
    
    # Fetch chat messages
    a = "SELECT * FROM chat WHERE (sender_id='%s' AND sender_type='user' AND receiver_id='%s' AND receiver_type='doctor') OR (sender_id='%s' AND sender_type='doctor' AND receiver_id='%s' AND receiver_type='user')" % (user_id, did, did, user_id)
    b = select(a)
    if b:
        data['status'] = 'success'
        data['data'] = b
    else:
        data['status'] = 'success'  # Still success if no messages
        data['data'] = []
    return jsonify(data)



@api.route('/user_send_doctor_chat')
def user_send_doctor_chat():
    data = {}
    lid = request.args['lid']  # Login ID
    did = request.args['did']  # Doctor ID
    msg = request.args['msg']  # Message
    
    # Fetch user_id from login_id
    u_query = "SELECT user_id FROM user WHERE login_id='%s'" % (lid)
    u_result = select(u_query)
    if not u_result:
        data['status'] = 'failed'
        data['message'] = 'User not found'
        return jsonify(data)
    user_id = u_result[0]['user_id']
    
    # Insert chat message
    a = "INSERT INTO chat VALUES (null, '%s', 'user', '%s', 'doctor', '%s', CURDATE(), CURTIME())" % (user_id, did, msg)
    b = insert(a)
    if b:
        data['status'] = 'success'
    else:
        data['status'] = 'failed'
    return jsonify(data)





@api.route('/api/scan_qr', methods=['POST'])
def scan_qr():
    data = {}
    try:
        qr_data = request.form.get('qr_data')  # Get QR code data from Flutter
        print(f"Received QR code data: {qr_data}")  # Print to Flask logs
        
        # Example: Process QR data (e.g., fetch pet/product info)
        # Here, we'll just echo it back for simplicity
        response_data = {"received_qr": qr_data, "message": "Data processed"}
        
        z="select * from pet_show_pet where pet_show_pet_id='%s'"%(qr_data)
        y=select(z)
        if y:
            data['status']='success'
            data['data']=y
        else:
            data['status']='failed'
            data['message']='No data found'
        
      
    except Exception as e:
        print(f"Error processing QR code: {e}")
        data['status'] = 'failed'
        data['message'] = str(e)
    
    return json.dumps(data)  # Return JSON response


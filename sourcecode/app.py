from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://codeusername:CodePassword@testcluster.sl9ku.mongodb.net/test")
db = client.get_database('total_records')
records = db.register

majors = ['Aerospace Engineering', 'Architecural Engineering', 'Chemical Engineering', 'Civil Engineering',
         'Computer Engineering', 'Computer Science', 'Construction Engineering', 'Cyber Security', 
         'Electircal Engineering', 'Environmental Engineering', 'Mechanical Engineering', 'Metallurgical Engineering',
         'Musical Audio Engineering']
# majors = majors.reverse()

@app.route('/', methods=['post', 'get'])
def index():
    if request.method == "POST":
        return redirect(url_for('register'))
    return render_template('index.html')

@app.route("/register", methods=['post', 'get'])
def register():
    global majors 
    majors.reverse()
    message = ''
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        first = request.form.get("firstname")
        last = request.form.get("lastname")
        email = request.form.get("email")
        
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        major = request.form.get("major")
        
        # user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        
        if first == "":
            message = 'Please enter your first name'
            return render_template('register.html', message=message)
        elif last == "":
            message = 'Please enter your last name'
            return render_template('register.html', message=message)
        elif email == "":
            message = 'Please enter your email'
            return render_template('register.html', message=message)
        elif major == "":
            message = 'Please enter your major'
            return render_template('register.html', message=message)
        elif email_found:
            message = 'This email already exists in database'
            return render_template('register.html', message=message)
        elif password1 != password2:
            message = 'Passwords should match!'
            return render_template('register.html', message=message)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'firstname': first, 'lastname': last, 'email': email, 'password': hashed, 'major': major}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            session["email"] = new_email
   
            return render_template('logged_in.html', email=new_email)
    return render_template('register.html', majors=majors)

@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

       
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)

        return render_template("signout.html")
    else:
        return render_template('index.html')

@app.route("/flowchart", methods=['post', 'get'])
def flowchart():
    if request.method == "POST":
        name = request.form.get("flowchartname")
        d1 = request.form.get("d1")
        d2 = request.form.get("d2")
        d3 = request.form.get("d3")
        d4 = request.form.get("d4")
        d5 = request.form.get("d5")
        d6 = request.form.get("d6")
        d7 = request.form.get("d7")
        d8 = request.form.get("d8")
        d9 = request.form.get("d9")
        d10 = request.form.get("d10")
        d11 = request.form.get("d11")
        d12 = request.form.get("d12")
        d13 = request.form.get("d13")
        d14 = request.form.get("d14")
        d15 = request.form.get("d15")
        d16 = request.form.get("d16")
        d17 = request.form.get("d17")
        d18 = request.form.get("d18")
        d19 = request.form.get("d19")
        d20 = request.form.get("d20")
        d21 = request.form.get("d21")
        d22 = request.form.get("d22")
        d23 = request.form.get("d23")
        d24 = request.form.get("d24")
        d25 = request.form.get("d25")
        d26 = request.form.get("d26")
        d27 = request.form.get("d27")
        d28 = request.form.get("d28")
        d29 = request.form.get("d29")
        d30 = request.form.get("d30")
        d31 = request.form.get("d31")
        d32 = request.form.get("d32")
        d33 = request.form.get("d33")
        d34 = request.form.get("d34")
        d35 = request.form.get("d35")
        d36 = request.form.get("d36")
        d37 = request.form.get("d37")
        new = request.form.get("newflowchart")
        name_found = records.find_one({name: {"$exists": True}})
        if (name == ""):
            message = 'Please enter a name for your flowchart'
            return render_template('flowchart.html', message=message)
        elif (name_found and (new == True)):
            message = 'You already have a flowchart named ' + name
            return render_template('flowchart.html', message=message, namefound=name_found)
        else: 
            email = session["email"]
            if (new == True):
                # records.update_one(
                #     {"email": email},
                #     {"$set": {name: [name, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27,d28, d29, d30, d31, d32, d33, d34, d35, d36, d37]}}
                # )
                records.update_one(
                    {"email": email},
                    {"$push": {
                        "flowcharts": {
                            "$each": [{ "name": name, 
                                        "1": d1, "2": d2, "3": d3, "4": d4, "5": d5,
                                        "6": d6, "7": d7, "8": d8, "9": d9, 
                                        "10": d10, "11": d11, "12": d12, "13": d13,
                                        "14": d14, "15": d15, "16": d16, "17": d17, "18": d18,
                                        "19": d19, "20": d20, "21": d21, "22": d22, "23": d23,
                                        "24": d24, "25": d25, "26": d26, "27": d27, "28": d28,
                                        "29": d29, "30": d30, "31": d31, "32": d32, "33": d33,
                                        "34": d34, "35": d35, "36": d36, "37": d37}],
                            "$position": 0
                        }
                    }
                    })
            else:
                entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
                newData = []
                len = 0
                for item in entry:
                    for thing in item['flowcharts']:
                        len += 1
                    for i in range(len):
                        if (item['flowcharts'][i]["name"] == name):
                            item['flowcharts'][i]["1"] = d1
                            item['flowcharts'][i]["2"] = d2
                            item['flowcharts'][i]["3"] = d3
                            item['flowcharts'][i]["4"] = d4
                            item['flowcharts'][i]["5"] = d5
                            item['flowcharts'][i]["6"] = d5
                            item['flowcharts'][i]["7"] = d6
                            item['flowcharts'][i]["8"] = d7
                            item['flowcharts'][i]["9"] = d8
                            item['flowcharts'][i]["10"] = d9
                            item['flowcharts'][i]["11"] = d10
                            item['flowcharts'][i]["12"] = d11
                            item['flowcharts'][i]["13"] = d12
                            item['flowcharts'][i]["14"] = d13
                            item['flowcharts'][i]["15"] = d14
                            item['flowcharts'][i]["16"] = d15
                            item['flowcharts'][i]["17"] = d16
                            item['flowcharts'][i]["18"] = d17
                            item['flowcharts'][i]["19"] = d18
                            item['flowcharts'][i]["10"] = d19
                            item['flowcharts'][i]["20"] = d20
                            item['flowcharts'][i]["21"] = d21
                            item['flowcharts'][i]["22"] = d22
                            item['flowcharts'][i]["23"] = d23
                            item['flowcharts'][i]["24"] = d24
                            item['flowcharts'][i]["25"] = d25
                            item['flowcharts'][i]["26"] = d26
                            item['flowcharts'][i]["27"] = d27
                            item['flowcharts'][i]["28"] = d28
                            item['flowcharts'][i]["29"] = d29
                            item['flowcharts'][i]["30"] = d30
                            item['flowcharts'][i]["31"] = d31
                            item['flowcharts'][i]["32"] = d32
                            item['flowcharts'][i]["33"] = d33
                            item['flowcharts'][i]["34"] = d34
                            item['flowcharts'][i]["35"] = d35
                            item['flowcharts'][i]["36"] = d36
                            item['flowcharts'][i]["37"] = d37
                        newData.append(item['flowcharts'][i])

                records.update_one(
                    {"email": email},
                    {"$set": {"flowcharts": newData}}
                )
            message = 'Your flowchart has been saved'
            return render_template('flowchart.html', message=message)
    if "email" in session: # GET
        email = session["email"]
        array = records.find_one({"email": email}, {"_id": 0, "firstname": 0, "lastname": 0, "email": 0, "password": 0, "major": 0})
        array1 = 0
        for item in array: 
            array1 += 1
        return render_template('flowchart.html', new=True, array=array, array1=array1)
    else:
        return redirect(url_for("login"))

#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)
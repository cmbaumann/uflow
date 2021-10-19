from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://codeusername:CodePassword@testcluster.sl9ku.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")

db = client.get_database('total_records')
records = db.register

majors = ['Aerospace Engineering', 'Architecural Engineering', 'Chemical Engineering', 'Civil Engineering',
         'Computer Engineering', 'Computer Science', 'Construction Engineering', 'Cyber Security', 
         'Electircal Engineering', 'Environmental Engineering', 'Mechanical Engineering', 'Metallurgical Engineering',
         'Musical Audio Engineering']

years = [2017, 2018, 2019, 2020, 2021, 2022, 2023]

@app.route('/', methods=['post', 'get'])
def index():
    if request.method == "POST":
        return redirect(url_for('register'))
    return render_template('index.html')

@app.route("/register", methods=['post', 'get'])
def register():
    global majors 
    majors.reverse()
    global years
    years.reverse()
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
        year = request.form.get("year")
        
        email_found = records.find_one({"email": email})
        
        if first == "":
            message = 'Please enter your first name'
            return render_template('register.html', message=message, majors=majors, years=years, last=last, email=email, password1=password1, password2=password2, selectedmajor=major, selectedyear=year)
        elif last == "":
            message = 'Please enter your last name'
            return render_template('register.html', message=message, majors=majors, years=years, first=first, email=email, password1=password1, password2=password2, selectedmajor=major, selectedyear=year)
        elif email == "":
            message = 'Please enter your email'
            return render_template('register.html', message=message, majors=majors, years=years, first=first, last=last, password1=password1, password2=password2, selectedmajor=major, selectedyear=year)
        elif (password1 == "") or (password2 == ""):
            message = 'Passwords do not match'
            return render_template('register.html', message=message, majors=majors, years=years, first=first, last=last, email=email, selectedmajor=major, selectedyear=year)
        elif email_found:
            message = 'There is already an account associated with this email'
            return render_template('register.html', message=message, majors=majors, years=years, first=first, last=last, password1=password1, password2=password2, selectedmajor=major, selectedyear=year)
        elif password1 != password2:
            message = 'Passwords do not match'
            return render_template('register.html', message=message, majors=majors, years=years, first=first, last=last, email=email, selectedmajor=major, selectedyear=year)
        else:
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            user_input = {'firstname': first, 'lastname': last, 'email': email, 'password': hashed, 'major': major, 'year': year, 'flowcharts': []}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            session["email"] = new_email
   
            return render_template('logged_in.html', email=new_email)
    return render_template('register.html', majors=majors, years=years)

@app.route('/logged_in', methods=['post', 'get'])
def logged_in():
    if request.method == "POST":
        name = request.form.get("name")
        email = session["email"]

        entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
        newData = []
        len = 0
        for item in entry:
            for thing in item['flowcharts']:
                len += 1
            for i in range(len):
                if (item['flowcharts'][i]["name"] != name):
                    newData.append(item['flowcharts'][i])
        print(newData)
        records.update_one(
            {"email": email},
            {"$set": {"flowcharts": newData}}
        )

        names = []
        len = 0
        entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
        for item in entry:
                for thing in item['flowcharts']:
                    len = len + 1
                for i in range(0, len):
                    names.append(item['flowcharts'][i]["name"])
        return render_template('logged_in.html', email=email, names=names)
    if "email" in session:
        email = session["email"]
        names = []
        len = 0
        entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
        for item in entry:
                for thing in item['flowcharts']:
                    len = len + 1
                for i in range(0, len):
                    names.append(item['flowcharts'][i]["name"])
        return render_template('logged_in.html', email=email, names=names)
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

@app.route("/flowchart-new", methods=['post', 'get'])
def flowchart1():
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

        #checking if name is found
        email = session["email"]
        entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
        len = 0
        name_found = False
        for item in entry:
            for thing in item['flowcharts']:
                len += 1
                for i in range(len):
                    if (item['flowcharts'][i]["name"] == name):
                        name_found = True
                        break

        if (name == ""):
            message = 'Please enter a name for your flowchart'
            return render_template('flowchart-new.html', message=message)
        elif (name_found):
            message = 'You already have a flowchart named ' + name
            return render_template('flowchart-new.html', message=message)
        else: 
            email = session["email"]
            len = 0
            entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
            for item in entry:
                for thing in item['flowcharts']:
                    len += 1
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
                        "$position": len
                    }
                }
            })   
            message = 'Your flowchart has been saved'
            return redirect(url_for('flowchart2', name=name))#render_template('flowchart-edit.html', message=message, name=name)
    if "email" in session: # GET
        return render_template('flowchart-new.html')
    else:
        return redirect(url_for("login"))

@app.route("/flowchart-edit/<name>", methods=['post', 'get'])
def flowchart2(name):
    if request.method == "POST":
        print("name: ", name)
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

        email = session["email"]
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
                    item['flowcharts'][i]["6"] = d6
                    item['flowcharts'][i]["7"] = d7
                    item['flowcharts'][i]["8"] = d8
                    item['flowcharts'][i]["9"] = d9
                    item['flowcharts'][i]["10"] = d10
                    item['flowcharts'][i]["11"] = d11
                    item['flowcharts'][i]["12"] = d12
                    item['flowcharts'][i]["13"] = d13
                    item['flowcharts'][i]["14"] = d14
                    item['flowcharts'][i]["15"] = d15
                    item['flowcharts'][i]["16"] = d16
                    item['flowcharts'][i]["17"] = d17
                    item['flowcharts'][i]["18"] = d18
                    item['flowcharts'][i]["19"] = d19
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
        data = []
        data.append(name)
        data.append(d1)
        data.append(d2)
        data.append(d3)
        data.append(d4)
        data.append(d5)
        data.append(d6)
        data.append(d7)
        data.append(d8)
        data.append(d9)
        data.append(d10)
        data.append(d11)
        data.append(d12)
        data.append(d13)
        data.append(d14)
        data.append(d15)
        data.append(d16)
        data.append(d16)
        data.append(d17)
        data.append(d18)
        data.append(d19)
        data.append(d20)
        data.append(d21)
        data.append(d22)
        data.append(d23)
        data.append(d24)
        data.append(d25)
        data.append(d26)
        data.append(d27)
        data.append(d28)
        data.append(d29)
        data.append(d30)
        data.append(d31)
        data.append(d32)
        data.append(d33)
        data.append(d34)
        data.append(d35)
        data.append(d36)
        data.append(d37)
        print("data: ", data)
        records.update_one(
            {"email": email},
            {"$set": {"flowcharts": newData}}
        )
        message = 'Your flowchart has been saved'
        year = records.find({"email": email}, {"year": 1, "_id": 0})
        for item in year:
            yearPass = item['year']
        yearPass2 = int(yearPass)+1
        yearPass3 = int(yearPass)+2
        yearPass4 = int(yearPass)+3
        yearPass5 = int(yearPass)+4
        yearData = []
        yearData.append(int(yearPass))
        yearData.append(yearPass2)
        yearData.append(yearPass3)
        yearData.append(yearPass4)
        yearData.append(yearPass5)
        return render_template('flowchart-edit.html', message=message, name=name, data=data, yearData=yearData)
    if "email" in session: # GET
        print("edit name: ", name)
        email = session["email"]
        entry = records.find({"email": email}, {"flowcharts": 1, "_id": 0})
        data = []
        len = 0
        for item in entry:
            for thing in item['flowcharts']:
                len += 1
            for i in range(len):
                if (item['flowcharts'][i]["name"] == name):
                    data.append(name)
                    data.append(item['flowcharts'][i]["1"])
                    data.append(item['flowcharts'][i]["2"])
                    data.append(item['flowcharts'][i]["3"])
                    data.append(item['flowcharts'][i]["4"])
                    data.append(item['flowcharts'][i]["5"])
                    data.append(item['flowcharts'][i]["6"])
                    data.append(item['flowcharts'][i]["7"])
                    data.append(item['flowcharts'][i]["8"])
                    data.append(item['flowcharts'][i]["9"])
                    data.append(item['flowcharts'][i]["10"])
                    data.append(item['flowcharts'][i]["11"])
                    data.append(item['flowcharts'][i]["12"])
                    data.append(item['flowcharts'][i]["13"])
                    data.append(item['flowcharts'][i]["14"])
                    data.append(item['flowcharts'][i]["15"])
                    data.append(item['flowcharts'][i]["16"])
                    data.append(item['flowcharts'][i]["17"])
                    data.append(item['flowcharts'][i]["18"])
                    data.append(item['flowcharts'][i]["19"])
                    data.append(item['flowcharts'][i]["10"])
                    data.append(item['flowcharts'][i]["20"])
                    data.append(item['flowcharts'][i]["21"])
                    data.append(item['flowcharts'][i]["22"])
                    data.append(item['flowcharts'][i]["23"])
                    data.append(item['flowcharts'][i]["24"])
                    data.append(item['flowcharts'][i]["25"])
                    data.append(item['flowcharts'][i]["26"])
                    data.append(item['flowcharts'][i]["27"])
                    data.append(item['flowcharts'][i]["28"])
                    data.append(item['flowcharts'][i]["29"])
                    data.append(item['flowcharts'][i]["30"])
                    data.append(item['flowcharts'][i]["31"])
                    data.append(item['flowcharts'][i]["32"])
                    data.append(item['flowcharts'][i]["33"])
                    data.append(item['flowcharts'][i]["34"])
                    data.append(item['flowcharts'][i]["35"])
                    data.append(item['flowcharts'][i]["36"])
                    data.append(item['flowcharts'][i]["37"])
        year = records.find({"email": email}, {"year": 1, "_id": 0})
        for item in year:
            yearPass = item['year']
        yearPass2 = int(yearPass)+1
        yearPass3 = int(yearPass)+2
        yearPass4 = int(yearPass)+3
        yearPass5 = int(yearPass)+4
        yearData = []
        yearData.append(int(yearPass))
        yearData.append(yearPass2)
        yearData.append(yearPass3)
        yearData.append(yearPass4)
        yearData.append(yearPass5)
        print("GET data: ", data)
        return render_template('flowchart-edit.html', data=data, yearData=yearData)
    else:
        return redirect(url_for("login"))

#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)
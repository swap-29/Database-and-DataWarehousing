from datetime import datetime    
from flask import render_template, flash, request, redirect ,Flask    
import pypyodbc      
from datetime import datetime   

app = Flask(__name__)
app.secret_key = 'secret key'

   
# creating connection Object which will contain SQL Server Connection    
connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=SWAPNIL;Database=Fact_db;uid=skamate;pwd=dbdw@123')# Creating Cursor    
    
cursor = connection.cursor()    
    
@app.route('/')
def main_page():
    return render_template("main.html")   


@app.route("/form_submit", methods=['POST'])
def back_call():
    query = request.form.getlist('text')[0]
    query = query.lower()
    x = query.split(" ")[0]

    if x =="select":
        cursor.execute(query)
        records = [tuple(i[0] for i in cursor.description)]

        for row in cursor:
            records.append(row)
        return render_template("display.html", values  = records)
    return redirect("/")


# connection.close()
if __name__ =="__main__":
    app.run()


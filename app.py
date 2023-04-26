from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "sistla-harsha"
 
DB_HOST = "localhost"
DB_NAME = "collegedb"
DB_USER = "postgres"
DB_PASS = "admin"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM student"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)
 
@app.route('/student', methods=['POST'])
def student():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':

        student_id = request.form['student_id']
        student_name = request.form['student_name']
        sports_id = request.form['sports_id']
        student_salary = request.form['student_salary']
        student_fees = request.form['student_fees']
        is_payment_received = request.form['is_payment_received']

        cur.execute(f"INSERT INTO student (student_id, student_name, sports_id, student_salary, student_fees, is_payment_received) VALUES {(student_id, student_name, sports_id, student_salary, student_fees, is_payment_received)}")
        conn.commit()
        flash('Student Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<student_id>', methods = ['POST', 'GET'])
def get_employee(student_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f'SELECT * FROM student WHERE student_id = {student_id}')
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', student = data[0])
 
@app.route('/update/<student_id>', methods=['POST'])
def update_student(student_id):
    if request.method == 'POST':
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        sports_id = request.form['sports_id']
        student_salary = request.form['student_salary']
        student_fees = request.form['student_fees']
        is_payment_received = request.form['is_payment_received']
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE student
            SET student_name = %s,
                sports_id = %s,
                student_salary = %s,
                student_fees = %s,
                is_payment_received = %s
            WHERE student_id = %s
        """, (student_name, sports_id, student_salary, student_fees, is_payment_received, student_id))
        flash('Student Details Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<student_id>', methods = ['POST','GET'])
def delete_student(student_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM student WHERE student_id = {0}'.format(student_id))
    conn.commit()
    flash('Student Details Removed Successfully')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)
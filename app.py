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
@app.route('/<table_id>')
def Index(table_id="student"):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = f"SELECT * FROM {table_id}"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template(f'{table_id}/index.html', list_users = list_users)

#################### STUDENT ####################
 
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
        return redirect(url_for('Index', table_id="student"))
 
@app.route('/edit/student/<student_id>', methods = ['POST', 'GET'])
def edit_student(student_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f'SELECT * FROM student WHERE student_id = {student_id}')
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('student/edit.html', student = data[0])
 
@app.route('/update/student/<student_id>', methods=['POST'])
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
        return redirect(url_for('Index', table_id="student"))
 
@app.route('/delete/student/<student_id>', methods = ['POST','GET'])
def delete_student(student_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM student WHERE student_id = {0}'.format(student_id))
    conn.commit()
    flash('Student Details Removed Successfully')
    return redirect(url_for('Index', table_id="student"))


#################### TEACHER ####################

@app.route('/teacher', methods=['POST'])
def teacher():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':

        teacher_id = request.form['teacher_id']
        teacher_name = request.form['teacher_name']
        specialisation = request.form['specialisation']
        experience = request.form['experience']
        payment = request.form['payment']

        cur.execute(f"INSERT INTO teacher (teacher_id, teacher_name, specialisation, experience, payment) VALUES {(teacher_id, teacher_name, specialisation, experience, payment)}")
        conn.commit()
        flash('Teacher Added successfully')
        return redirect(url_for('Index', table_id="teacher"))
 
@app.route('/edit/teacher/<teacher_id>', methods = ['POST', 'GET'])
def edit_teacher(teacher_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f'SELECT * FROM teacher WHERE teacher_id = {teacher_id}')
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('teacher/edit.html', teacher = data[0])
 
@app.route('/update/teacher/<teacher_id>', methods=['POST'])
def update_teacher(teacher_id):
    if request.method == 'POST':

        teacher_id = request.form['teacher_id']
        teacher_name = request.form['teacher_name']
        specialisation = request.form['specialisation']
        experience = request.form['experience']
        payment = request.form['payment']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE teacher
            SET teacher_name = %s,
                specialisation = %s,
                experience = %s,
                payment = %s
            WHERE teacher_id = %s
        """, (teacher_name, specialisation, experience, payment, teacher_id))
        flash('Teacher Details Updated Successfully')
        conn.commit()
        return redirect(url_for('Index', table_id="teacher"))
 
@app.route('/delete/teacher/<teacher_id>', methods = ['POST','GET'])
def delete_teacher(teacher_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM teacher WHERE teacher_id = {0}'.format(teacher_id))
    conn.commit()
    flash('Teacher Details Removed Successfully')
    return redirect(url_for('Index', table_id='teacher'))

#################### GROUND ####################
 
@app.route('/ground', methods=['POST'])
def ground():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':

        ground_id = request.form['ground_id']
        ground_name = request.form['ground_name']
        ground_location = request.form['ground_location']

        cur.execute(f"INSERT INTO ground (ground_id, ground_name, ground_location) VALUES {(ground_id, ground_name, ground_location)}")
        conn.commit()
        flash('Ground Added successfully')
        return redirect(url_for('Index', table_id="ground"))

@app.route('/edit/ground/<ground_id>', methods = ['POST', 'GET'])
def edit_ground(ground_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f'SELECT * FROM ground WHERE ground_id = {ground_id}')
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('ground/edit.html', ground = data[0])

@app.route('/update/ground/<ground_id>', methods=['POST'])
def update_ground(ground_id):
    if request.method == 'POST':

        ground_id = request.form['ground_id']
        ground_name = request.form['ground_name']
        ground_location = request.form['ground_location']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE ground
            SET ground_name = %s,
                ground_location = %s
            WHERE ground_id = %s
        """, (ground_name, ground_location, ground_id))
        flash('Ground Details Updated Successfully')
        conn.commit()
        return redirect(url_for('Index', table_id="ground"))

@app.route('/delete/ground/<ground_id>', methods = ['POST','GET'])
def delete_ground(ground_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM ground WHERE ground_id = {0}'.format(ground_id))
    conn.commit()
    flash('Ground Details Removed Successfully')
    return redirect(url_for('Index', table_id="ground"))

#################### SPORTS ####################

@app.route('/sports', methods=['POST'])
def sports():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':

        sports_id = request.form['sports_id']
        sports_name = request.form['sports_name']
        ground_id = request.form['ground_id']

        cur.execute(f"INSERT INTO sports (sports_id, sports_name, ground_id) VALUES {(sports_id, sports_name, ground_id)}")
        conn.commit()
        flash('Sports Added successfully')
        return redirect(url_for('Index', table_id="sports"))
 
@app.route('/edit/sports/<sports_id>', methods = ['POST', 'GET'])
def edit_sports(sports_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(f'SELECT * FROM sports WHERE sports_id = {sports_id}')
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('sports/edit.html', sports = data[0])
 
@app.route('/update/sports/<sports_id>', methods=['POST'])
def update_sports(sports_id):
    if request.method == 'POST':

        sports_id = request.form['sports_id']
        sports_name = request.form['sports_name']
        ground_id = request.form['ground_id']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE sports
            SET sports_name = %s,
                ground_id = %s
            WHERE sports_id = %s
        """, (sports_name, ground_id, sports_id))
        flash('Sports Details Updated Successfully')
        conn.commit()
        return redirect(url_for('Index', table_id="sports"))
 
@app.route('/delete/sports/<sports_id>', methods = ['POST','GET'])
def delete_sports(sports_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM sports WHERE sports_id = {0}'.format(sports_id))
    conn.commit()
    flash('Sports Details Removed Successfully')
    return redirect(url_for('Index', table_id='sports'))

if __name__ == "__main__":
    app.run(debug=True)
CREATE TABLE student (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(50),
  sports_id INT,
  student_salary FLOAT,
  student_fees FLOAT,
  is_payment_received BOOLEAN
);

CREATE TABLE ground (
  ground_id INT PRIMARY KEY,
  ground_name VARCHAR(50),
  ground_location VARCHAR(50)
);

CREATE TABLE sports (
  sports_id INT PRIMARY KEY,
  sports_name VARCHAR(50),
  ground_id INT,
  FOREIGN KEY (ground_id) REFERENCES ground(ground_id)
);

CREATE TABLE teacher (
  teacher_id INT PRIMARY KEY,
  teacher_name VARCHAR(50),
  specialisation VARCHAR(50),
  experience INT,
  payment FLOAT
);

CREATE TABLE teacher_sports (
  teacher_id INT,
  sports_id INT,
  FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id),
  FOREIGN KEY (sports_id) REFERENCES sports(sports_id)
);

CREATE TABLE student_teacher (
  student_id INT,
  teacher_id INT,
  FOREIGN KEY (student_id) REFERENCES student(student_id),
  FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

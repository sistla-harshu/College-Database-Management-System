INSERT INTO student (student_id, student_name, sports_id, student_salary, student_fees, is_payment_received)
VALUES (1, 'John Smith', 1, 1000.00, 500.00, false);

INSERT INTO ground (ground_id, ground_name, ground_location)
VALUES (1, 'Green Field', 'Central Park');

INSERT INTO sports (sports_id, sports_name, ground_id)
VALUES (1, 'Football', 1);

INSERT INTO teacher (teacher_id, teacher_name, specialisation, experience, payment)
VALUES (1, 'Mr. Johnson', 'Mathematics', 10, 5000.00);

INSERT INTO teacher_sports (teacher_id, sports_id)
VALUES (1, 1);

INSERT INTO student_teacher (student_id, teacher_id)
VALUES (1, 2);
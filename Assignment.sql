create database student;
use student;

--task 1 database creation 

create table Students(
	student_id int primary key,
	first_name varchar(30),
	last_name varchar(30),
	date_of_birth date,
	email varchar(40) unique not null,
	phone_number varchar(40)
	);

insert into Students
values
	(1,'Rasika','B','2002-10-07','rasika07@gmail.com','9876543210'),
	(2,'Usha','K','2004-01-27','usha27@gmail.com','7654321896'),
	(3,'Som','R','2004-01-01','som01@gmail.com','6543217893'),
	(4,'Sivalalitha','K','2004-05-19','lalli@gmail.com','6789023451'),
	(5,'Shreeja','E','2004-01-21','shreeja21@gmail.com','8765432193');


create table Teachers
(
	teacher_id int primary key,
	first_name varchar(40),
	last_name varchar(40),
	email varchar(50)
);

insert into Teachers
values 
	(1,'Anitha','S','anitha@gmail.com'),
	(2,'Madhu','P','madhu@gmail.com'),
	(3,'Deepa','K','deepa@gmail.com');


create table Courses
(
	course_id int primary key,
	course_name varchar(60),
	credits int check (credits>0),
	teacher_id int,
	foreign key (teacher_id) references Teachers(teacher_id)
);

insert into Courses
values
	(1,'Python',4,1),
	(2,'Sql',3,2),
	(3,'Java',4,3);
	


create table Enrollments
(
	enrollment_id int primary key  IDENTITY(1,1),
	student_id int,
	course_id int,
	enrollment_date date,
	foreign key (student_id) references Students (student_id) on delete cascade,
	foreign key (course_id) references Courses(course_id)
);

insert into Enrollments (student_id, course_id, enrollment_date) 
values
    (1, 1, '2025-02-10'),
    (2, 2, '2025-02-11'),
    (3, 3, '2025-02-12'),
    (4, 1, '2025-02-13'),
    (5, 2, '2025-02-14');

--drop table Enrollments;
--drop table Payments;
create table Payments
(
	payment_id int primary key IDENTITY(1,1),
	student_id int,
	amount decimal (20,2) NOT NULL CHECK (amount > 0),
	payment_date date,
	foreign key (student_id) references Students(student_id)

);

insert into  Payments (student_id, amount, payment_date) 
values
    (1, 5000.00, '2025-03-01'),
    (2, 4500.00, '2025-03-02'),
    (3, 5500.00, '2025-03-03'),
    (4, 4000.00, '2025-03-04'),
    (5, 6000.00, '2025-03-05');


--task 2 Select, Where, Between, AND, LIKE:

--q1
insert into  Students (student_id, first_name, last_name, date_of_birth, email, phone_number) 
values (6, 'John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890');

select * from Students;

--q2
insert into Enrollments (student_id, course_id, enrollment_date) 
values (6, 1, '2025-03-27');

--q3
update Teachers
set email = 'madhumitha29@gmail.com'
where teacher_id = 2;

--q4
delete from  Enrollments 
where student_id = 6 AND course_id = 1;

--q5
update Courses
set teacher_id = 3
where course_id = 2;

--q6
delete from Students 
where student_id = 6;

--q7
update Payments
set amount = 7000.00
where payment_id = 3;

--task 3

--q1
select s.student_id, s.first_name, s.last_name, coalesce(sum(p.amount), 0) as total_payment
from students s
left join payments p on s.student_id = p.student_id
where s.student_id = 1
group by s.student_id, s.first_name, s.last_name;

--q2
select c.course_id, c.course_name, count(e.student_id) as student_count
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name
order by student_count desc;

--q3
select s.student_id, s.first_name, s.last_name
from students s
left join enrollments e on s.student_id = e.student_id
where e.course_id is null;

--q4
select s.first_name, s.last_name, c.course_name
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
order by s.first_name, s.last_name;


--q5
select t.first_name, t.last_name, c.course_name
from teachers t
left join courses c on t.teacher_id = c.teacher_id
order by t.first_name, t.last_name;


--q6
select s.first_name, s.last_name, e.enrollment_date
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
where c.course_id = 1;  -- Replace 1 with the specific course_id


--q7
select s.student_id, s.first_name, s.last_name
from students s
left join payments p on s.student_id = p.student_id
where p.payment_id is null;


--q8
select c.course_id, c.course_name
from courses c
left join enrollments e on c.course_id = e.course_id
where e.enrollment_id is null;


--q9
select e1.student_id, s.first_name, s.last_name, count(e1.course_id) as course_count
from enrollments e1
join students s on e1.student_id = s.student_id
group by e1.student_id, s.first_name, s.last_name
having count(e1.course_id) > 1
order by course_count desc;

--q10
select t.teacher_id, t.first_name, t.last_name
from teachers t
left join courses c on t.teacher_id = c.teacher_id
where c.course_id is null;

--task 4

--q1
select avg(student_count) as avg_enrollment
from (
    select course_id, count(student_id) as student_count
    from enrollments
    group by course_id
) as enrollment_counts;


--q2
select s.first_name, s.last_name, p.amount
from students s
join payments p on s.student_id = p.student_id
where p.amount = (select max(amount) from payments);

--q3
select c.course_name, count(e.student_id) as enrollment_count
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name
having count(e.student_id) = (
    select max(enrollment_count) 
    from (select course_id, count(student_id) as enrollment_count 
          from enrollments 
          group by course_id) as course_enrollments
);


--q4
select t.first_name, t.last_name, coalesce(sum(p.amount), 0) as total_payment
from teachers t
left join courses c on t.teacher_id = c.teacher_id
left join enrollments e on c.course_id = e.course_id
left join payments p on e.student_id = p.student_id
group by t.teacher_id, t.first_name, t.last_name;


--q5
select s.student_id, s.first_name, s.last_name
from students s
where (select count(course_id) from courses) = (
    select count(e.course_id)
    from enrollments e
    where e.student_id = s.student_id
);

--q6
select t.first_name, t.last_name
from teachers t
where not exists (
    select 1 from courses c where c.teacher_id = t.teacher_id
);

--q7
select avg(datediff(year, date_of_birth, getdate())) as avg_age
from students;

--q8
select course_name
from courses
where course_id not in (select distinct course_id from enrollments);

--q9
select s.first_name, s.last_name, c.course_name, coalesce(sum(p.amount), 0) as total_payment
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
left join payments p on s.student_id = p.student_id
group by s.student_id, s.first_name, s.last_name, c.course_name;

--q10
select s.student_id, s.first_name, s.last_name, count(p.payment_id) as payment_count
from students s
join payments p on s.student_id = p.student_id
group by s.student_id, s.first_name, s.last_name
having count(p.payment_id) > 1;

--q11
select s.student_id, s.first_name, s.last_name, coalesce(sum(p.amount), 0) as total_payment
from students s
left join payments p on s.student_id = p.student_id
group by s.student_id, s.first_name, s.last_name;

--q12
select c.course_name, count(e.student_id) as student_count
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name;

--q13
select avg(p.amount) as avg_payment
from payments p;



	




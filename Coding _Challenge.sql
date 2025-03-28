create database CareerHub;
use CareerHub;


--q1,q2,q3,q4
create table Companies (
    company_id int primary key ,
    company_name varchar(255) not null,
    location varchar(255) not null
);

insert into Companies (company_id, company_name, location) 
values 
(1, 'TechCorp', 'New York'),
(2, 'Innovate Ltd', 'San Francisco'),
(3, 'Green Solutions', 'Chicago');

create table Jobs (
    job_id int primary key ,
    company_id int not null,
    job_title varchar(255) not null,
    job_description text,
    job_location varchar(255),
    salary decimal(10,2) check (salary >= 0),
    job_type varchar(50),
    posted_date datetime default current_timestamp,
    foreign key (company_id) references Companies(company_id) on delete cascade
);

insert into Jobs (job_id, company_id, job_title, job_description, job_location, salary, job_type) 
values 
(1, 1, 'Software Engineer', 'Develop and maintain software applications', 'New York', 85000.00, 'Full-time'),
(2, 2, 'Data Analyst', 'Analyze company data and generate reports', 'San Francisco', 75000.00, 'Full-time'),
(3, 3, 'Project Manager', 'Manage company projects and coordinate teams', 'Chicago', 95000.00, 'Full-time');


create table  Applicants (
    applicant_id int primary key ,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(255) unique not null,
    phone varchar(20),
    resume text
);

insert into Applicants (applicant_id, first_name, last_name, email, phone, resume) 
values 
(1, 'John', 'Doe', 'johndoe@email.com', '123-456-7890', 'Experienced software engineer with 5+ years of experience.'),
(2, 'Jane', 'Smith', 'janesmith@email.com', '987-654-3210', 'Data analyst with 3+ years of experience in SQL and Python.');

create table Applications (
    application_id int primary key ,
    job_id int not null,
    applicant_id int not null,
    application_date datetime default current_timestamp,
    cover_letter text,
    foreign key (job_id) references Jobs(job_id) on delete cascade,
    foreign key (applicant_id) references Applicants(applicant_id) on delete cascade
);

insert into Applications (application_id, job_id, applicant_id, cover_letter) 
values 
(1, 1, 1, 'I am excited to apply for this role and bring my expertise to your company.'),
(2, 2, 2, 'I am passionate about data analysis and would love to contribute to your team.');



-- q5
select j.job_title, count(a.application_id) as application_count
from jobs j
left join applications a on j.job_id = a.job_id
group by j.job_title;

-- q6
declare @min_salary int = 60000;
declare @max_salary int = 80000;
select j.job_title, c.company_name, j.job_location, j.salary
from jobs j
join companies c on j.company_id = c.company_id
where j.salary between @min_salary and @max_salary;

-- q7
declare @applicant_id int = 1;
select j.job_title, c.company_name, a.application_date
from applications a
join jobs j on a.job_id = j.job_id
join companies c on j.company_id = c.company_id
where a.applicant_id = @applicant_id;

-- q8
select avg(salary) as avg_salary
from jobs
where salary > 0;

-- q9
select top 1 with ties c.company_name, count(j.job_id) as job_count
from companies c
join jobs j on c.company_id = j.company_id
group by c.company_name
order by job_count desc;

-- q10
select a.first_name, a.last_name
from applicants a
join applications app on a.applicant_id = app.applicant_id
join jobs j on app.job_id = j.job_id
join companies c on j.company_id = c.company_id
where c.location = 'cityx' and a.experience_years >= 3;

-- q11
select distinct job_title
from jobs
where salary between 60000 and 80000;

-- q12
select j.job_title
from jobs j
left join applications a on j.job_id = a.job_id
where a.application_id is null;

-- q13
select a.first_name, a.last_name, c.company_name, j.job_title
from applications app
join applicants a on app.applicant_id = a.applicant_id
join jobs j on app.job_id = j.job_id
join companies c on j.company_id = c.company_id;

-- q14
select c.company_name, count(j.job_id) as job_count
from companies c
left join jobs j on c.company_id = j.company_id
group by c.company_name;

-- q15
select a.first_name, a.last_name, isnull(c.company_name, 'no applications') as company_name, isnull(j.job_title, 'no applications') as job_title
from applicants a
left join applications app on a.applicant_id = app.applicant_id
left join jobs j on app.job_id = j.job_id
left join companies c on j.company_id = c.company_id;

-- q16
select c.company_name
from companies c
join jobs j on c.company_id = j.company_id
where j.salary > (select avg(salary) from jobs where salary > 0);

-- q17
select first_name, last_name, concat(city, ', ', state) as location
from applicants;

-- q18
select job_title, job_location, salary
from jobs
where job_title like '%developer%' or job_title like '%engineer%';

-- q19
select a.first_name, a.last_name, coalesce(j.job_title, 'no application') as job_title
from applicants a
left join applications app on a.applicant_id = app.applicant_id
left join jobs j on app.job_id = j.job_id

union

select a.first_name, a.last_name, j.job_title
from jobs j
left join applications app on j.job_id = app.job_id
left join applicants a on app.applicant_id = a.applicant_id
where a.applicant_id is null;

-- q20
declare @city varchar(100) = 'new york';

select a.first_name, a.last_name, c.company_name
from applicants a, companies c
where c.location = @city
and a.experience_years > 2;

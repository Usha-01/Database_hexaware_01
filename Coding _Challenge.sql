create database CareerHub;
use CareerHub;


--q1,q2,q3,q4
create table Companies (
    company_id int primary key ,
    company_name varchar(255) not null,
    location varchar(255) not null
);


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


create table  Applicants (
    applicant_id int primary key ,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(255) unique not null,
    phone varchar(20),
    resume text
);


create table Applications (
    application_id int primary key ,
    job_id int not null,
    applicant_id int not null,
    application_date datetime default current_timestamp,
    cover_letter text,
    foreign key (job_id) references Jobs(job_id) on delete cascade,
    foreign key (applicant_id) references Applicants(applicant_id) on delete cascade
);


--q5
select j.job_title, count(a.application_id) as application_count
from jobs j
left join applications a on j.job_id = a.job_id
group by j.job_title;



--q6
select distinct JobTitle
from Jobs
where Salary between 60000 and 80000;


-- q7

select j.jobid, j.jobtitle, c.companyname
from jobs j
join companies c on j.companyid = c.companyid
left join applications a on j.jobid = a.jobid
where a.jobid is null;


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
select distinct a.*
from applicants a
join applications app on a.applicant_id = app.applicant_id
join jobs j on app.job_id = j.job_id
join companies c on j.company_id = c.company_id
where c.location = 'cityx' and a.resume like '%3+ years experience%';



-- q11
select distinct job_title
from jobs
where salary between 60000 and 80000;



-- q12
select *
from jobs
where job_id not in (select job_id from applications);



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
select a.first_name, a.last_name, coalesce(c.company_name, 'No Applications') as company_name, coalesce(j.job_title, 'No Applications') as job_title
from applicants a
left join applications app on a.applicant_id = app.applicant_id
left join jobs j on app.job_id = j.job_id
left join companies c on j.company_id = c.company_id;


-- q16
select distinct c.company_name
from companies c
join jobs j on c.company_id = j.company_id
where j.salary > (select avg(salary) from jobs where salary > 0);


-- q17
select first_name, last_name, city + ', ' + state as location
from applicants;



-- q18
select * from jobs
where job_title like '%developer%' or job_title like '%engineer%';



-- q19
select a.first_name, a.last_name, j.job_title
from applicants a
full join applications app on a.applicant_id = app.applicant_id
full join jobs j on app.job_id = j.job_id;



-- q20
select a.FirstName, a.LastName, c.CompanyName
from Applicants a, Companies c
where c.City = 'Chennai' AND a.ExperienceYears > 2;


--create schema transport;

create database case_study;
use case_study;

create table vehicles (
    vehicle_id int primary key,
    model varchar(255) not null,
    capacity decimal(10,2) not null,
    type varchar(50) not null,
    status varchar(50) not null
);


insert into vehicles (vehicle_id, model, capacity, type, status) 
values 
(1, 'volvo x100', 50, 'bus', 'active'),
(2, 'mercedes sprinter', 30, 'minibus', 'active'),
(3, 'tesla model x', 5, 'car', 'inactive');


create table routes (
    route_id int primary key,
    start_destination varchar(255) not null,
    end_destination varchar(255) not null,
    distance decimal(10,2) not null
);

insert into routes (route_id, start_destination, end_destination, distance) 
values 
(1, 'new york', 'washington d.c.', 360.50),
(2, 'los angeles', 'san francisco', 620.00),
(3, 'chicago', 'detroit', 380.75);

create table trips (
    trip_id int primary key,
    vehicle_id int not null,
    route_id int not null,
    departure_date datetime not null,
    arrival_date datetime not null,
    status varchar(50) not null,
    trip_type varchar(50) ,
    max_passengers int,
    foreign key (vehicle_id) references vehicles(vehicle_id),
    foreign key (route_id) references routes(route_id)
);


insert into trips (trip_id, vehicle_id, route_id, departure_date, arrival_date, status, trip_type, max_passengers) 
values 
(1, 1, 1, '2025-04-01 08:00:00', '2025-04-01 14:00:00', 'scheduled', 'one-way', 50),
(2, 2, 2, '2025-04-02 09:30:00', '2025-04-02 17:00:00', 'scheduled', 'round-trip', 30),
(3, 3, 3, '2025-04-03 07:45:00', '2025-04-03 12:30:00', 'cancelled', 'one-way', 5);

create table passengers (
    passenger_id int  primary key,
    first_name varchar(255) not null,
    gender varchar(255) not null,
    age int not null,
    email varchar(255) unique not null,
    phone_number varchar(50) not null
);


insert into passengers (passenger_id, first_name, gender, age, email, phone_number) 
values 
(1, 'alice', 'female', 28, 'alice@example.com', '1234567890'),
(2, 'bob', 'male', 35, 'bob@example.com', '0987654321'),
(3, 'charlie', 'non-binary', 22, 'charlie@example.com', '1122334455');


create table bookings (
    booking_id int  primary key,
    trip_id int not null,
    passenger_id int not null,
    booking_date datetime not null,
    status varchar(50) not null,
    foreign key (trip_id) references trips(trip_id),
    foreign key (passenger_id) references passengers(passenger_id)
);


insert into bookings (booking_id, trip_id, passenger_id, booking_date, status) 
values 
(1, 1, 1, '2025-03-20 12:00:00', 'confirmed'),
(2, 2, 2, '2025-03-21 14:30:00', 'confirmed'),
(3, 3, 3, '2025-03-22 16:45:00', 'cancelled');
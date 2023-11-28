drop table if exists contact_request;

drop table if exists client_contact;
drop table if exists client_account;

drop table if exists industry;
drop table if exists company;

drop table if exists logins; 

drop table if exists project_status;
drop table if exists project;

drop table if exists ticket_status;
drop table if exists ticket; 
drop table if exists checklist;

-- references 
--      https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/
--      https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table/
--      https://stackoverflow.com/questions/5621469/database-design-what-fields-are-must-for-a-user-table-in-database

-- clients 

create table contact_request (
    id int primary key generated always as identity,
    name varchar(50) not null,
    phone char(11) not null,
    email varchar(50) not null,
    requested_at timestamp
);

create table client_contact (
    id int primary key generated always as identity,
    f_name varchar(50) not null,
    l_name varchar(50) not null,
    phone varchar(12) not null,
    email varchar(120) not null
);

create table client_account (
    id int primary key generated always as identity,
    contact_id int,
    company_id int, 
    username varchar(20),
    pass varchar(60),
    constraint fk_contact foreign key (contact_id) references client_contact(id)
);

-- companies

create table industry (
    id int primary key generated always as identity,
    industry varchar(100),
    industry_description text
);


create table company (
    id int primary key generated always as identity,
    company varchar(100) not null,
    industry_id int,
    website_url varchar(255),
    created_at timestamp,
    constraint fk_industry foreign key (industry_id) references industry(id)
);

-- projects

create table project_status (
    id int primary key generated always as identity,
    status_code varchar(25) not null,
    status_description varchar(255) not null 
);

create table project (
    id int primary key generated always as identity,
    project_status_id int,
    created_at timestamp,
    updated_at timestamp,
    completed_at timestamp,
    title varchar(100) not null, 
    content text not null,
    client_id int,
    total_hours real, 
    hourly_rate real,
    constraint fk_project_status foreign key (project_status_id) references project_status(id),
    constraint fk_client foreign key (client_id) references client_account(id)
);

-- tickets

create table ticket_status (
    id int primary key generated always as identity,
    status_code varchar(25) not null,
    status_description varchar(255) not null
);


create table ticket (
    id int primary key generated always as identity,
    title varchar(50) not null,
    content text not null,
    client_id int,
    status_id int, 
    project_id int,
    created_at timestamp,
    completed_at timestamp,
    foreign key (client_id) references client_account(id),
    foreign key (status_id) references ticket_status(id),
    foreign key (project_id) references project(id)
);

create table ticket_item (
    id int primary key generated always as identity,
    ticket_id int,
    created_at timestamp,
    item varchar(255),
    completed boolean,
    completed_at timestamp,
    constraint fk_ticket foreign key (ticket_id) references ticket(id)
);
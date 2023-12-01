drop table if exists contact_request;

drop table if exists client;
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
    id integer primary key autoincrement,
    name text not null,
    phone text not null,
    email text not null,
    requested_at timestamp
);

create table client (
    id integer primary key autoincrement,
    client text not null,
    created_at timestamp default current_timestamp
);

create table client_contact (
    id integer primary key autoincrement,
    f_name text not null,
    l_name text not null,
    phone text not null,
    email text not null
);

create table client_account (
    id integer primary key autoincrement,
    contact_id integer,
    company_id integer, 
    username text,
    pass text,
    constraint fk_contact foreign key (contact_id) references client_contact(id)
);

-- companies

create table industry (
    id integer primary key autoincrement,
    industry text,
    industry_description text
);


create table company (
    id integer primary key autoincrement,
    company text not null,
    industry_id integer,
    website_url text,
    created_at timestamp,
    constraint fk_industry foreign key (industry_id) references industry(id)
);

-- projects

create table project_status (
    id integer primary key autoincrement,
    status_code text not null,
    status_description text not null 
);

create table project (
    id integer primary key autoincrement,
    project_status_id integer,
    created_at timestamp,
    updated_at timestamp,
    completed_at timestamp,
    title text not null, 
    content text not null,
    client_id integer,
    total_hours real, 
    hourly_rate real,
    constraint fk_project_status foreign key (project_status_id) references project_status(id),
    constraint fk_client foreign key (client_id) references client_account(id)
);

-- tickets

create table ticket_status (
    id integer primary key autoincrement,
    status_code text not null,
    status_description text not null
);


create table ticket (
    id integer primary key autoincrement,
    title text not null,
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
    id integer primary key autoincrement,
    ticket_id integer,
    created_at timestamp,
    item text,
    completed boolean,
    completed_at timestamp,
    constraint fk_ticket foreign key (ticket_id) references ticket(id)
);
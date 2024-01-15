drop table if exists leads;
drop table if exists clients;
drop table if exists client_accounts;
drop table if exists status_codes;
drop table if exists projects;
drop table if exists tickets;

create table leads (
    id integer primary key autoincrement,
    company varchar(60),
    email varchar(60),
    phone varchar(12),
    contact_name varchar(60),
    contacted boolean,
    viable boolean,
    converted boolean
);

create table clients(
    id integer primary key autoincrement,
    company varchar(60) unique not null,
    f_name varchar(60) not null,
    l_name varchar(60) not null,
    phone varchar(12) not null
);

create table client_accounts(
    id integer primary key autoincrement,
    client_id integer not null,
    username varchar(60),
    pass_hash varchar(60),
    foreign key (client_id) references clients(id)
);

create table status_codes(
    id integer primary key autoincrement,
    _status varchar(60),
    _description varchar(250)
);

create table projects(
    id integer primary key autoincrement,
    project_status integer,
    client_id integer,
    personal boolean,
    project_name varchar(80),
    project_description varchar(500),
    estimated_selling_price real,
    hourly_rate real,
    foreign key (project_status) references status_codes(id)
    foreign key (client_id) references clients(id)
);

create table tickets(
    id integer primary key autoincrement,
    project_id integer,
    ticket_status integer,
    ticket_title varchar(80),
    ticket_description varchar(500),
    foreign key (project_id) references projects(id),
    foreign key (ticket_status) references status_codes(id)
);
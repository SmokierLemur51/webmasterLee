-- tables to create

-- client



drop table if exists contact_request;
create table contact_request (
    id integer primary key,
    name text not null,
    phone text not null,
    email text not null,
);


-- guru tables
drop table if exists ticket_status;
create table ticket_status (
    id integer primary key autoincrement,
    'status' text not null,
    
);



drop table if exists project;
create table project();

drop table if exists ticket;
create table ticket (
    id integer primary key,
    title text not null,
    content text,
    client_id integer,
    status_id integer, 
    project_id integer,
    created_at timestamp,
    completed_at timestamp, 
    foreign key (client_id) references client(id),
    foreign key (status_id) references ticket_status(id),
    foreign key (project_id) references project(id)
);


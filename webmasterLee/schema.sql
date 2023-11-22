drop table if exists contact_request; -- done

drop table if exists client_user;

drop table if exists project_status; -- done
drop table if exists project;

drop table if exists ticket_status;
drop table if exists ticket; 


-- public tables 

create table contact_request (
    id integer primary key,
    name text not null,
    phone text not null,
    email text not null,
);

-- client tables

create table project_status (
    id integer primary key autoincrement,
    p_status text not null,
    p_description text not null
    created_at timestamp 
);


drop table if exists ticket_status;
create table ticket_status (
    id integer primary key autoincrement,
    t_status text not null,
    t_description text not null,
    created_at timestamp
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

    foreign key (project_status_id) references project_status(id),
    foreign key (client_id) references client_user(id)
);

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


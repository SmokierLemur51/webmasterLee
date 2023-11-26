drop table if exists contact_request;

drop table if exists client_user;

drop table if exists project_status;
drop table if exists project;

drop table if exists ticket_status;
drop table if exists ticket; 
drop table if exists checklist;


-- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/
-- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table/

create table contact_request (
    id integer primary key generated always as identity,
    name varchar(50) not null,
    phone char(11) not null,
    email varchar(50) not null,
    requested_at timestamp,
);
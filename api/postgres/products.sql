DROP DATABASE IF EXISTS "DemoProducts";
CREATE DATABASE "DemoProducts";

\connect DemoProducts;

create type currency as enum ('USD', 'CAD', 'EUR', 'GBP');

create sequence product_id_seq start 1;

create table products (
    id bigint not null primary key,
    name text not null,
    price integer not null,
    description text,
    view_count integer not null,
    active boolean not null
);

--Insert a few preliminary entries to simulate populated db:

insert into products(id, name, price, description, view_count, active)
values
(nextval('product_id_seq'), 'AwesomeProduct 1', 100, 'Awesome product description', 0, true),
(nextval('product_id_seq'), 'AwesomeProduct 2', 50, 'Awesome product description', 3, true),
(nextval('product_id_seq'), 'AwesomeProduct 3', 20, NULL, 4, true),
(nextval('product_id_seq'), 'AwesomeProduct 4', 20, 'Awesome product description', 2, true),
(nextval('product_id_seq'), 'AwesomeProduct 5', 25, 'Awesome product description', 1, true),
(nextval('product_id_seq'), 'AwesomeProduct 6', 15, 'Awesome product description', 0, true);



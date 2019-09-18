create table products(product_id integer, title varchar(100));
insert into products(product_id, title) values(1, "Apple");
insert into products(product_id, title) values(2, "Banana");
insert into products(product_id, title) values(3, "Cat");
select * from products;


create table order_items(order_id integer,product_id integer, quantity integer);
insert into order_items(order_id, product_id, quantity) values(1,1,10);
insert into order_items(order_id, product_id, quantity) values(1,2,20);
insert into order_items(order_id, product_id, quantity) values(1,3,30);
insert into order_items(order_id, product_id, quantity) values(2,2,2);
insert into order_items(order_id, product_id, quantity) values(3,3,3);
-- select it1.product_id from order_items as it1;

select it1.product_id , it2.product_id
from order_items AS it1
inner join order_items AS it2 on it1.order_id = it2.order_id
and it2.product_id > it1.product_id
group by it1.product_id, it2.product_id
order by count(*) DESC
LIMIT 3












create table a(id integer);
create table b(id integer);
create table c(id integer);
insert into a(id) values(0);
insert into a(id) values(1);
insert into b(id) values(1);
insert into b(id) values(2);
insert into c(id) values(2);
insert into c(id) values(3);

select * from a
right join b
on a.id = b.id
left join c
on b.id = c.id



create table person(id integer, title varchar(100));
create table loan(id integer, person_id integer);

insert into person(id, title) values(1, "Girish");
insert into person(id, title) values(2, "Manish");

insert into loan(id, person_id) values(1, 2);

select t.id, t.title
from person As t
where t.id not in
(select NULL from loan as l where l.person_id = t.id)

-- Your code here!

create table person(id integer, title varchar(100));
create table loan(id integer, person_id integer);

insert into person(id, title) values(1, "Hello");
insert into person(id, title) values(1, "Hello");
insert into person(id, title) values(2, "Hello2");
insert into person(id, title) values(NULL, "Hello3");

-- select distinct(title) from person having title like 'H%'
-- select title from person
-- group by title
-- having title like 'H%'


-- select title from person where title like 'H%'
-- group by title

-- select MAX(id) from person

-- select * from person where id <= 2 or id >=2
select count(*) , count(id) from person



create table items(id integer, parent_id integer, item_name varchar(100));
insert into items(id, parent_id,  item_name) values(1, NULL, "parent1");
insert into items(id, parent_id,  item_name) values(2, 1, "child1");
insert into items(id, parent_id,  item_name) values(3, 1, "child2");
insert into items(id, parent_id,  item_name) values(4, NULL, "parent2");
insert into items(id, parent_id,  item_name) values(5, NULL, "parent3");
insert into items(id, parent_id,  item_name) values(6, 5, "child3");

select it2.item_name as child, it2.id , it1.item_name from items it1 ,
items it2 where it1.parent_id = it2.id;
parent1	1	child1
parent1	1	child2
parent3	5	child3


create table person(id integer, title varchar(100));
create table loan(id integer, person_id integer);
insert into person(id, title) values(1, "Girish");
insert into person(id, title) values(2, "Manish");
insert into person(id, title) values(3, "Ganesh");

insert into loan(id, person_id) values(1, 1);
insert into loan(id, person_id) values(2, 2);


select t.id, t.title
from person As t
-- where t.id not in
where not exists
(select NULL from loan as l where l.person_id = t.id)


select id, title
from person  where title like 'G%'

union


select id, title
from person  where title like '%h';

1	Girish
3	Ganesh
2	Manish



create table person(id integer, title varchar(100));
create table loan(id integer, person_id integer);

insert into person(id, title) values(1, "Girish Gupta");
insert into person(id, title) values(2, "Manish Kumar");
insert into person(id, title) values(3, "Ganesh Yadav");
insert into person(id, title) values(4, "Girish Kumar");
insert into person(id, title) values(5, "Girish Kumar");

insert into loan(id, person_id) values(1, 1);
insert into loan(id, person_id) values(2, 2);


select title
from person  where title like 'Girish%';
-- Girish Gupta
-- Girish Kumar
-- Girish Kumar

select title
from person  where title like 'Girish%'
group by title;

-- Girish Gupta
-- Girish Kumar

select title
from person
group by title
having title like 'Girish%';

-- Girish Gupta
-- Girish Kumar

select distinct(title)
from person
where title like 'Girish%'
group by title;

-- Girish Gupta
-- Girish Kumar


select title
from person
having title like 'Girish%';
-- Girish Gupta
-- Girish Kumar
-- Girish Kumar


create table products(product_id integer, title varchar(100));
insert into products(product_id, title) values(1, "Apple");
insert into products(product_id, title) values(2, "Banana");
insert into products(product_id, title) values(3, "Cat");


create table order_items(order_id integer,product_id integer, quantity integer);
insert into order_items(order_id, product_id, quantity) values(1,1,10);
insert into order_items(order_id, product_id, quantity) values(2,2,20);
insert into order_items(order_id, product_id, quantity) values(3,3,30);
insert into order_items(order_id, product_id, quantity) values(4,2,2);
insert into order_items(order_id, product_id, quantity) values(5,3,3);
-- select it1.product_id from order_items as it1;

select p.title, SUM(quantity) as total
from order_items AS o
inner join products AS p on o.product_id = p.product_id
group by p.title, p.title
order by total DESC
LIMIT 3

Cat	33
Banana	22
Apple	10


create table people(person_id integer, name varchar(100) , mother_id integer , father_id integer);
insert into people(person_id, name, mother_id, father_id) values(1, 'father', NULL, NULL);
insert into people(person_id, name, mother_id, father_id) values(2, 'mother', NULL, NULL);
insert into people(person_id, name, mother_id, father_id) values(3, 'son', 1, 2);
insert into people(person_id, name, mother_id, father_id) values(4, 'son2', NULL, NULL);
-- select * from people where mother_id is null and father_id is null;

select * from people p
where not exists
(
select *
from people ch
where ch.mother_id = p.person_id or ch.father_id = p.person_id
);


select p.* from people p
left outer join people ch
on p.person_id = ch.mother_id or p.person_id = ch.father_id
where ch.father_id is NULL;



create table person(id integer, title varchar(100));

insert into person(id, title) values(1, "Hello");
insert into person(id, title) values(1, "Hello");
insert into person(id, title) values(2, "Hello2");
insert into person(id, title) values(NULL, "Hello3");
select count(*) , count(id) from person
-- 4	3


class Student:
    def __init__(self,name,date_string,*args):
        self.name = name
        self.birthdate = date_string

s = Student("girish","20/12/1233")
print(s)



#
create table person(id integer, title varchar(100) , favoirite_flavour_id integer);
create table ice_cream_flavours(flavour_id integer, flavour_name  varchar(100));




insert into person(id, title,favoirite_flavour_id) values(1, "Girish Gupta",1);
insert into person(id, title,favoirite_flavour_id) values(2, "Manish Gupta",1);

insert into ice_cream_flavours(flavour_id, flavour_name) values(1, 'Vanila');
insert into ice_cream_flavours(flavour_id, flavour_name) values(2, 'Butter Scotch');


select f1.flavour_name , fav.number_of_fab
from ice_cream_flavours f1
join (
select favoirite_flavour_id , count(*) as number_of_fab
from person
group by favoirite_flavour_id
) fav on f1.flavour_id = fav.favoirite_flavour_id



select f.flavour_name , count(p.favoirite_flavour_id)
from ice_cream_flavours f
left join person p on f.flavour_id = p.favoirite_flavour_id
group by f.flavour_name;
-- Butter Scotch	0
-- Vanila	2

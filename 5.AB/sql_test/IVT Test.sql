/* Úvodní konfigurace */
drop database if exists test;
create database test;

use test;
create table if not exists tables (
        id int not null,
        chairs int not null,
        primary key(id)
);

delete from tables;
insert into tables values (1, 4);
insert into tables values (2, 5);
insert into tables values (3, 3);
insert into tables values (4, 6);
insert into tables values (5, 10);
insert into tables values (6, 4);

create table if not exists menu (
        id int not null,
        name text not null,
        price float not null,
        primary key(id)
);

delete from menu;
insert into menu values (1, "Řízek", 130);
insert into menu values (2, "Smažák", 100);
insert into menu values (3, "Hermoš s chlebem", 90);
insert into menu values (4, "Utopenec", 120);

create table if not exists bookings (
        id int not null,
        hour int not null,
        tableId int not null,
        primary key(id),
        foreign key(tableId) references tables(id)
);

delete from bookings;
insert into bookings values (1, 14, 3);
insert into bookings values (2, 17, 6);
insert into bookings values (3, 17, 4);

/* -------------------------------------------------- */
/* TADY ZAČÍNÁ TEST --------------------------------- */
/* -------------------------------------------------- */

/* Zadání 1: Vytvořte tabulku objednávek. Každá objednávka sestává z
        - čísla stolu (berte z tabulky 'tables'),
        - položky v menu (berte z tabulky 'menu'),
        - informace o tom, zda byla zaplacena, či ne. */





/* Zadání 2: Stůl číslo 3 si přeje zaplatit. Vyberte z tabulky objednávek
   všechny objednávky, které patří stolu 3. */
   
   



/* Zadání 3: Stůl číslo 3 zaplatil. Označte všechny jeho objednávky za
   zaplacené v tabulce objednávek. */





/* Zadání 4: Přišla rezervace na stůl číslo 1 od 19 hodin. Zaneste tento
   údaj do tabulky rezervací. */





/* Zadání 5: Od 16 hodin je plánovaná odstávka elektřiny v oblasti.
   Restaurace se pročež musí zavřít. Smažte v tabulce rezerací všechny
   rezervace od 15 hodin dále. */





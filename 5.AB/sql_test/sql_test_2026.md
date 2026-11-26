# SQL Test pro 5.AB

## Úloha 1

Slučte tabulky `Customer` a `Invoice` tak, aby vzniklá tabulka obsahovala tyto sloupce:
- jméno zákazníka (`FirstName`)
- příjmení zákazníka (`LastName`)
- email (`Email`)
- datum vystavení faktury (`InvoiceDate`)
- zaplacená částka (`Total`)
Z této tabulky vyberte pouze zákazníky z USA a faktury z datem vystavení pozdějším 1. 1. 2010.

| FirstName | LastName | Email               | InvoiceDate         | Total |
| --------- | -------- | ------------------- | ------------------- | ----- |
| Harris    | Frank    | fharris@google.com  | 2013-04-01 00:00:00 | 3.96  |

### Bonus

Slučte k těmto dvěma tabulkám navíc tabulku `InvoiceLine` a `Track`, a místo `Total` v původní tabulce ukazujte cenu za jednotku (`UnitPrice`) a název tracku (`Name`), který zákazník zakoupil.

| FirstName | LastName | Email               | InvoiceDate         | Name                    | UnitPrice |
| --------- | -------- | ------------------- | ------------------- | ----------------------- | --------- |
| Harris    | Frank    | fharris@google.com  | 2013-04-01 00:00:00 | Opachorô (Live)         | 0.99      |
| Harris    | Frank    | fharris@google.com  | 2013-04-01 00:00:00 | A Novidade (Live)       | 0.99      |
| Harris    | Frank    | fharris@google.com  | 2013-04-01 00:00:00 | De Ouro E Marfim (Live) | 0.99      |
| Harris    | Frank    | fharris@google.com  | 2013-04-01 00:00:00 | Lamento De Carnaval     | 0.99      |

---

## Úloha 2

Vložte to tabulky `Invoice` fakturu k datu 14. 5. 2021 a zákazníkovi se jménem Julia Barnett (**nemáte** povoleno hledat její ID manuálně) a celkovou částkou 4.50. Jiné než povinné sloupce smíte vyplnit, ale nemusíte.

---

## Úloha 3

V tabulce `Genre` aktualizujte název žánru s ID 27 na `Horror`. Pokud takové ID v tabulce `Genre` neexistuje, má být nový žánr **automaticky** přidán.

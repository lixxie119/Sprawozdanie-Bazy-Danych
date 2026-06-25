============
Wprowadzenie
============

Niniejsze sprawozdanie zostało przygotowane w ramach zajęć laboratoryjnych z zakresu projektowania, implementacji oraz administracji bazami danych. Celem realizowanych ćwiczeń było zdobycie praktycznych umiejętności związanych z tworzeniem modeli danych, definiowaniem struktur bazodanowych, wykonywaniem zapytań SQL oraz obsługą systemów zarządzania bazami danych PostgreSQL i SQLite. Istotnym elementem zajęć było również poznanie metod komunikacji aplikacji z bazą danych przy wykorzystaniu języka Python oraz odpowiednich bibliotek programistycznych.

Wykorzystane repozytoria
========================

Pliki źródłowe sprawozdania

* https://github.com/karaskamil/Sprawozdanie-Bazy-Danych

Badania literaturowe

* https://github.com/karaskamil/Sprzet-dla-bazy-danych.git
* https://github.com/Youarecheck/Bazy_Danych_Tematyczne_Repo_MK.git
* https://github.com/pawlos1337/Bazy-danych-temat.git
* https://github.com/OskarProgrammer/monitorowanie_i_diagnostyka.git
* https://github.com/KMachoK/Tematyczne.git
* https://github.com/domino0472/Partycjonowani-Danych
* https://github.com/oski486/BazyDanych-Subject.git
* https://github.com/Koko9077/Kopie-zapasowe-i-odzyskiwanie-danych.git

Publiczne repozytoria wykorzystane do ćwiczeń laboratoryjnych

* https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs

Przebieg Laboratoriów
======================

Podczas ćwiczeń laboratoryjnych wykonywano zadania obejmujące nawiązywanie połączeń z bazami danych przy użyciu Pythonowych bibliotek SQLite3 oraz Psycopg, wykorzystanie plików konfiguracyjnych JSON przechowujących dane uwierzytelniające, a także realizację wsadowego wprowadzania danych do baz danych. W środowisku pgAdmin przeprowadzano bardziej zaawansowane operacje na demonstracyjnej bazie Northwind, obejmujące selekcję danych, sortowanie wyników, grupowanie rekordów, wykorzystanie funkcji agregujących, wykonywanie złączeń pomiędzy tabelami oraz stosowanie funkcji wierszowych. Dodatkowo realizowano ćwiczenia związane z pracą na zdalnym serwerze Linux poprzez połączenie SSH przy użyciu programu PuTTY oraz wykonywanie poleceń SQL za pomocą narzędzia ``psql``.

Przedstawiony w raporcie projekt obejmuje również proces planowania i dokumentowania bazy danych, począwszy od opracowania modelu konceptualnego, poprzez model logiczny uwzględniający zasady normalizacji, aż do przygotowania modelu fizycznego oraz implementacji struktury bazy danych. Następnie zaprezentowano proces definiowania tabel, wprowadzania danych oraz przygotowania przykładowych zapytań realizujących wymagane operacje na zgromadzonych danych.

Wnioski z przeprowadzonych ćwiczeń i eksperymentów
===================================================

Przeprowadzone ćwiczenia laboratoryjne pozwoliły na zdobycie praktycznego doświadczenia w pracy z relacyjnymi bazami danych oraz systemem PostgreSQL. Szczególnie istotne okazało się zrozumienie procesu projektowania bazy danych, ponieważ poprawnie przygotowany model konceptualny i logiczny znacząco ułatwia późniejszą implementację oraz rozwój systemu.

Ćwiczenia wykazały również, że efektywne wykorzystanie języka SQL umożliwia realizację złożonych operacji analitycznych przy stosunkowo niewielkiej liczbie poleceń. Zastosowanie złączeń, grupowania oraz funkcji agregujących pozwala na szybkie pozyskiwanie informacji z dużych zbiorów danych. Praktyczna praca z bazą Northwind umożliwiła sprawdzenie działania tych mechanizmów na rzeczywistych i rozbudowanych strukturach danych.

Dodatkowo potwierdzono przydatność narzędzi programistycznych takich jak Jupyter Notebook, Psycopg oraz SQLite3 w procesie integracji aplikacji z bazą danych. Wykorzystanie wsadowego wprowadzania danych pozwala znacząco zwiększyć wydajność operacji importu, natomiast przechowywanie parametrów połączenia w plikach konfiguracyjnych poprawia organizację projektu i bezpieczeństwo aplikacji.

Realizacja wszystkich ćwiczeń pozwoliła na zdobycie wiedzy obejmującej zarówno aspekty projektowe, jak i praktyczne wykorzystanie systemów baz danych, co stanowi podstawę do tworzenia bardziej zaawansowanych aplikacji korzystających z relacyjnych baz danych.

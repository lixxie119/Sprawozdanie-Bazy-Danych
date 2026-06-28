============
Wprowadzenie
============

Niniejszy raport stanowi podsumowanie zagadnień realizowanych w ramach zajęć laboratoryjnych z przedmiotu bazy danych. Dokument omawia narzędzia, techniki projektowe oraz metody zasilania i odpytywania struktur relacyjnych. Kluczowym elementem opracowania jest analiza porównawcza dwóch systemów zarządzania bazami danych (DBMS): zaawansowanego, serwerowego rozwiązania **PostgreSQL** oraz lekkiej, bezserwerowej bazy **SQLite**. Praca uwzględnia pełną ścieżkę tworzenia baz danynch — od modelowania, aż po fizyczną implementację i optymalizację zapytań SQL.

Spis użytych repozytoriów
=========================

W trakcie realizacji projektu wykorzystano następujące repozytoria na platformie Github:

* **Grupowe repozytorium z plikami projektowymi:** `https://github.com/karaskamil/Sprawozdanie-Bazy-Danych` - zawierające zebrane wszystkie repozytoria z badaniami literaturowymi oraz grupowo pisane rozdziały raportu.
* **Indywidualne repozytorium z plikami projektowymi:** `https://github.com/lixxie119/Sprawozdanie-Bazy-Danych` - w stosunku do repozytorium grupowego, dodane zostało wprowadzenie pisane indywidualnie oraz drobne poprawki stylistyczne.
* **Badania literaturowe - sprzęt dla baz danych:** `https://github.com/karaskamil/Sprzet-dla-bazy-danych.git` - zawierające pierwszy podrozdział badań literaturowych.
* **Badania literaturowe - konfiguracja bazy danych:** `https://github.com/Youarecheck/Bazy_Danych_Tematyczne_Repo_MK.git` - zawierające drugi podrozdział badań literaturowych.
* **Badania literaturowe - kontrola i konserwacja:** `https://github.com/pawlos1337/Bazy-danych-temat.git` - zawierające trzeci podrozdział badań literaturowych.
* **Badania literaturowe - monitorowanie i diagnostyka:** `https://github.com/OskarProgrammer/monitorowanie_i_diagnostyka.git` - zawierające czwarty podrozdział badań literaturowych.
* **Badania literaturowe - wydajność, skalowanie i replikacja:** `https://github.com/KMachoK/Tematyczne/blob/main/index.rst` - zawierające piąty podrozdział badań literaturowych.
* **Badania literaturowe - partycjonowanie danych:** `https://github.com/domino0472/Partycjonowani-Danych` - zawierające szósty podrozdział badań literaturowych.
* **Badania literaturowe - bezpieczeństwo:** `https://github.com/oski486/BazyDanych-Subject.git` - zawierające siódmy podrozdział badań literaturowych.
* **Badania literaturowe - kopie zapasowe i odzyskiwanie danych:** `https://github.com/Koko9077/Kopie-zapasowe-i-odzyskiwanie-danych.git` - zawierające ósmy podrozdział badań literaturowych.

Wprowadzenie tematyczne do ćwiczeń i eksperymentów
==================================================

Celem przeprowadzonych zajęć laboratoryjnych było zapoznanie z projektowaniem i wdrożeniem baz danych. W zadaniach laboratoryjnych, wykonaliśmy relacyjną bazę danych wspomagającą zarządzanie systemem wypożyczalni samochodów. Eksperymenty polegały na zbadaniu, jak teoretyczne założenia relacyjnego modelu danych zachowują się w dwóch  różnych środowiskach wykonawczych.

W ramach zadań laboratoryjnych przeprowadzono kolejne kroki:
1. Opracowanie badań literaturowych:** Podstawa teoretyczna do dalszych zadań, w przypadku naszej grupy opracowany został temat sprzęt dla baz danych.
2. **Modelowanie i normalizacja:** Stworzenie modelu konceptualnego, logicznego z normalizacją oraz fizycznego dla konkretnej bazy danych (wypożyczalnia).
3. **Migracja i mechanizmy wsadowe:** Porównanie wydajności i elastyczności graficznego importu przez narzędzia pgAdmin (wykorzystujące komendę ``COPY``) z programistycznym ładowaniem danych przy użyciu biblioteki Pandas w Pythonie.
4. **Analityka SQL:** Konstruowanie złożonych kwerend filtrujących, grupujących oraz łączących dane w celu wyciągnięcia kluczowych wskaźników efektywności (KPI) dla przedsiębiorstwa, zarówno dla PostgreSQL, jak i SQLite.

Struktura raportu
=================

Opracowanie zostało podzielone na następujące rozdziały:

* **Badania literaturowe:** Przedstawienie podstaw teoretycznych związanych z tworzeniem, administracją i utrzymaniem systemów bazodanowych na przykładzie architektury PostgreSQL.
* **Planowanie baz danych i tworzenie dokumentacji:** Opis procesu modelowania konceptualnego, logicznego (z uwzględnieniem normalizacji) oraz fizycznego z podziałem na dialekty PostgreSQL i SQLite.
* **Definiowanie bazy danych i wprowadzanie danych do bazy:** Komentarz z wykonania skryptów oraz analiza metod masowego zasilania tabel z plików CSV.
* **Zapytania do bazy danych:** Prezentacja oraz omówienie wykonanych zapytań SQL realizujących zadania postawione w instrukcji laboratoryjnej.

Wnioski z przeprowadzonych ćwiczeń
==================================

Przeprowadzone ćwiczenia dały możliwość praktycznego sprawdzenia informacji o obsłudze baz danych, a także pogłębienia zrozumienia procesu projektowania baz danych. Pokazały różnice między implementacjami SQL oraz pozwoliły na porównanie poleceń przy bardziej złożonych operacjach analitycznych. W praktyczny sposób pokazały również jak przydatna jest metoda wsadowego dodawania danych za pomocą pliku .csv.

Badania laboratoryjne wykazały, że wybór systemu DBMS musi być podyktowany architekturą docelowego systemu. **PostgreSQL** oferuje bezpieczeństwo, zaawansowane mechanizmy transakcyjne i wysoką wydajność przy operacjach wielowątkowych, jednak wymaga dedykowanej administracji. Z kolei **SQLite** doskonale sprawdza się w scenariuszach lokalnych, oferując zerowy koszt konfiguracji kosztem braku zaawansowanego współbieżnego zapisu. 

Dodatkowo proces normalizacji potwierdził, że poprawne zaprojektowanie bazy danych w 3NF w fazie planowania eliminuje ryzyko wystąpienia anomalii podczas operacji modyfikacji danych i upraszcza późniejsze utrzymanie kodu aplikacji.

Realizacja ćwiczeń pomogła zdobyć praktyczne informacje oraz umiejętności, które stanowią podstawę do dalszej, bardziej zaawansowanej pracy z bazami danych.

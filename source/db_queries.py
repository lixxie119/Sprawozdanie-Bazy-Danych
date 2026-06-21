# -*- coding: utf-8 -*-
"""
Moduł realizujący zaawansowane zapytania do baz danych SQLite oraz PostgreSQL.
Zawiera dedykowane funkcje operujące na tabelach systemu wypożyczalni pojazdów.
"""

import sqlite3
import psycopg
from typing import List, Tuple, Any

# =============================================================================
# FUNKCJE DLA BAZY SQLITE
# =============================================================================

def sqlite_get_client_summary(db_path: str) -> List[Tuple[str, str]]:
    """
    Generuje sformatowane zestawienie klientów wraz z ich miejscem zamieszkania.

    Wykorzystuje funkcje wierszowe (konkatenację ciągów tekstowych oraz 
    funkcję UPPER) w celu ujednolicenia prezentacji danych do raportu.

    Zadanie/Cel:
        Przygotowanie danych adresowych w formacie gotowym do wydruku etykiet.

    Argumenty:
        db_path (str): Ścieżka lokalna do pliku bazy danych SQLite (*.db).

    Zwraca:
        List[Tuple[str, str]]: Lista krotek zawierających (pelne_nazwisko, adres_poczty),
        gdzie nazwisko jest pisane wielkimi literami.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT 
            UPPER(imie || ' ' || nazwisko) AS pelne_nazwisko,
            (kod_pocztowy || ' ' || miasto || ', ul. ' || adres) AS adres_poczty
        FROM klient;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def sqlite_get_popular_drive_types(db_path: str, min_rentals: int) -> List[Tuple[str, int]]:
    """
    Analizuje popularność typów napędów pojazdów na podstawie liczby wypożyczeń.

    Wykorzystuje funkcje agregujące (COUNT), złączenia wielotabelowe (JOIN)
    oraz klauzulę agregacji grupowej z filtrowaniem (GROUP BY ... HAVING).

    Zadanie/Cel:
        Optymalizacja zakupów nowej floty poprzez identyfikację najchętniej 
        wybieranych rodzajów napędów.

    Argumenty:
        db_path (str): Ścieżka lokalna do pliku bazy danych SQLite.
        min_rentals (int): Minimalny próg liczby wypożyczeń kwalifikujący grupę.

    Zwraca:
        List[Tuple[str, int]]: Pary zawierające nazwę napędu oraz sumaryczną liczbę najmów.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT p.naped, COUNT(w.wypozyczeniaId) AS liczba_wypozycen
        FROM pojazdy p
        JOIN wypozyczenia w ON p.pojazdId = w.pojazdId
        GROUP BY p.naped
        HAVING COUNT(w.wypozyczeniaId) >= ?;
    """
    cursor.execute(query, (min_rentals,))
    results = cursor.fetchall()
    conn.close()
    return results


def sqlite_get_all_active_and_historical_ids(db_path: str) -> List[Tuple[str, str]]:
    """
    Konsoliduje unikalne identyfikatory pojazdów z różnych etapów cyklu życia.

    Wykorzystuje operator zbiorowy (UNION) do połączenia zbiorów identyfikatorów
    z tabeli bieżącego stanu technicznego oraz historycznego rejestru wypożyczeń.

    Zadanie/Cel:
        Weryfikacja spójności danych i wykrywanie pojazdów niewypożyczonych ani razu w bazie.

    Argumenty:
        db_path (str): Ścieżka lokalna do pliku bazy danych SQLite.

    Zwraca:
        List[Tuple[str, str]]: Zbiór krotek (pojazdId, zrodlo_danych) bez duplikatów.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT pojazdId, 'STAN_TECHNICZNY' AS zrodlo FROM stan_techniczny
        UNION
        SELECT pojazdId, 'HISTORIA_WYPOZYCZEN' AS zrodlo FROM wypozyczenia;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def sqlite_get_vehicles_above_average_mileage(db_path: str) -> List[Tuple[str, str, int]]:
    """
    Wyszukuje pojazdy, których przebieg przewyższa średnią.

    Wykorzystuje podzapytanie nieskorelowane w klauzuli WHERE do dynamicznego
    obliczenia średniej wartości przebiegu.

    Zadanie/Cel:
        Wytypowanie samochodów do priorytetowego przeglądu okresowego lub sprzedaży.

    Argumenty:
        db_path (str): Ścieżka lokalna do pliku bazy danych SQLite.

    Zwraca:
        List[Tuple[str, str, int]]: Lista pojazdów (pojazdId, rejestracja, przebieg).
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT pojazdId, rejestracja, przebieg 
        FROM pojazdy 
        WHERE przebieg > (SELECT AVG(przebieg) FROM pojazdy);
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def sqlite_get_clients_with_multiple_rentals(db_path: str) -> List[Tuple[str, str, int]]:
    """
    Wyszukuje stałych klientów przy użyciu zaawansowanego podzapytania skorelowanego.

    Podzapytanie w klauzuli WHERE odwołuje się do zewnętrznego rekordu klienta,
    zliczając jego indywidualne operacje w tabeli wypożyczeń.

    Zadanie/Cel:
        Identyfikacja partnerów biznesowych kwalifikujących się do rabatów lojalnościowych.

    Argumenty:
        db_path (str): Ścieżka lokalna do pliku bazy danych SQLite.

    Zwraca:
        List[Tuple[str, str, int]]: Dane klientów (imie, nazwisko, łączna_liczba_wypożyczeń).
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT k.imie, k.nazwisko,
               (SELECT COUNT(*) FROM wypozyczenia w WHERE w.klientId = CAST(k.klientId AS TEXT)) AS lacznie
        FROM klient k
        WHERE (
            SELECT COUNT(*) FROM wypozyczenia w WHERE w.klientId = CAST(k.klientId AS TEXT)
        ) > 1;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# =============================================================================
# FUNKCJE DLA BAZY POSTGRESQL
# =============================================================================

def pg_get_expired_inspections(db_config: dict) -> List[Tuple[Any, ...]]:
    """
    Pobiera listę pojazdów, których termin przeglądu technicznego minął.

    Wykorzystuje funkcje wierszowe PostgreSQL do operacji na datach (CURRENT_DATE)
    oraz obliczania interwałów czasowych (wiek wpisu / różnica dni).

    Zadanie/Cel:
        Zapewnienie bezpieczeństwa prawnego poprzez niedopuszczenie do ruchu
        samochodów bez ważnych badań.

    Argumenty:
        db_config (dict): Słownik konfiguracyjny połączenia (host, dbname, user, password, port).

    Zwraca:
        List[Tuple[Any, ...]]: Dane (pojazdId, rejestracja, opoznienie_w_dniach).
    """
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT p.pojazdId, p.rejestracja, (CURRENT_DATE - s.data_przegladu) AS dni_po_terminie
                FROM pojazdy p
                JOIN stan_techniczny s ON p.pojazdId = s.pojazdId
                WHERE s.data_przegladu < CURRENT_DATE;
            """
            cursor.execute(query)
            return cursor.fetchall()


def pg_get_financial_payment_report(db_config: dict) -> List[Tuple[Any, ...]]:
    """
    Generuje raport księgowy dotyczący form płatności i ich popularności.

    Implementuje funkcje agregujące (COUNT) wraz z grupowaniem, sortowaniem
    oraz wielopoziomowym łączeniem danych.

    Zadanie/Cel:
        Analiza preferencji płatniczych klientów w celach optymalizacji prowizji bankowych.

    Argumenty:
        db_config (dict): Słownik konfiguracyjny połączenia PostgreSQL.

    Zwraca:
        List[Tuple[Any, ...]]: Statystyki (platnosc, liczba_transakcji).
    """
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT platnosc, COUNT(wypozyczeniaId) AS wolumen_transakcji
                FROM wypozyczenia
                WHERE platnosc IS NOT NULL
                GROUP BY platnosc
                ORDER BY wolumen_transakcji DESC;
            """
            cursor.execute(query)
            return cursor.fetchall()


def pg_get_system_chronology_report(db_config: dict) -> List[Tuple[str, str, str]]:
    """
    Generuje chronologiczny rejestr zdarzeń operacyjnych w systemie (oś czasu).

    Wykorzystuje operator UNION do skonsolidowania informacji o datach zawarcia 
    umów wypożyczeń (wraz z formą płatności) oraz datach wykonanych przeglądów 
    technicznych z tabeli stan_techniczny.

    Zadanie/Cel:
        Prezentacja globalnej linii czasu działań firmy na jednym raporcie.

    Argumenty:
        db_config (dict): Słownik konfiguracyjny połączenia PostgreSQL.

    Zwraca:
        List[Tuple[str, str, str]]: Rekordy w formacie (data_zdarzenia, typ_zdarzenia, opis).
    """
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT CAST("data" AS TEXT) AS data_zdarzenia, 'WYPOZYCZENIE' AS typ, ('Platnosc: ' || platnosc) AS opis 
                FROM wypozyczenia
                
                UNION
                
                SELECT CAST(data_przegladu AS TEXT) AS data_zdarzenia, 'PRZEGLAD TECHNICZNY' AS typ, ('Pojazd ID: ' || pojazdId) AS opis 
                FROM stan_techniczny
                
                ORDER BY data_zdarzenia DESC;
            """
            cursor.execute(query)
            return cursor.fetchall()


def pg_get_vehicles_never_rented(db_config: dict) -> List[Tuple[Any, ...]]:
    """
    Wyszukuje pojazdy widniejące w kartotece, które nigdy nie zostały wypożyczone.

    Wykorzystuje podzapytanie nieskorelowane (operator NOT IN) do wykluczenia 
    pojazdów przypisanych do jakiegokolwiek kontraktu.

    Zadanie/Cel:
        Wykrywanie martwych zasobów generujących koszty stałe bez przychodu.

    Argumenty:
        db_config (dict): Słownik konfiguracyjny połączenia PostgreSQL.

    Zwraca:
        List[Tuple[Any, ...]]: Wykaz pojazdów (pojazdId, rejestracja, silnik).
    """
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT pojazdId, rejestracja, silnik 
                FROM pojazdy 
                WHERE pojazdId NOT IN (
                    SELECT DISTINCT pojazdId FROM wypozyczenia WHERE pojazdId IS NOT NULL
                );
            """
            cursor.execute(query)
            return cursor.fetchall()


def pg_get_faulty_vehicles_report(db_config: dict) -> List[Tuple[Any, ...]]:
    """
    Zwraca szczegółowe opisy uszkodzeń floty bazując na zaawansowanym podzapytaniu.

    Wykorzystuje podzapytanie skorelowane (klauzula EXISTS) sprawdzające, czy dla danego 
    pojazdu istnieją krytyczne wpisy o braku sprawności w tabeli stanu technicznego.

    Zadanie/Cel:
        Przekazanie raportu uszkodzeń mechanikom serwisowym.

    Argumenty:
        db_config (dict): Słownik konfiguracyjny połączenia PostgreSQL.

    Zwraca:
        List[Tuple[Any, ...]]: Lista (rejestracja, zarysowania_lub_usterki).
    """
    with psycopg.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            query = """
                SELECT p.rejestracja, 
                       (SELECT s.zarysowania FROM stan_techniczny s WHERE s.pojazdId = p.pojazdId) AS opis_usterki
                FROM pojazdy p
                WHERE EXISTS (
                    SELECT 1 
                    FROM stan_techniczny st 
                    WHERE st.pojazdId = p.pojazdId AND st.sprawne = FALSE
                );
            """
            cursor.execute(query)
            return cursor.fetchall()
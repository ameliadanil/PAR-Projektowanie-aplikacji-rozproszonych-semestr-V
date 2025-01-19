# PAR-Projektowanie-aplikacji-rozproszonych-semestr-V
Repozytorium z projektem z przedmiotu- Projektowanie aplikacji rozproszonych, semestr V, prowadzący: dr inż. P Bobiński

Aplikacja Quiz to prosta aplikacja rozproszona składająca się z serwera i klienta, które komunikują się za pomocą protokołu Socket.IO. Umożliwia ona przeprowadzanie quizu w czasie rzeczywistym, w którym użytkownik odpowiada na pytania wysyłane przez serwer.

Funkcjonalności aplikacji:
1. Połączenie klient-serwer: Klient łączy się z serwerem i inicjuje quiz. 
2. Zadawanie pytań:
Serwer przesyła pytania wraz z możliwymi odpowiedziami do klienta.
Klient wyświetla pytania i umożliwia użytkownikowi wybór odpowiedzi.
3. Odpowiedzi i wyniki:
Klient przesyła odpowiedź użytkownika na serwer.
Serwer ocenia odpowiedź jako poprawną lub niepoprawną i aktualizuje wynik użytkownika.
4. Zakończenie quizu:
Po udzieleniu odpowiedzi na wszystkie pytania serwer wysyła podsumowanie wyniku użytkownika.

Przepływ działania aplikacji:
1. Klient przesyła swoją nazwę użytkownika do serwera.
2. Serwer rozpoczyna quiz, przesyłając pytania jedno po drugim.
3. Klient wyświetla pytanie, a użytkownik odpowiada poprzez wybór odpowiedzi.
4. Serwer analizuje odpowiedzi użytkownika i aktualizuje wynik.
5. Po zakończeniu quizu serwer wyświetla końcowy wynik użytkownika i rozłącza klienta.

Technologie i biblioteki:
Python: Język programowania użyty do stworzenia aplikacji.
Flask: Framework do stworzenia serwera.
Socket.IO: Biblioteka do obsługi komunikacji w czasie rzeczywistym między klientem a serwerem.

Aplikacja działa lokalnie, co oznacza, że zarówno serwer, jak i klient są uruchamiane na tym samym komputerze, korzystając z adresu 127.0.0.1 (localhost) i portu 5000. Jest to prosty przykład aplikacji rozproszonej, który można rozbudowywać o dodatkowe funkcjonalności.

*** Problemy na które się natknęłam podczas tworzenia aplikacji Quiz:

1. Problemy z konfiguracją środowiska:
Brak zainstalowanych wymaganych bibliotek, takich jak Flask, Flask-SocketIO, czy socketio.
Rozwiązanie: Zainstalowałam brakujące pakiety za pomocą polecenia pip install.

2. Konflikty wersji bibliotek:
Niekompatybilne wersje Flask-SocketIO i python-socketio powodowały błędy.
Rozwiązanie: Zainstalowano odpowiednie wersje bibliotek, zgodne z dokumentacją Flask-SocketIO.

3. Błędy połączenia klient-serwer:
Klient nie mógł połączyć się z serwerem lub serwer nie reagował na żądania.
Rozwiązanie: Upewniono się, że serwer jest uruchomiony przed klientem oraz że działa na poprawnym porcie 127.0.0.1:5000. Dodatkowo miałam problem z Windows Defender Firewall, który blokował komunikację pomiędzy app i client, dodałam wyjątki w ustawieniach zapory, pozwalając na komunikację pomiędzy nimi.


# CarShopPhotoMicroservice

Microservice odpowiedzialny za przechowywanie zdjęć dla systemu **CarShopBackend**.
Serwis obsługuje odczyt i zapis zdjęć samochodów.

## 🧱 Technologie

* Python 3.12.3
* FastAPI
* Pillow / biblioteki do obróbki zdjęć
* REST API

## 📦 Wymagania

* Python **3.12.3**
* pip
* virtualenv (zalecane)

## 🚀 Uruchomienie lokalne

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/F1vus/CarShopPhotoMicroservice.git
cd CarShopPhotoMicroservice
```

### 2. Utworzenie środowiska wirtualnego

```bash
python3.12 -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

### 4. Uruchomienie serwera

```bash
cd app/
fastapi dev main.py
```

Serwis powinien być dostępny pod:

```
http://localhost:8000
```

Dokumentacja API:

```
http://localhost:8000/docs
```

## 📁 Struktura projektu

```
app/
 ├── main.py            # punkt startowy aplikacji
 ├── api/               # endpointy API
 ├── services/          # logika biznesowa
 ├── models/            # modele danych
 ├── db/                # konfiguracja bazy danych
 └── utils/             # operacje na zdjęciach
requirements.txt
```

## 🧪 Test działania

Przykładowy upload zdjęcia:

```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@car.jpg"
```

## 🛠 Integracja z CarShopBackend

Serwis jest przeznaczony do komunikacji z backendem sklepu samochodowego.
Backend wysyła żądania HTTP do tego mikroserwisu w celu:

* dodania zdjęcia
* pobrania zdjęcia
* edycji (resize/crop)

## 📌 Wersja lokalna

Uruchomiono i przetestowano na:

```
Python 3.12.3
```

## 👨‍💻 Autor

F1vus

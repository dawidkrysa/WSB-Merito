# WSB-Merito

Rozwiązania zadań z przedmiotów realizowanych na studiach w WSB Merito, napisane w Pythonie.

## Struktura

Każdy przedmiot ma własny katalog, a w nim podkatalogi według tematów zajęć:

```
├── Ekonometria/
│   └── Metoda najmniejszych kwadratów/   # regresja liniowa, współczynnik determinacji
└── Statystyka Opisowa/
    ├── Szeregi rozdzielcze, histogram/   # rozkład liczebności, histogram
    └── Średnia, mediana/                 # średnia, mediana, kwartyle
```

Każdy plik `zadanie_N.py` zawiera treść zadania w komentarzu, dane wejściowe i rozwiązanie.

## Uruchomienie

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt

python "Statystyka Opisowa/Średnia, mediana/zadanie_5.py"
```

## Autor

Dawid Krysa

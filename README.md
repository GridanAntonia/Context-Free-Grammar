# Context-Free Grammar Implementation

Programul meu implementează următorul CFG:
        
```bash
S -> aSb | ε
```

## Definirea CFG-ului

Conform definiției, vom separa simbolurile gramticii în categoriile specifice: terminale, non-terminale, simbol de start și regulile de producție.

Non-terminale : "S"

Terminale : "a", "b"

Simbol de start: "S"

Regulile de producție: S -> aSb | ε



## Generarea string-urilor

Folosind o funcție recursivă, la întâlnirea unui non-terminal, alegem random o regulă de producție. Astfel, string-ul inițial se modifică. Când string-ul nu mai conține non-terminale sau numărul de pași maxim a fost depășit, funcția se oprește.

Funcția returnează fie caracterul ε, fie un șir de forma aaa...aaabbb...bbb, cu număr egal de a-uri și b-uri.

``` bash
aabb
aaabbb
ε
aabb
ε
```

## Derivare

Pornind de la simbolul de start, "S", vom alege prima regulă de producție până se atinge numărul de a-uri și b-uri dorit. La final, vom alege să înlocuim simbolul "S" cu ε, pentru a avea un cuvânt care conține doar terminale.

```bash
Target string:  
aaaaabbbbb

S ->  aSb ->  aaSbb ->  aaaSbbb ->  aaaaSbbbb ->  aaaaaSbbbbb ->  aaaaaεbbbbb =  aaaaabbbbb
```
## Testare

Se verifică liniar, dacă numărul de a-uri este egal cu numărul de b-uri și dacă a-urile sunt intercalate cu b-uruile. Funcția returnează True, dacă string-ul respectă toate regulile sau False, în caz contrar.

```bash
Target string: 
aabbb

False
-------------------
Target string: 
aaaabbbb

True

```

## Rulare

* Python3 instalat.
* Rulează fișierul main.py, rezultatele vor fi afișate în consolă.

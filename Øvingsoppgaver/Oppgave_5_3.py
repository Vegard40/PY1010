"""
Lag en funksjon som tar antall euro som input, regner om til NOK (norske kr) og dollar
(US Dollar). Funksjonen skal returnere begge svarene som s ̊a skrives til skjerm (konsoll). Du
kan bruke følgende omregninger: 1 euro = 10,42 NOK og 1 euro = 1,19 dollar (valutakurser
er hentet ut 28/9 2019, kl 11:53).
"""


def convert_euro():
    # Vekslingskurser
    rates = {"USD": 1.19, "NOK": 10.42}

    while True:
        # Spør brukeren om ønsket valuta og beløp
        currency = input("Hvilken valuta ønsker du å konvertere til? (USD/NOK): ").strip().upper()
        if currency not in rates:
            print("Ugyldig valuta. Vennligst velg enten USD eller NOK.")
            continue

        try:
            amount_euro = float(input("Hvor mange euro ønsker du å konvertere?: "))
        except ValueError:
            print("Ugyldig beløp. Vennligst skriv inn et tall.")
            continue

        # Konverter til ønsket valuta
        amount_converted = amount_euro * rates[currency]
        print(f"{amount_euro} euro er lik {amount_converted} {currency}.")
        break

# Kjør funksjonen
convert_euro()
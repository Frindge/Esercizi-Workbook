# Si consideri il software che gira su una macchina per il self-checkout. Un compito che deve essere in grado di
# svolgere è determinare quanto resto fornire quando l'acquirente paga un acquisto in contanti.
# Scrivete un programma che inizia leggendo un numero di centesimi dall'utente come un intero. Poi il vostro programma
# dovrebbe calcolare e mostrare le denominazioni delle monete che dovrebbero essere usate per dare quella quantità di
# resto al cliente. Il resto dovrebbe essere dato usando il minor numero possibile di monete. Supponiamo che la macchina
# sia caricata con penny, nichel, dimes, quarters, loonies e toonies.

# Una moneta da un dollaro è stata introdotta in Canada nel 1987. Viene chiamata loonie perché un lato della moneta ha
# un loone (un tipo di uccello) su di esso. La moneta da due dollari, chiamata toonie, fu introdotta 9 anni dopo.
# Il suo nome deriva dalla combinazione del numero due e il nome del loonie.

centesimi=int(input("inserire un numero intero di centesimi: "))
# rapporto in centesimi
nichel=5
dimes=10
quarters=25
loonies=100
toonies=200
#resto in nikel
print(centesimi // nichel, "nichel", centesimi % nichel,"centesimi")
#resto in dimes e centesimi residui
print(centesimi // dimes, "dimes", centesimi % dimes, "centesimi")
#resto in quarters e centesimi residui
print(centesimi // quarters, "quarters", centesimi % quarters, "centesimi")
#resto in loonies e centesimi residui
print(centesimi // loonies, "loonies", centesimi % loonies, "centesimi")
#resto in toonies e centesimi residui
print(centesimi // toonies, "toonies", centesimi % toonies, "centesimi")

    

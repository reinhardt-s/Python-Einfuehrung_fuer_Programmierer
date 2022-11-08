import prettytable

tbl = prettytable.PrettyTable()

tbl.add_column("Bezeichnung", ["Netflix", "Amazon"])
tbl.add_column(fieldname="Betrag", column=["-14.20", "-305.40"], align="r",)

print(tbl)


# challenge: formatiere hiermit deine bank_account ausgabe
#  Kapitel 10 - 3. Challenge
#  Herausforderung das alignment von bezeichnung linksbündig, betrag rechtbündig


from person import Person
from datetime import date 

P = Person("Teagan Liddle", date(2006, 5, 12))
print(P.initials())
print(P.is_birthday())
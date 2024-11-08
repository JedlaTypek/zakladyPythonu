import dateutil.utils
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *

now = datetime.now()
print("Datum a čas: " + str(now))

print("5 nejbližších velikonoc:")
for i in range(6):
    print(easter(2024+i))

vanoce = rrule(YEARLY,dtstart=now,bymonth=12,bymonthday=24,byweekday=SU)[0].year
print("Nejbližší štědrý den v neděli bude v roce " + str(vanoce))
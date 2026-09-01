#!/usr/bin/env python3

import ephem  
o=ephem.Observer()  
o.lat='51.3168'  
o.long='0.56'  
s=ephem.Sun()  
s.compute()  
print ephem.localtime(o.next_rising(s))
print ephem.localtime(o.next_transit(s))
print ephem.localtime(o.next_setting(s))
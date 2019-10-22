"""
== --> Value Equality
!= --> Not equal to
<  --> Less than
> --> Greater than
<= --> Less than equal to
>= --> Greater than equal to
"""
bool1 = 10 ==10
if bool1 is True:
    print('success')
else: print('unsuccessful')


bool2 = 10 !=10
if bool2 is True:
    print('success')
else: print('unsuccessful')

bool3 = 10 < 11
if bool3 is True:
    print('success')
else: print('unsuccessful')

bool4 = 10 > 11
if bool4 is True:
    print('success')
    if bool4 is False:
        print('Try')
else: print('unsuccessful')

bool5 = 10 >= 9
if bool5 is True:
    print('success')
else: print('unsuccessful')

bool6 = 10 <= 11 - 2
if bool6 is True:
    print('success')
else: print('unsuccessful')
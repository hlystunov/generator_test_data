import random, re
from elizabeth import Personal
from datetime import date
from uuid import uuid4

# Логин
def login(): return Personal('ru').username()

# E-mail
def mail(): return Personal('ru').email()

# Номер телефона
def phone(): return Personal('ru').telephone('8(9##)###-##-##')

# UUID
def uuid(): return uuid4().hex

# GUID
def guid(): return str(uuid4()).upper()

# GUID LOWER
def guid_lower(): return str(uuid4()).lower()

# ИНН ЮЛ
def inn_entity(): return inn(10)

# ИНН ИП
def inn_individual(): return inn(12)

# ФИО
def full_name():
    FIO = re.findall(r'\S+|\s+', Personal('ru').full_name(gender='male'))
    return FIO[2] + " " + FIO[0] + " Тестович"

# Дата рождения
def birdthay():
    random_day = date.fromordinal(random.randint(date.today().replace(year=1950).toordinal(),
                                                 date.today().replace(year=1990).toordinal())).strftime('%d.%m.%Y')
    return random_day

# Проверка на контрольную сумму
def ctrl_summ(nums, type):
    ctrl_type = {
        'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
    }
    n = 0
    l = ctrl_type[type]
    for i in range(0, len(l)):
        n += nums[i] * l[i]
    return n % 11 % 10

# СНИЛС
def snils():
    nums = [
        random.randint(1, 1) if x == 0
        else '-' if x == 3
        else '-' if x == 7
        else ' ' if x == 11
        else random.randint(0, 9)
        for x in range(0, 12)
    ]

    cont = (nums[10] * 1) + (nums[9] * 2) + (nums[8] * 3) + \
           (nums[6] * 4) + (nums[5] * 5) + (nums[4] * 6) + \
           (nums[2] * 7) + (nums[1] * 8) + (nums[0] * 9)

    if cont in (100, 101):
        cont = '00'

    elif cont > 101:
        cont = (cont % 101)
        if cont in (100, 101): cont = '00'
        elif cont < 10: cont = '0' + str(cont)

    elif cont < 10: cont = '0' + str(cont)

    nums.append(cont)
    return ''.join([str(x) for x in nums])

# Создание ИНН
def inn(l):
    nums = [
        random.randint(9, 9) if x == 0
        else random.randint(6, 6) if x == 1
        else random.randint(0, 9)
        for x in range(0, 9 if l == 10 else 10)
    ]

    if l == 10:
        n1 = ctrl_summ(nums, 'n1_10')
        nums.append(n1)

    elif l == 12:
        n2 = ctrl_summ(nums, 'n2_12')
        nums.append(n2)
        n1 = ctrl_summ(nums, 'n1_12')
        nums.append(n1)

    return ''.join([str(x) for x in nums])

# ОГРН ЮЛ
def ogrn_entity():
    nums = [
        1 if x == 0
        else random.randint(1, 9) if x == 4
        else random.randint(0, 9)
        for x in range(0, 11)
    ]

    nums.append(ctrl_summ(nums, 'n1_12'))
    ogrn = (int(''.join(str(x) for x in nums)) % 11)
    nums.append(0) if ogrn == 10 else nums.append(ogrn)
    return ''.join([str(x) for x in nums])

# ОГРН ИП
def ogrn_individual():
    while True:
        nums = [
            random.randint(3, 4) if x == 0
            else random.randint(1, 9) if x == 4
            else random.randint(0, 9)
            for x in range(0, 13)
        ]

        nums.append(ctrl_summ(nums, 'n1_12'))
        ogrn = (int(''.join(str(x) for x in nums)) % 13)

        if ogrn > 10:
            continue

        nums.append(0) if ogrn == 10 else nums.append(ogrn)
        return ''.join([str(x) for x in nums])


def luhn_residue(digits):
    return sum(sum(divmod(int(d)*(1 + i%2), 10))
                 for i, d in enumerate(digits[::-1])) % 10


def oms():
    part = ''.join(str(random.randrange(0, 9)) for _ in range(16 - 1))
    res = luhn_residue('{}{}'.format(part, 0))
    return '{}{}'.format(part, -res % 10)


def okpo():
    return get_okpo(False)


def okpo_individual():
    return get_okpo(True)


def get_okpo(infividual):
    nums = [
        random.randint(0, 9)
        for _ in range(0, 9 if infividual else 7)
    ]

    summ = 0

    for index, i in enumerate(nums):
        summ += (index+1)* i

    control = summ % 11

    if control == 10:
        summ = 0

        for index, i in enumerate(nums):
            j = index + 3

            if j > 10:
                j = j % 10

            summ += j * i

        control = summ % 11

        if control == 10:
            control = 0

    nums.append(control)

    return ''.join([str(x) for x in nums])

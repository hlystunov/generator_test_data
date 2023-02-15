token = '###################################'

from collections import OrderedDict

from returns import \
    inn_entity, inn_individual, ogrn_entity, ogrn_individual, \
    snils, full_name, birdthay, login, mail, phone, uuid, guid, oms, \
    okpo, okpo_individual, guid_lower, passport_number

actions = OrderedDict([
    ('ИНН', inn_entity),
    ('ИНН ФЛ', inn_individual),
    ('ОГРН', ogrn_entity),
    ('ОГРН ИП', ogrn_individual),
    ('СНИЛС', snils),
    ('ФИО', full_name),
    ('Дата рождения', birdthay),
    ('Логин', login),
    ('E-mail', mail),
    ('Телефон', phone),
    ('GUID', guid),
    ('UUID', uuid),
    ('ЕНП ОМС', oms),
    ('ОКПО', okpo),
    ('ОКПО ИП', okpo_individual),
    ("GUID LOWER", guid_lower),
    ("Серия и номер паспорта РФ", passport_number),
])

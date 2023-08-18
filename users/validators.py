from django.utils.translation import gettext_lazy as _


def phone_validator(value):
    if not len(value) == 13:
        raise ValueError(_('Invalid phone number'))
    else:
        return True

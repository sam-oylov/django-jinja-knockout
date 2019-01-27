.. _file_exists(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=file_exists
.. _get_FOO_display(): https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.get_FOO_display
.. _get_choice_str(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=get_choice_str
.. _get_meta(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=get_meta
.. _get_related_field(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=get_related_field
.. _get_related_field_val(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=get_related_field_val
.. _get_users_with_permission(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=get_users_with_permission
.. _get_verbose_name(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=get_verbose_name
.. _model_values(): https://github.com/Dmitri-Sintsov/django-jinja-knockout/search?l=Python&q=model_values

======
Models
======

This module contains the functions / classes to manipulate Django models.

.. highlight:: python

* `get_users_with_permission()`_ - return the queryset of all users who have specified permission string, including
  all three possible sources of such users (user permissions, group permissions and superusers).
* Next functions allow to use parts of queryset functionality on single Django model object instances:

  * `get_related_field_val()`_ / `get_related_field()`_ support quering of related field properties from supplied
    model instance via specified string with double underscore-separated names, just like in Django querysets.
  * `model_values()`_ - get the dict of model fields name / value pairs like queryset ``.values()`` for one model
    instance supplied.

* `get_meta()`_ / `get_verbose_name()`_ - get meta property of Django model field by query string, including related
  (foreign) and reverse-related fields::

    get_verbose_name(profile, 'user__username')
    get_meta(profile, 'verbose_name_plural', 'user__username')

* `get_choice_str()`_ - Similar to Django model built-in magic method `get_FOO_display()`_ but does not require to have
  an instance of particular Django model object. For example::

    class Member(models.Model):

        # ... skipped ...
        role = models.IntegerField(choices=ROLES, default=ROLE_MEMBER, verbose_name='Member role')

    from .models import Member
    from django_jinja_knockout.models import get_choice_str

    # ... skipped ...
    role_str = sdv.get_choice_str(Member.ROLES, role_val)

* `file_exists()`_ - checks whether Diango file field object exists in the related filesystem.
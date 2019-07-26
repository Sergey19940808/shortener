import pytest

from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    """Avoid creating/setting up the test database"""
    pass


@pytest.fixture
def db_access_without_rollback_and_truncate(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)
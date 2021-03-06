# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing
import re
from setuptools import setup, find_packages


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = 'entity_event_slack/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='django-entity-event-slack',
    version=get_version(),
    description='A pushable slack medium for the Django Entity Event system',
    long_description=open('README.rst').read(),
    url='https://github.com/ambitioninc/django-entity-event-slack',
    author='Wes Kendall',
    author_email='opensource@ambition.com',
    keywords='django-entity-event, slack',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
    ],
    license='MIT',
    install_requires=[
        'celery>=3.1',
        'Django>=1.7',
        'django-db-mutex>=0.2.2',
        'django-entity-event>=0.4.2',
        'django-manager-utils>=0.8.2',
        'pyslack>=0.1.3',
        'requests',
    ],
    tests_require=[
        'psycopg2',
        'django-nose>=1.4',
        'django-dynamic-fixture',
        'freezegun',
        'mock==1.0.1',
        'coverage>=3.7.1',
    ],
    test_suite='run_tests.run_tests',
    include_package_data=True,
    zip_safe=False,
)

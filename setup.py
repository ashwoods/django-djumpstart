from setuptools import setup, find_packages
import os
#from djumpstart import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.txt'))
try:
    LONG_DESCRIPTION = f.read()
finally:
    f.close()

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'django_djumpstart', 'templates')
STARTPROJECT_DATA = []
for path, dirs, filenames in os.walk(DATA_DIR):
   # Ignore directories that start with '.'
    for i, dir in enumerate(dirs):
        if dir.startswith('.'):
            del dirs[i]
    path = path[len(DATA_DIR) + 1:]
    STARTPROJECT_DATA.append(os.path.join('templates', path, '*.*'))
    # Get files starting with '.' too (they are excluded from the *.* glob).
    STARTPROJECT_DATA.append(os.path.join('templates', path, '.*'))

# using setuptools_git plugin and 


setup(name='django-djumpstart',
      version='0.1a',
      author='Ashley Camba & Lincoln Loop',
      author_email='stuff4ash@gmail.com',
      description=('Create a Django project/app layout'),
      long_description=LONG_DESCRIPTION,
      #ackages=['djumpstart'],
      packages = find_packages(),
      package_data={'django_djumpstart': STARTPROJECT_DATA},
#      include_package_data = True,
      scripts=['bin/djumpstart.py'],
      setup_requires = ["setuptools_git >= 0.3",],
      install_requires=['jinja2',],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'])

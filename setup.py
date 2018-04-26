from setuptools import setup

setup(name='py2ifttt',
      version='1.0.0',
      description='an interface for triggering ifttt webhooks',
      long_description='an interface for triggering ifttt webhooks, http://github.com/moevis/py2ifttt',
      url='http://github.com/moevis/py2ifttt',
      author='moevis',
      author_email='moevery@gmail.com',
      license='MIT',
      packages=['py2ifttt'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
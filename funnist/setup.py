from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()



setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
         long_description='Really, the funniest around.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://example',
      author='Flying circus',
      author_email='email@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
        'markdown',
      ],
      test_suite='nose2.collector',
      tests_require=['nose2'],
      dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
      include_package_data=True,
      scripts=['bin/funniest-joke'],
      zip_safe=False)

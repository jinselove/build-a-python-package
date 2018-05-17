from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://example',
      author='Flying circus',
      author_email='email@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
        'markdown',
      ],
      dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
      zip_safe=False)

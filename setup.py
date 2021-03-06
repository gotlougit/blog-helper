from distutils.core import setup

setup(name='blog-helper',
      version='1.1',
      description='Small blog maintenance helper',
      long_description='Small program to add templates and add blogpost entry to main webpage with easy customization settings.',
      author='Saksham Mittal',
      author_email='gotlouemail@gmail.com',
      url='https://github.com/gotlougit/blog-helper',
      scripts=['src/main.py', 'src/config.py', 'src/polish.py'],
      entry_points = {
        'console_scripts': [
            'blog-helper = src.main:start'
            ]
          }
     )

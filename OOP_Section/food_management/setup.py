from setuptools import setup, find_packages

with open('README.md', "r") as f:
    readme = f.read()


setup(
    name='food_management',
    version='0.1.0',
    author='Teghfo',
    author_email='teghfo@gmail.com',
    description='A Customized food management framework',
    long_description_content_type='text/markdown',
    long_description=readme,
    url='https://github.com/teghfo/food_management',
    keywords=['food-management', 'pure-python'],
    install_requires=[
        'numpy>=1.15.0'
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)

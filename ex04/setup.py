import setuptools

setuptools.setup(
    name='my_minipack',
    version='1.0.0',
    author='arlaine',
    license='',
    description='My minipack',
    author_email='arlaine@student.42.fr',
    packages=['progressbar', 'logger'],
    install_requires=['setuptools', 'wheel'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Students/Developers',
        'Topic :: Testing/Education',
        'License ::',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
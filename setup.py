from setuptools import setup, find_packages


setup(
    name='choose',
    version='0.1',
    description='Choices on steroids',
    long_description=open('README.md').read(),
    url='http://github.com/krotkiewicz/choose',
    author='Konrad Rotkiewicz',
    author_email='konrad.rotkiewicz@gmail.com',
    install_requires=[
        'six>=1.10.0',
    ],
    license='BSD',
    packages=find_packages(),
    test_suite="tests",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

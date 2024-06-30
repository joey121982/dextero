from setuptools import setup, find_packages
setup(
    name='dextero',
    version='0.1.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joey121982/dextero',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dextero=dextero.main:main',
        ]
    },
    python_requires='>=3.10',
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
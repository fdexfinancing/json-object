from setuptools import setup, find_packages

setup(
    name='jsonobject',
    version='0.0.1',
    url='',
    download_url='tarball/0.0.1',
    author='F(x)',
    author_email='ti@fdex.com.br',
    description='F(x) Json Object Package',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    install_requires=[]
)
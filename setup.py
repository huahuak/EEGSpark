from setuptools import setup, find_packages  


setup(
    name='EEGSpark',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 'pyspark=={site.SPARK_VERSION}'
    ]
)
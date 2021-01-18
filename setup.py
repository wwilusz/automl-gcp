from setuptools import setup

# after https://github.com/googleapis/python-automl/blob/master/setup.py
dependencies = [
    "google-api-core[grpc] >= 1.22.0, < 2.0.0dev",
    "proto-plus >= 1.10.0",
    "libcst >= 0.2.5",
]
extras = {
    "pandas": ["pandas>=0.17.1"],
    "storage": ["google-cloud-storage >= 1.18.0, < 2.0.0dev"],
}

setup(
    name='automl-gcp',
    version='',
    packages=['automl_gcp'],
    url='',
    license="Apache 2.0",
    author='',
    author_email='',
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.6",
    description='(Part of) Python Client for Cloud AutoML API adjusted to taste'
)

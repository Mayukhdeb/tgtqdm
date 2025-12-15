import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

"""
release checklist:
0. cleanup `rm -rf mosaic_dataset.egg-info build dist/`
1. update version on `setup.py`
4. commit changes and push
5. make release on PyPI. Run the following commands:
    5.1 `python3 setup.py sdist bdist_wheel`
    5.2 (optional) `python3 -m pip install --user --upgrade twine`
    5.3 `python3 -m twine upload dist/*`
6. git tag the release: `git tag vX.Y.Z` and `git push origin vX.Y.Z`
"""

setuptools.setup(
    name="tgtqdm",
    version="0.0.0",
    description="watch your scripts go brr on telegram",
    author="a very bored mayukh on a sunday night",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mayukhdeb/tgtqdm",
    packages=setuptools.find_packages(),
    install_requires=None,
    classifiers=[
        "Operating System :: OS Independent",
    ],
)
# Example pybind11 A+B Package
[![Python package](https://github.com/dmpyatin/setuptools_test/actions/workflows/workflow.yml/badge.svg)](https://github.com/dmpyatin/setuptools_test/actions/workflows/workflow.yml)

This is a simple example package for publishing pybind11 package on PyPl with setuptools. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/) to write your content.

Links:
Create distribution with setuptools and manualy publish in PyPI:
https://test.pypi.org/project/setuptools-test-dmpyatin/
https://packaging.python.org/tutorials/packaging-projects/

Create CI\CD workflow with github actions and auto publish in PyPI: 
https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
https://docs.github.com/en/actions/guides/building-and-testing-python
https://github.com/pypa/gh-action-pypi-publish

Pybind11 publish example:
https://github.com/pybind/python_example

Usage:
```python
import pybind11_test_dmpytain as ptd
print(ptd.add(1,2))
```
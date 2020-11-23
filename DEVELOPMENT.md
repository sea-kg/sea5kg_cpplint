## 

## Pylint


```
$ python3 -m pylint --rcfile=.pylintrc sea5kg_cpplint/*.py
$ python3 -m pylint --rcfile=.pylintrc tests/*.py
```

## Tests

```
$ cd tests
$ python3 -m pytest -rAs .
```

## Install/Uninstall from localdev dir

```
$ python3 setup.py sdist bdist_wheel
$ python3 -m pip install .
```

```
$ pip3 uninstall sea5kg-cpplint
```
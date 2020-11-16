# sea5kg_cpplint

[![Build Status](https://api.travis-ci.com/sea-kg/sea5kg_cpplint.svg?branch=master)](https://travis-ci.com/sea-kg/sea5kg_cpplint) [![Total alerts](https://img.shields.io/lgtm/alerts/g/sea-kg/sea5kg_cpplint.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sea-kg/sea5kg_cpplint/alerts/) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/sea-kg/sea5kg_cpplint.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/sea-kg/sea5kg_cpplint/context:python)

Nice configurable cpplint (c++ source code lint) on Python


How to install:
```
pip3 install sea5kg_cpplint
```

How to run:

```
python3 -m sea5kg_cpplint
```

## file with config for cpplint

example of `sea5kg_cpplint.config`:
```
# comment
line_length_limit = 80
check_copyright_in_files = yes
skip_files = src\.wsjcpp/.*
skip_files = tmp/.*
```

### config parameters

#### line_length_limit

integer, how long line allows

#### check_copyright_in_files

bool, check in files copyright comment 

#### skip_files

regexp, what files must be to skip
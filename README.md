# Difference Generator

"Difference Generator" is an educational project within the Python Development course
at [Hexlet.io](https://ru.hexlet.io). The project allows comparing files with the extensions `.json` and `.yaml` using
the `gendiff` utility. The comparison result can be output in plain or JSON format. The package can be installed as a
dependency and used in your code. The library provides the `gendiff` module with the `generate_diff()` function, which
returns a string with the difference between the contents of the two files.

[![Actions Status](https://github.com/ESergievich/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ESergievich/python-project-50/actions)
[![Actions Status](https://github.com/ESergievich/python-project-50/actions/workflows/pyci.yaml/badge.svg)](https://github.com/ESergievich/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/2b62cb75ca0b350a0273/maintainability)](https://codeclimate.com/github/ESergievich/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2b62cb75ca0b350a0273/test_coverage)](https://codeclimate.com/github/ESergievich/python-project-50/test_coverage)

## Dependencies
List of dependencies, without which the project code will not work correctly:

- python = "^3.10"
- pyyaml = "^6.0.1"

## Installation

Run the following commands in the shell:

```commandline
# To begin working with the package, it's necessary to replicate the repository on your local machine.
# This is accomplished by utilizing the git clone command. Execute this command in the terminal to clone the project:
>> git clone [[repository URL]](https://github.com/ESergievich/python-project-50.git)

# The next step is to navigate to the directory and proceed with the package installation.
>> cd python-project-50
>> make build
>> make package-install
```

### Help command
```
gendiff -h

usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output
```

## Usage

After the installation is complete, you can use the command:  
`gendiff --format <path/to/file1> <path/to/file2>`  
There are three variations of the `--format` option:

file1.json:  ``{ "host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": false }``  
file2.json:  ``{ "timeout": 20, "verbose": true, "host": "hexlet.io" }``

- `stylish` (set by default)  

`gendiff <path/to/file1.json> <path/to/file2.json>`   
```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

- `plain`

`gendiff -f plain <path/to/file1.json> <path/to/file2.json>`   
```
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

- `json` (allows other programs to use the output for their work)

`gendiff -f json <path/to/file1.json> <path/to/file2.json>`  
```
{"follow": {"key": "follow", "operation": "removed", "value": false}, "host": {"key": "host", "operation": "unchanged", "value": "hexlet.io"}, "proxy": {"key": "proxy", "operation": "removed", "value": "123.234.53.22"}, "timeout": {"key": "timeout", "operation": 
"changed", "old": 50, "new": 20}, "verbose": {"key": "verbose", "operation": "added", "value": true}}
```
These examples demonstrate different methods to compare the contents of two test files.

[![asciicast](https://asciinema.org/a/gUqCosNdUZpfiPCEe0XC9cidv.svg)](https://asciinema.org/a/gUqCosNdUZpfiPCEe0XC9cidv)

[![asciicast](https://asciinema.org/a/0aZs2qJM44Ah2YPK79Rl09abx.svg)](https://asciinema.org/a/0aZs2qJM44Ah2YPK79Rl09abx)

[![asciicast](https://asciinema.org/a/stI5skN7E1GL9TMeMaaZu047v.svg)](https://asciinema.org/a/stI5skN7E1GL9TMeMaaZu047v)

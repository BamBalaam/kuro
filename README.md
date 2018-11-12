# Kuro

Run [Black](https://github.com/ambv/black) (Python code formatter) only on Git unstaged/untracked files

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Requirements

* Python 3.6 (f-strings!)
* [Click](https://github.com/pallets/click)
* [Black](https://github.com/ambv/black)

## Usage

```
Usage: kuro [OPTIONS]

Options:
  --diff             Create a diff of the changes, in a 'kuro.diff' file. If
                     you approve the changes, run kuro with --apply_diff.
  --apply_diff       Consume (and delete) an existing 'kuro.diff' file.
  --project_options  Setup options for Kuro/Black on a directory level.
  --help             Show this message and exit.

```

If you so desire, you can set a different Kuro/Black configuration on a global level by exporting an environment variable called `KURO_BLACK_OPTIONS`.

Kuro will prioritize using project options over using global options.

If no global or local options are set, Kuro will just run Black normally.

## TODO List

* Validation of Black settings saved on `.kuro_config` file
* Fix applying patch file (slightly broken at the moment)

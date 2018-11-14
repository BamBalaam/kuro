# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
- Verification of if kuro command is executed in a git repository.
- Check to see if there are no files to change at all.

### Fixed
- Ignore python files included in .gitignore.

## 0.0.3 - 2018-11-13 (First publicly released version)
### Added
- Core project and bare minimum functionalities
    + Use [Black](https://github.com/ambv/black) on Python files only
    + Only files references by git-ls command
    + Capability to export a diff file of the changes Black outputs
    + Capability 

[Unreleased]: https://github.com/BamBalaam/kuro/compare/0.0.3...master

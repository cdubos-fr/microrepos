# TOPWING

TOPWING (for "**T**eam **O**rganization of **P**rojects **W**ith **I**nterface a**N**d **G**it) is a [`typer`](https://typer.tiangolo.com/) command line interface
tool to help team with multiple git repositories to manage there work.

# CONTRIBUTING

- Respect the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Branch name should be `<type>/<description>`
- Allowed type are:
  * `ci`: ci/cd modification
  * `refactor`: code restructuration
  * `feat`: breaking change or new feature add
  * `fix`: minor bugfix
  * `test`: modification concerning test
  * `docs`: documentation
- [pre-commit](https://pre-commit.com/) is used in pre-integration
- following tools are used:
  * [flake8](https://flake8.pycqa.org/en/latest/): Linting
  * [autopep8](https://pypi.org/project/autopep8/): formatter for [PEP](https://peps.python.org/)
  * [bandit](https://bandit.readthedocs.io/en/latest/): Static security analysis
  * [mypy](https://mypy.readthedocs.io/en/stable/): type annotation verification
  * [xenon](https://pypi.org/project/xenon/): Cyclomatic complexity
  * [tox](https://tox.wiki/en/latest/): centralized workflows
  * [pytest](https://docs.pytest.org/en/7.2.x/): testing

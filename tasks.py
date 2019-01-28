from invoke import task

main_file = "main.py"
config_file = "config.py"
files = f"{main_file} {config_file}"
test_file = "test.py"
all_files = f"{files} {test_file}"


@task
def run(c):
    """ Runs main app """
    c.run(f"python3 {main_file}")


@task
def full(c):
    """ Runs full battery of tests """
    test(c)
    cov(c)
    style(c)


@task
def test(c):
    """ Runs all unit and integration tests """
    c.run("green3 .")


@task
def cov(c):
    """ Checks code coverage """
    c.run(f"coverage run -m py.test {test_file}")
    c.run(f"coverage report -m {files}")
    c.run(f"coverage html {files}")


@task
def html(c):
    """ Opens code coverage html """
    c.run("python -m webbrowser -t \"htmlcov/index.html\"")


@task
def style(c):
    """ Checks for PEP8 mistakes """
    c.run(f"pycodestyle {all_files} tasks.py --ignore=E402,W504")


@task
def doc(c):
    """ Checks for Documentation mistakes """
    c.run(f"pydocstyle {all_files}")


@task
def install(c):
    """ Install all required packages """
    c.run("pip install -r requirements.txt")


@task(pre=[test, style])
def travis(c):
    c.run(f"coverage run -m py.test {test_file}")

import subprocess


def app():
    subprocess.run(["python", "./src/mock_data/main.py"])


def test():
    subprocess.run(["pytest"])


def lint():
    subprocess.run(["ruff", "check", "."])
    subprocess.run(["black", "."])


def scan():
    subprocess.run(["safety", "check", "-r", "requirements.txt", "--full-report"])
    subprocess.run(["bandit", "-c", "pyproject.toml", "-r", "."])

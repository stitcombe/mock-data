import subprocess

def app():
    subprocess.run(
        ['python', './src/mock_data/main.py']
    )

def test():
    subprocess.run(
        ['pytest']
    )
    subprocess.run(
        ['coverage']
    )

def lint():
    subprocess.run(
        ['ruff', 'check', './src']
    )
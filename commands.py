import subprocess
import os


def run_npm_start():
    subprocess.run("npm start", shell=True)


def git_status():
    subprocess.run("git status", shell=True)


def git_add_all():
    subprocess.run("git add .", shell=True)


def git_push():
    subprocess.run("git push", shell=True)


def open_vscode():
    os.system("code .")
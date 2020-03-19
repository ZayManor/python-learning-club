# Instructions for Installing Python Club Learning (PCL) Tools

## Computer/Laptop
I'm biased and prefer Macs, but any computer or laptop will work. If you don't have a Mac, hit me up because the following instructions are Macbook specific.

## Terminal
The terminal is an interface that allows you to execute commands. This is a very powerful tool, one that we'll be using
early on. A basic understanding of the terminal is a great skill to have and will get you far.

## PyEnv
PyEnv is a great tool for managing Python versions. Installing this will make it easier to update and change versions as we go. To download, follow the directions below:

1. In your terminal, type the following command: `curl https://pyenv.run | bash`
2. In the same terminal, open up your bash file: `vim ~/.bashrc`
3. Press `i` (insert mode) to write in the file
4. Paste in the following (note: `your_user_name` should be your user name):
    ```
    export PATH="/Users/your_user_name/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```
5. Hit `esc` on your keyboard
6. Type `:x` to Save and Exit the file
7. In the terminal, type `source ~/.bashrc` to to "reset" your shell session
8. To verify PyEnv installed successfully, type `pyenv` in your terminal

## Python 3.7.0 or higher
Remember, PyEnv? We'll use this to install Python version 3.7.0. Python 3.7.0 has the latest libraries installed (we'll get into that later) which will be useful for us in later lessons:

1. Install Python version 3.7.0: `pyenv install 3.7.0` (this may take a moment or 2)
2. Set your global system to this python version: `pyenv global 3.7.0`
3. Confirm you're using this python version: `pyenv global` (outcome: `3.7.0`)

    **Update pip**
    Python comes with a package manager called `pip`. Update this to the latest version:

    1. `pip install -U pip` (should install pip version 20.0.2)

## iPython
iPython is an interactive command shell for Python that creates an environment to execute Python code quickly. We'll use `pip` to install this:

1. `pip install ipython`
2. Confirm iPython successfully installed: `ipython` (you should now be entered in the iPython terminal where we'll do most of our introductory items)
3. To exit the iPython terminal type: `exit()`

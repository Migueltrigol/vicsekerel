from setuptools import setup

setup(
      name='vicsekerel',
      version='1.0.0',
      description='Implemetation of the Vicsek model in Python. It allows users to edit the parameters of the original model and to generate a video of the resulting simulation.',
      author='Miguel Trigo',
      author_email='migueltrigol@gmail.com',
      packages=['vicsekerel'],
      zip_safe=False,
      install_requires=[
        "asttokens==2.2.1",
        "backcall==0.2.0",
        "colorama==0.4.6",
        "contourpy==1.0.7",
        "cycler==0.11.0",
        "decorator==5.1.1",
        "executing==1.2.0",
        "fonttools==4.38.0",
        "ipython==8.9.0",
        "jedi==0.18.2",
        "kiwisolver==1.4.4",
        "matplotlib==3.6.3",
        "matplotlib-inline==0.1.6",
        "numpy==1.24.1",
        "packaging==23.0",
        "parso==0.8.3",
        "pickleshare==0.7.5",
        "Pillow==9.4.0",
        "prompt-toolkit==3.0.36",
        "pure-eval==0.2.2",
        "Pygments==2.14.0",
        "pyparsing==3.0.9",
        "python-dateutil==2.8.2",
        "six==1.16.0",
        "stack-data==0.6.2",
        "traitlets==5.9.0",
        "wcwidth==0.2.6",
        ],
      )
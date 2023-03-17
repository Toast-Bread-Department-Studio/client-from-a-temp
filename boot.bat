@echo off
    set TRANSFORMERS_CACHE=.cache\huggingface\transformers
    set XDG_CACHE_HOME=.cache
    set MATPLOTLIBRC=.cache

    set GIT=git\bin\git.exe
    set GIT_PYTHON_GIT_EXECUTABLE=git\bin\git.exe
    set PYTHON=py310\python.exe
    set COMMANDLINE_ARGS=--xformers --api 

    %PYTHON% launch.py
    pause
    exit /b
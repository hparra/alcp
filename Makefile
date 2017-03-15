.PHONY: test test-watch ipython

#
# Python
#

test:
	python -m unittest discover -p "test_*.py"

test-watch:
	ls */**.py | entr python -m unittest discover -p "test_*.py"

ipython:
	PYTHONSTARTUP="app/startup.py" ipython

.PHONY: test test-watch ipython

#
# Python
#

test:
	python -m unittest discover -p "test_*.py"

watch:
	ls */**.py | entr python -m unittest discover -p "test_*.py"

random:
	python src/randoms.py

ipython:
	PYTHONSTARTUP="app/startup.py" ipython

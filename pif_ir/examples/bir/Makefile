# Simple make file for AIR target
ROOT_DIR=../../..

OFTEST_PATH=${ROOT_DIR}/submodules/oftest
OFTEST_PYTHON=${OFTEST_PATH}/src/python
PYPATH=PYTHONPATH=${ROOT_DIR}/:${OFTEST_PYTHON}

sample: submodule
	sudo ${PYPATH} ./start.py bir_sample.yml

%.yml: submodule
	sudo ${PYPATH} ./start.py $@

submodule:
	git submodule update --init

.PHONY: submodule start


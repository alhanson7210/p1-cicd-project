#[var]
UNITS = test_user_model.py test_database_model.py
FLAGS = -v
MODULE = unittest
TDD_SRC = tdd_tests
BDD_SRC = bdd_tests
#[cmd]
setup:
	pip3 install pytest-bdd
	pip3 install requests
#[cmd]
tdd:
	echo "running tdd"
	cd $(TDD_SRC)
	python3 -m $(MODULE) $(FLAGS) $(UNITS)
	cd ..
#[cmd]
bdd:
	echo "running bdd"
	cd $(BDD_SRC)
	pytest
	cd ..

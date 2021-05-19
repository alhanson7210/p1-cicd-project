#[var]
TESTPATH = src/tests
TDD_SRC = tdd_tests
BDD_SRC = bdd_tests
UNITS = $(TESTPATH)/$(TDD_SRC)/test_user_model.py $(TESTPATH)/$(TDD_SRC)/test_database_model.py
FLAGS = -v
MODULE = unittest
#[cmd]
tdd:
	python3 -m $(MODULE) $(FLAGS) $(UNITS)
#[cmd]
bdd:
	echo "running bdd"
	#cd $(BDD_SRC) && \
	pytest
	#cd ..

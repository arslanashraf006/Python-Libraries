import mydb
import pytest
# code repeatation and more database connect cause issues
# two ways to fix those issues
# setup and teardown methods (classic xunit style)
# fixtures (recommended)

# both this method initialize the data in the beginning

#fixtures
# to show print in cmd
# pytest -v --capture=no

#passing scope module run the setup once
@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db = mydb.MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("closing database")

#setup and tear down
# conn = None
# cur = None
# def setup_module(module):
#     global conn
#     global cur
#     db = mydb.MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
# after test cases finish the execution you want some clean up so you use teardown
# def teardown_module(module):
#     cur.close()
#     conn.close()

def test_john_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789

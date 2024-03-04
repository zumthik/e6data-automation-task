from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import Login
from pageObjects.WorkSpace import Workspace
from pageObjects.QueryPage import Query


class TestQuery(BaseClass):

    def test_query_of_7_days(self, login):
        try:
            # login = Login(self.driver)
            # login.login_using_valid_cre()

            workspace = Workspace(self.driver)
            workspace.workspace_details()

            query = Query(self.driver)
            query.get_query_page()
            query.apply_filter_from_picker()
            query.get_query_history_table()

        except Exception as e:
            print(e)
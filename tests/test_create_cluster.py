
from utilities.BaseClass import BaseClass

from pageObjects.LoginPage import Login
from pageObjects.WorkSpace import Workspace
from pageObjects.ClusterPage import Cluster


class TestCreateCluster(BaseClass):

	def test_option_in_left_navigation(self):
		login = Login(self.driver)
		login.login_using_valid_cre()

		workspace = Workspace(self.driver)
		workspace.workspace_details()

		cluster = Cluster(self.driver)
		cluster.get_cluster_page()
		cluster.get_title()
		assert (cluster.get_title(), "Clusters")
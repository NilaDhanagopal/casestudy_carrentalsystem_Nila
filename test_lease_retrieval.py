import unittest

from dao.ICarLeaseRepositoryImpl import CarLeaseRepositoryImpl


class TestLeaseRetrieval(unittest.TestCase):

    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()  # Assuming the repository instance
        self.leaseID = 1  # Example lease ID

    def test_find_lease_by_id(self):
        lease = self.repo.findLeaseById(self.leaseID)

        # Verify lease was retrieved
        self.assertIsNotNone(lease)
        self.assertEqual(lease.get_leaseID(), self.leaseID)

if __name__ == '__main__':
    unittest.main()

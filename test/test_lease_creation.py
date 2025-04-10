import unittest

from dao.ICarLeaseRepositoryImpl import CarLeaseRepositoryImpl


class TestLeaseCreation(unittest.TestCase):

    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()  # Assuming the repository instance
        self.customerID = 1  # Example customer ID
        self.vehicleID = 1  # Example vehicle ID
        self.startDate = "2025-04-01"
        self.endDate = "2025-04-10"

    def test_create_lease(self):
        lease = self.repo.createLease(self.customerID, self.vehicleID, self.startDate, self.endDate)

        # Verify lease is created
        self.assertIsNotNone(lease)  # Lease object should not be None
        self.assertEqual(lease.get_customerID(), self.customerID)
        self.assertEqual(lease.get_vehicleID(), self.vehicleID)
        self.assertEqual(lease.get_startDate(), self.startDate)
        self.assertEqual(lease.get_endDate(), self.endDate)

if __name__ == '__main__':
    unittest.main()

import unittest
from dao.ICarLeaseRepositoryImpl import CarLeaseRepositoryImpl

from exceptions.CustomerNotFoundException import CustomerNotFoundException
from exceptions.CarNotFoundException import CarNotFoundException
from exceptions.LeaseNotFoundException import LeaseNotFoundException


class TestExceptions(unittest.TestCase):

    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()  # Assuming repository instance

    def test_car_not_found_exception(self):
        print("Running test for CarNotFoundException...")
        try:
            self.repo.findCarById(999)  # A non-existent car ID
        except CarNotFoundException as e:
            print(f"Caught exception: {e}")
            self.assertTrue(isinstance(e, CarNotFoundException))

    # A non-existent car ID


    def test_lease_not_found_exception(self):
        # Using assertRaises as a context manager
        with self.assertRaises(LeaseNotFoundException):
            self.repo.findLeaseById(999)  # Assume 999 is a non-existent lease ID

    def test_customer_not_found_exception(self):
        # Using assertRaises as a context manager
        with self.assertRaises(CustomerNotFoundException):
            self.repo.findCustomerById(999)  # Assume 999 is a non-existent customer ID

    def test_car_not_found_exception(self):
        print("Running test for CarNotFoundException...")
        with self.assertRaises(CarNotFoundException):
            self.repo.findCarById(999)  # Assume 999 is a non-existent car ID


if __name__ == '__main__':
    unittest.main()

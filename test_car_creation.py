import unittest
from dao.ICarLeaseRepositoryImpl import CarLeaseRepositoryImpl
from entity.vehicle import Vehicle

class TestCarCreation(unittest.TestCase):
    def setUp(self):
        self.repo = CarLeaseRepositoryImpl()
        self.car = Vehicle(make="Toyota", model="Corolla", year=2023, dailyRate=50.0,
                           status="available", passengerCapacity=5, engineCapacity=2.0)

    def test_add_car(self):
        self.repo.addCar(self.car)
        car_from_db = self.repo.findCarById(self.car.get_vehicleID())
        self.assertEqual(car_from_db.get_make(), self.car.get_make())
        self.assertEqual(car_from_db.get_model(), self.car.get_model())
        self.assertEqual(car_from_db.get_year(), self.car.get_year())
        self.assertEqual(car_from_db.get_dailyRate(), self.car.get_dailyRate())
        self.assertEqual(car_from_db.get_status(), self.car.get_status())
        self.assertEqual(car_from_db.get_passengerCapacity(), self.car.get_passengerCapacity())
        self.assertEqual(car_from_db.get_engineCapacity(), self.car.get_engineCapacity())

if __name__ == '__main__':
    unittest.main()

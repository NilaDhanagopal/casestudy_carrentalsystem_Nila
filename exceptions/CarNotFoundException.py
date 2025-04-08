class CarNotFoundException(Exception):
    def __init__(self, message="Car with the given ID not found."):
        self.message = message
        super().__init__(self.message)

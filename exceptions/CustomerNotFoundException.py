class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer with the given ID not found."):
        self.message = message
        super().__init__(self.message)

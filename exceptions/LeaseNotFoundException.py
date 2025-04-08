class LeaseNotFoundException(Exception):
    def __init__(self, message="Lease with the given ID not found."):
        self.message = message
        super().__init__(self.message)

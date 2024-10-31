class Branch:
    def __init__(self, name, bank, ifsc_code, address):
        self.name = name
        self.bank = bank
        self.ifsc_code = ifsc_code
        self.address = address
        self.accounts = {}
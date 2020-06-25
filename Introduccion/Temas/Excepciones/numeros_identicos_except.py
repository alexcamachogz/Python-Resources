class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        # message es propio de Exception
        self.message = mensaje
class Lector:
    """
    This Lector reads several times from stdout.
    It's saves how many bytes has readed and ignores
    this first bytes when returning what it has read

    In other words it always return something it hasn't 
    readed before
    """
    readed = 0

    def read(self, stdout):
        first_read = stdout.getvalue()
        last_part = first_read[self.readed:]
        self.readed = len(first_read)
        return last_part


reader = Lector()

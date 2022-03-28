class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if not filename:
            raise ValueError("must specify a file to read")
        if not isinstance(skip_top, int) or skip_top < 0:
            raise ValueError("skip_top must be a positive integer")
        if not isinstance(skip_bottom, int) or skip_bottom < 0:
            raise ValueError("skip_bottom must be a positive integer")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_obj = None
        self.full_data = []

    def __enter__(self):
        try:
            self.file_obj = open(self.filename, mode="r", encoding="utf-8")
        except FileNotFoundError:
            self.file_obj = None
            return None
        for line in self.file_obj:
            self.full_data.append(list(map(str.strip, line.split(self.sep))))
        base_length = None
        for i, elem in enumerate(self.full_data):
            if i == 0:
                base_length = len(elem)
            elem = [e for e in elem if e]
            if i != 0 and len(elem) != base_length:
                return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.full_data = []
        if self.file_obj:
            self.file_obj.close()

    def getdata(self):
        start = self.skip_top
        end = len(self.full_data) - self.skip_bottom
        if self.header:
            return self.full_data[start + 1: end]
        else:
            return self.full_data[start: end]

    def getheader(self):
        if self.header:
            return self.full_data[0]
        else:
            return None

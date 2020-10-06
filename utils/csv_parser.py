import io


class CsvBytesParser:
    # @TODO - create parser with generator without caching all bytes/lines in memory to handle very large files

    def __init__(self, bytes):
        """
        :param bytes:gets bytes data from http request and converts it to lines
        """
        self.lines = io.StringIO(bytes.decode())

    def parse_line(self, line):
        """
        clean line from csv
        :param line: string
        :return: list of attributes in line
        """
        return line.strip('\r\n').split(",")

    def get_next_line(self):
        """
        generator that yields one line every time from file
        :return: list of line items
        """
        # patch to skip first few lines
        num_of_lines_to_ignore = 4
        for line in self.lines:
            if num_of_lines_to_ignore:
                num_of_lines_to_ignore -= 1
                continue
            if line == "\r\n":  # ignore empy lines as well
                continue
            items = self.parse_line(line)
            yield items

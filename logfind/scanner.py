class Scanner(object):
    def __init__(self, flag=None):
        self.flag = flag

    def scan(self, s, k):
        if self.flag == '-o':
            return self.scan_with_or(s, k)
        else:
            return self.scan_with_and(s, k)

    def scan_with_and(self, s, k):
        """returns True if all words in k are in s. False otherwise."""
        k = k.split()
        for word in k:
            if word not in s:
                return False
        return True

    def scan_with_or(self, s, k):
        """returns True if any word in k is in s. False otherwise."""
        k = k.split()
        for word in k:
            if word in s:
                return True
        return False

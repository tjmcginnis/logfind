import re


class Scanner(object):
    def __init__(self, flag=None):
        self.or_flag = flag

    def scan(self, s, k):
        reg = []
        for word in k.split(' '):
            reg.append(re.compile(word))
        if self.or_flag is True:
            return self.scan_with_or(s, reg)
        else:
            return self.scan_with_and(s, reg)

    def scan_with_and(self, s, r):
        """returns True if all words in k are in s. False otherwise."""
        for regexp in r:
            if re.search(regexp, s) is None:
                return False
            # if word not in s:
            #     return False
        return True

    def scan_with_or(self, s, r):
        """returns True if any word in k is in s. False otherwise."""
        for regexp in r:
            if re.search(regexp, s) is not None:
                return True
            # if word in s:
            #     return True
        return False

"""Custom Feed Exports extension."""
import os
import shutil
from tempfile import NamedTemporaryFile

from scrapy.extensions.feedexport import FileFeedStorage


class CustomFileFeedStorage(FileFeedStorage):
    """
    A File Feed Storage extension that overwrites existing files.

    See: https://github.com/scrapy/scrapy/blob/master/scrapy/extensions/feedexport.py#L79
    """

    def open(self, spider):
        """Return the opened file."""
        res = NamedTemporaryFile()
        return res

    def store(self, file):
        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        shutil.move(file.name, self.path)


from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from pdfminer.pdfparser import PDFParser

from pic_core.utils.pic_utils import is_path_valid, byte_to_string
from pic_core.utils.log import getMyLogger
log = getMyLogger(__file__)


class ELPDF(object):
    def __init__(self, pdf_path, password=None, encoding='utf-8', caching=True):
        self._pdfPath = pdf_path
        self._password = password
        self._caching = caching
        self._codec = encoding

        self._totalPageNo = 0
        self._metadata = None
        self._pdfText = None
        self._convert_to_txt()

    @property
    def metadata(self):
        """
         Return the PDF file's metadata (i.e. Author, Producer, Title..etc.)
         :return: A Python dictionary with key:value pair.
         """
        return self._metadata[0]

    @property
    def total_page_number(self):
        return self._totalPageNo

    @property
    def pdf_text(self):
        return self._pdfText

    def _convert_to_txt(self):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=self._codec, laparams=laparams)
        if is_path_valid(self._pdfPath):
            fp = open(self._pdfPath, 'rb')
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            pagenos=set()
            for page in PDFPage.get_pages(fp, pagenos, maxpages=0, password=self._password,caching=self._caching, check_extractable=True):
                self._totalPageNo += 1
                interpreter.process_page(page)

            parser = PDFParser(fp)
            self._metadata = PDFDocument(parser).info
            fp.close()

        self._pdfText = retstr.getvalue()

        device.close()
        retstr.close()


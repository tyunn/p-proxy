import unittest
from run import replace_content


class TestReplaceContent(unittest.TestCase):
    def test_replace_content_body(self):
        content = (
            "<head></head><body><h1>A word with a length of 6 characters</h1></body>"
        )
        result = replace_content(content.encode("utf-8"))
        self.assertEqual(
            result.decode("utf-8"),
            (
                u"<head></head><body><h1>A word with a "
                "length\N{TRADE MARK SIGN} of 6 characters</h1></body>"
            ),
        )

    def test_no_replace_content_header(self):
        content = "<head>header no need to replace</head><body>123</body>"
        result = replace_content(content.encode("utf-8"))
        self.assertEqual(
            result.decode("utf-8"),
            "<head>header no need to replace</head><body>123</body>",
        )

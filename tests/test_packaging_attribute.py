from .utils import is_canonical_version


class TestPackagingAttribute:

    def test_version_respect_pep440(self):
        from topwing import __version__
        assert isinstance(__version__, str)
        assert is_canonical_version(__version__)

    def test_package_description(self):
        from topwing import __doc__
        assert isinstance(__doc__, str)
        assert len(__doc__) > 0

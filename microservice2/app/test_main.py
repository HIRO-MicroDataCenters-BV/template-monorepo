from .main import main


def test_read_main() -> None:
    result = main()
    assert result is True

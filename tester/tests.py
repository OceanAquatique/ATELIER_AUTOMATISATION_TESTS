from tester.client import get

URL = "https://coffee.alexflipnote.dev/random.json"


def test_status_code():
    r = get(URL)
    assert r["status_code"] == 200


def test_content_type():
    r = get(URL)
    assert "application/json" in r["headers"].get("Content-Type", "")


def test_json_valid():
    r = get(URL)
    assert isinstance(r["json"], dict)


def test_file_field():
    r = get(URL)
    assert "file" in r["json"]


def test_file_type():
    r = get(URL)
    assert isinstance(r["json"]["file"], str)


def test_file_url():
    r = get(URL)
    assert r["json"]["file"].startswith("http")

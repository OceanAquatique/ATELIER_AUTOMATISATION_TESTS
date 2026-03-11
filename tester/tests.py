import requests

URL = "https://coffee.alexflipnote.dev/random.json"

def test_status_code():
    response = requests.get(URL)
    assert response.status_code == 200
    print("PASS : status code 200")

def test_content_type():
    response = requests.get(URL)
    content_type = response.headers.get("Content-Type")
    assert "application/json" in content_type
    print("PASS : content-type JSON")

def test_json_valid():
    response = requests.get(URL)
    data = response.json()
    assert isinstance(data, dict)
    print("PASS : JSON valide")

def test_file_field():
    response = requests.get(URL)
    data = response.json()
    assert "file" in data
    print("PASS : champ file présent")

def test_file_type():
    response = requests.get(URL)
    data = response.json()
    assert isinstance(data["file"], str)
    print("PASS : file est une string")

def test_file_url():
    response = requests.get(URL)
    data = response.json()
    assert data["file"].startswith("http")
    print("PASS : file est une URL")

if __name__ == "__main__":
    test_status_code()
    test_content_type()
    test_json_valid()
    test_file_field()
    test_file_type()
    test_file_url()

from fastapi import FastAPI, File, Form
from fastapi.testclient import TestClient

app = FastAPI()


@app.post("/file_before_form")
def file_before_form(
    file: bytes = File(...), city: str = Form(...),
):
    return {"file_content": file, "city": city}


@app.post("/file_after_form")
def file_after_form(
    city: str = Form(...), file: bytes = File(...),
):
    return {"file_content": file, "city": city}


client = TestClient(app)


def test_file_before_form():
    response = client.post(
        "/file_before_form", data={"city": "Thimphou"}, files={"file": "<file content>"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"file_content": "<file content>", "city": "Thimphou"}


def test_file_after_form():
    response = client.post(
        "/file_after_form", data={"city": "Thimphou"}, files={"file": "<file content>"}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"file_content": "<file content>", "city": "Thimphou"}

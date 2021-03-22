import requests
import json


def test_1():
    # get single course details fail
    id = 8000
    r = requests.get("http://127.0.0.1:5000/course" + f"/{id}")
    assert r.status_code == 200


def test_2():
    # get single course details pass
    id = 80
    r = requests.get("http://127.0.0.1:5000/course" + f"/{id}")
    assert r.status_code == 200


def test_3():
    # title words do not exist (fail)
    words = "Tanisha,Manoj"
    r = requests.get("http://127.0.0.1:5000/course" + f"?title-words={words}")
    assert r.status_code == 200


def test_4():
    # title words exist (pass)
    r = requests.get("http://127.0.0.1:5000/course?Django")
    assert r.status_code == 200


def test_5():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_len_imagepath = {
        "image_path": "images/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpg",
        "discount_price": 5,
        "price": 9,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_len_imagepath), headers=headers)

    assert r.status_code == 200


def test_6():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_type_discount = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": "This is wrong",
        "price": 9,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_type_discount), headers=headers)

    assert r.status_code == 200


def test_7():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_type_price = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": "This is wrong",
        "title":"Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_type_price), headers=headers)

    assert r.status_code == 200


def test_8():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_type_title = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": 15,
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_type_title), headers=headers)

    assert r.status_code == 200


def test_9():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_len_title = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course Brand new course Brand new course Brand new course Brand new course Brand new courseBrand new course Brand new courseBrand new course  Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_len_title), headers=headers)

    assert r.status_code == 200


def test_10():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_ondiscount_type = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": "This is wrong",
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_ondiscount_type), headers=headers)

    assert r.status_code == 200


def test_11():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_description_type = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": 15
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_description_type), headers=headers)

    assert r.status_code == 200


def test_12():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    wrong_len_description = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description New description New description New description New description New description New description New description New description New description New description v New description New description New description New description New description New description New description New description "
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(wrong_len_description), headers=headers)

    assert r.status_code == 200

def test_13():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    image_path_missing = {

        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(image_path_missing), headers=headers)

    assert r.status_code == 200


def test_14():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    discount_missing = {
        "image_path": "images/some/path/foo.jpg",
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(discount_missing), headers=headers)

    assert r.status_code == 200

def test_15():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    price_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(price_missing), headers=headers)

    assert r.status_code == 200

def test_16():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    title_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(title_missing), headers=headers)

    assert r.status_code == 200


def test_17():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    ondiscount_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(ondiscount_missing), headers=headers)

    assert r.status_code == 200


def test_18():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    description_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(description_missing), headers=headers)

    assert r.status_code == 200


def test_19():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    correct_data = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description"
    }

    r = requests.post("http://127.0.0.1:5000/course", data=json.dumps(correct_data), headers=headers)

    assert r.status_code == 200



def test_20():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_len_imagepath = {
        "image_path": "images/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpgimages/some/path/foo.jpg",
        "discount_price": 5,
        "price": 9,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_len_imagepath), headers=headers)

    assert r.status_code == 200


def test_21():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_type_discount = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": "This is wrong",
        "price": 9,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_type_discount), headers=headers)

    assert r.status_code == 200


def test_22():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_type_price = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": "This is wrong",
        "title":"Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_type_price), headers=headers)

    assert r.status_code == 200


def test_23():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_type_title = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": 15,
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_type_title), headers=headers)

    assert r.status_code == 200


def test_24():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_len_title = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course Brand new course Brand new course Brand new course Brand new course Brand new courseBrand new course Brand new courseBrand new course  Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_len_title), headers=headers)

    assert r.status_code == 200


def test_25():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_ondiscount_type = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": "This is wrong",
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_ondiscount_type), headers=headers)

    assert r.status_code == 200


def test_26():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_description_type = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": 15,
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_description_type), headers=headers)

    assert r.status_code == 200


def test_27():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_len_description = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description New description New description New description New description New description New description New description New description New description New description v New description New description New description New description New description New description New description New description ",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_len_description), headers=headers)

    assert r.status_code == 200

def test_28():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    image_path_missing = {

        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(image_path_missing), headers=headers)

    assert r.status_code == 200


def test_29():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    discount_missing = {
        "image_path": "images/some/path/foo.jpg",
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(discount_missing), headers=headers)

    assert r.status_code == 200

def test_30():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    price_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(price_missing), headers=headers)

    assert r.status_code == 200

def test_31():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    title_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(title_missing), headers=headers)

    assert r.status_code == 200


def test_32():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    ondiscount_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(ondiscount_missing), headers=headers)

    assert r.status_code == 200


def test_33():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    description_missing = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(description_missing), headers=headers)

    assert r.status_code == 200


def test_34():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    wrong_id_type = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":"this is wrong"
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(wrong_id_type), headers=headers)

    assert r.status_code == 200


def test_35():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    non_matching_id = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":170
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(non_matching_id), headers=headers)

    assert r.status_code == 200

def test_36():
    # post request parameter title type fail
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    id=180
    correct_data = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 15,
        "price": 200,
        "title": "Brand new course",
        "on_discount": False,
        "description": "New description",
        "id":180
    }

    r = requests.put("http://127.0.0.1:5000/course" + f"/{id}", data=json.dumps(correct_data), headers=headers)

    assert r.status_code == 200


def test_37():
    id = 83
    r = requests.delete("http://127.0.0.1:5000/course" + f"/{id}")
    assert r.status_code == 200


def test_38():
    id = 800
    r = requests.delete("http://127.0.0.1:5000/course" + f"/{id}")
    assert r.status_code == 200

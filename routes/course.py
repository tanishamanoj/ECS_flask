"""Routes for the course resource.
"""

from flask import Flask, jsonify, request
from datetime import datetime
import data
from validate import Validation_Put, Validation_Post

d = data.load_data()
app = Flask(__name__)
current_highest_id = 200


@app.route('/course/<int:id>', methods=['GET'])
def get_course(id):
    """Get a course by id.

        :param int id: The record id.
        :return: A single course (see the challenge notes for examples)
        :rtype: object
        """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    if id in d.keys():
        return jsonify({"data": d[id]}),200
    else:
        return jsonify({"message": f"Course {id} does not exist"}),404


@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
        words separated by commas".

        Query parameters: page-number, page-size, title-words
        If not present, we use defaults of page-number=1, page-size=10

        :return: A page of courses (see the challenge notes for examples)
        :rtype: object
        """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE

    # Included sorting for title-words match
    # Highest to lowest in terms of number of matching words
    # For each number of similar words, sorted in ascending order

    pages = request.args.get('page-size', 200)
    pages = int(pages)
    page_number = request.args.get('page-size', 1)
    words = request.args.get('title-words', '')
    words = words.split(',')
    count = [[] for i in range(len(words) + 1)]
    final = []
    for i in (sorted(d)):
        c = 0
        for j in words:
            if j.lower() in d[i]['title'].lower():
                c += 1
        if c != 0:
            count[c].append(d[i])
    for i in range(len(count) - 1, -1, -1):
        final += count[i]
    print(final)
    if final != [] and pages <= current_highest_id:
        if len(final) > pages:

            return jsonify({"data": final[0:pages],
                            "metadata": {"page_count": int(pages / int(page_number)), "page_number": 1,
                                         "page_size": pages, "record_count": len(final)}}),200
        else:
            return jsonify({"data": final, "metadata": {"page_count": int(pages / int(page_number)), "page_number": 1,
                                                        "page_size": pages, "record_count": len(final)}}),200
    else :
        return jsonify({"message": "No courses found"}), 404


@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
        :return: The course object (see the challenge notes for examples)
        :rtype: object
        """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    global current_highest_id
    current_highest_id += 1
    validating = Validation_Post()
    errors = validating.validate(request.get_json())
    if errors:
        message = ''
        for i in errors:
            message += errors[i][0]
        return jsonify(({"message": message})), 404
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    date_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    new_entry = request.get_json()
    new_entry["date_created"] = date_created
    new_entry["date_updated"] = date_updated
    new_entry["id"] = current_highest_id
    d[current_highest_id] = new_entry
    return jsonify({"data": d[current_highest_id]}),200


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
        :param int id: The record id.
        :return: The updated course object (see the challenge notes for examples)
        :rtype: object
        """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE
    validating = Validation_Put()

    errors = validating.validate(request.get_json())
    if errors:
        message = ''
        for i in errors:
            message += errors[i][0]
        return jsonify({"message": message}), 404

    else:
        updated_entry = request.get_json()
        if id != updated_entry["id"]:
            return jsonify({"message": "The id does match the payload"}), 404
        else:
            updated_entry["date_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            updated_entry["date_created"] = d[id]["date_created"]
            d[id]=updated_entry
            return jsonify({"data": d[id]}), 200


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
        :return: A confirmation message (see the challenge notes for examples)
        """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    try:
        del d[id]
    except KeyError:
        return jsonify({"message": f"Course {id} does not exist"}), 404
    return jsonify({"message": "The specified course was deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)

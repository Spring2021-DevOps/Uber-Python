from flask import Flask, request, jsonify, Response
from bson.objectid import ObjectId
import uuid
import DatabaseOperations as database
from flask_cors import CORS
import simplejson as json

app = Flask(__name__)
CORS(app)

@app.route('/book-trip', methods=["POST"])
def bookTrip():
    print("Booking new trip..")
    try:
        firstName = request.json["firstNameP"]
        lastName = request.json["lastNameP"]
        source = request.json["sourceP"]
        destination = request.json["destinationP"]
        journeyDate = request.json["journeydDateP"]

        booking = dict(firstName=firstName, lastName=lastName, source=source,
                    destination=destination, journeyDate=journeyDate,
                    )
        bookingId = database.add_booking(booking)
        print("Booked new trip!")
        data = {
                "message": "Booking Successful",
                "BookingID": bookingId
        }
        statusCode = 200

    except Exception as e:
        print("An exception occurred", e)
        data = {
            "message": "Booking unsuccessful. Please try again later",
            "BookingID": None
        }
        statusCode = 500

    js = json.dumps(data)
    response = Response(js, status=statusCode, mimetype='application/json')
    return response

@app.route('/bookings', methods=["GET"])
def getAllBookings():
    try:
        bookings = database.get_bookings()
        if bookings is None:
            bookings = []
        data = {
                "message": "Booking List",
                "bookings": bookings
        }
        statusCode = 200

    except Exception as e:
        data = {
                "message": "Cannot get booking list at this time. Please try again later",
                "bookings": {}
        }
        statusCode = 500
    js = json.dumps(data)
    response = Response(js, status=statusCode, mimetype='application/json')
    return response
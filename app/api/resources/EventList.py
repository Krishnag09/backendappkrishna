from datetime import date, datetime
from unittest import result
from flask import Flask, jsonify, Response
from flask_restful import Resource, Api, reqparse, inputs
import json
import os
import pytz
TESTDIR = 'test-files'


class Eventlist(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'filename', type=str, help="From Date is missing")
        self.reqparse.add_argument(
            'from', type=inputs.datetime_from_iso8601, help="From Date is missing")
        self.reqparse.add_argument(
            'to', type=inputs.datetime_from_iso8601, help="To Date is missing")

    def post(self):
        try:
            result = []
            args = self.reqparse.parse_args()
            filename = args['filename']
            fromdate = args['from'].replace(tzinfo=None)
            todate = args['to'].replace(tzinfo=None)
            filepath = os.path.join(TESTDIR, filename)
            with open(filepath, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    row = line.split()
                    dateevent = datetime.strptime(
                        row[0], '%Y-%m-%dT%H:%M:%SZ')
                    print(dateevent, fromdate, todate)
                    if (dateevent >= fromdate and dateevent <= todate):
                        resultevent = {"eventTime": row[0],
                                       "email": row[1],
                                       "sessionId": row[2]
                                       }
                        result.append(resultevent)
                sorted_result = sorted(result, key=lambda d: d['eventTime'])
        except Exception as e:
            sorted_result = []
            Response.status_code = 200
        return jsonify(sorted_result)


# /change to json- done
# sort as - done
# /add 200 for erro and resturn empty - done
# add port 8279 - add this as part of docker file.- done
# test for sample files location - done
# .gitignore
# Readme - In this zip file is an empty README.md. Please fill this out describing your project,
# your test methodology, embellishments, and places where you can improve.
# - You should include testing code
# - The solution should handle failure cases
# - Package the final code in a zip file. Please do not include any binaries files in the zip, e.g. libraries, compiled code...
# constant memory


# running the application
# run.sh is used to test the app by running docker and providing the test files
# build.sh is used to trigger the docker build
# make changes to docker files to run the app but keep the app/test

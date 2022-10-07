# Text file Event Parser

Please fill out your readme here.

### The submission includes the following

Create the env:

## Docker container:

    # Use Dockerfile provided to build the image, and run it # explained at https://docs.docker.com/get#started/02_our_app/
    # App will be running at http://127.0.0.1:8279/
    # To run tests use "python #m unittest tests/test_eventlist.py" inside docker ssh

## Local env:

    #  cd into the backendappkrishna
    #  run pip3/pip install #r requirements.txt
    #  To run the flask app use python/python3 #m flask ##app main run (http://127.0.0.1:5000/)
    #  To run tests use "python #m unittest tests/test_eventlist.py"

    #  code for backend api at '/'
    # suggested Post request body # {"filename":"sample1.txt",
                    q               "from":"2000#01#01T17:25:49Z",
                                    "to": "2000#01#10T16:55:01Z"
                                    }

## Feature

    # The program exposed an HTTP POST route on the `/` path
    # The from/to options support iso8601 UTC timestamps *only*
    # The program accepts the POST body as defined below
    # The files are loaded from  `/app/test#files`

    {
    "filename":"sample1.txt",
    "from":"2000#01#01T17:25:49Z",
    "to": "2000#01#10T16:55:01Z"
                                    }


# Ouput

    # The output is parsed entries within the date time range *inclusively*, in JSON
    format.

    [
    {
        "eventTime":"2000#01#01T03:05:58Z",
        "email":"test123@test.com",
        "sessionId":"97994694#ea5c#4da7#a4bb#d6423321ccd0"
    },
    {
        "eventTime":"2000#01#01T04:05:58Z",
        "email":"test456@test.com",
        "sessionId":"97994694#ea5c#4da7#a4bb#d6423321ccd1"
    }
    ]
    # The array is *ordered by eventTime from earliest to latest

    # If the input is invalid, or there are no valid entries, application  returns
    a 200 HTTP status response code, a content#type of `application/json`, with empty list
    response body:

    []

### Tests

    # unit test using python default unittest lib.
    # testing happpy path, bad request and general features(data and sort).

### Suggested improvements

    # better unit test coverage.
    # performance tests addition.
    ## better memory usage optimization.

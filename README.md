mirror-api-python-cli
=====================

A Python based command line interface for sending stuff to Google Glass using the Google Mirror API

## Requirements

- A [Google API key with the Mirror API enabled](https://developers.google.com/glass/develop/mirror/quickstart/python#creating_a_google_apis_console_project)
- The [Google Python API Client](https://code.google.com/p/google-api-python-client/), either installed or copied into the source directory

## Usage

1. Run `get-credentials.py` to do the offline flavor of the OAuth 2.0 dance. Use the client ID and client secret for your project found on the [Google APIs console / Google Cloud Console](code.google.com/apis/console)

    $ python get-credentials.py 3141927848-catsareawesomekpcngkb.apps.googleusercontent.com 850_ITS_A_SECRET_TO_EVERYBODY_vDYhcV

2. The flow should complete and create a `credentials` file. You may want to verify that it's there. If you inspect it, you'll see a blob of json. Keep this file safe! It contains credentials for your account.
3. Run `send-to-glass.py`

    $ send-to-glass.py 'Hello World!'

mirror-api-python-cli
=====================

A Python based command line interface for sending stuff to Google Glass using the Google Mirror API

## Requirements

- A [Google API key with the Mirror API enabled](https://developers.google.com/glass/develop/mirror/quickstart/python#creating_a_google_apis_console_project)
- The [Google Python API Client](https://code.google.com/p/google-api-python-client/), either installed or copied into the source directory

## Usage

1. Run `get-credentials.py` to do the offline flavor of the OAuth 2.0 dance. Use the client ID and client secret for your project found on the [Google APIs console / Google Cloud Console](code.google.com/apis/console)

        $ python get-credentials.py 3141927848-catsareawesomekpcngkb.apps.googleusercontent.com \   
          850_ITS_A_SECRET_TO_EVERYBODY_vDYhcV

2. The flow should complete and create a `credentials` file. You may want to verify that it's there. If you inspect it, you'll see a blob of json. Keep this file safe! It contains credentials for your account.
3. Run `send-to-glass.py`

        $ send-to-glass.py 'Hello World!'

4. Wait for the notification to be delivered on Glass.

## License

Copyright 2014 Mimming

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


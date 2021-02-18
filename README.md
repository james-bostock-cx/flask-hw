<!-- -*- coding: utf-8-dos; -*- -->
# Flask Hello, World!

This is a simple "hello, World!" Flask application.

# Installation

This application has the following dependencies which can be installed
using the **pip** command:

- Flask
- Flask-SSLify
- pyOpenSSL

# Running

This application can be run, under Powershell, with the following
commands:

```
PS C:\...> $env:FLASK_APP = "hw"
PS C:\...> $env:FLASK_ENV = "production"
PS C:\...> flask run --cert=adhoc
```

This will cause Flask to generate a self-signed certificate on the
fly.

# Testing

This application can be tested, under PowerShell, with the following
command:

```
PS C:\...> Invoke-WebRequest -Uri https://localhost:5000/hello -SkipCertificateCheck

StatusCode        : 200
StatusDescription : OK
Content           : Hello, World!
RawContent        : HTTP/1.0 200 OK
                    Strict-Transport-Security: max-age=31536000
                    Server: Werkzeug/1.0.1
                    Server: Python/3.9.1
                    Date: Thu, 18 Feb 2021 01:29:55 GMT
                    Content-Type: text/html; charset=utf-8
                    Content-Length:…
Headers           : {[Strict-Transport-Security, System.String[]], [Server, System.String[]], [Date, System.String[]], [Content-Type, System.String[]]…}
Images            : {}
InputFields       : {}
Links             : {}
RawContentLength  : 13
RelationLink      : {}
```

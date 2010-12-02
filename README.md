## django-globalshorturls ##

An app for the django framework that simplifies the task of shortening any URL to an URL of the form yourdomain.com/XYZ
It supports very basic stats (how many has visited the link), as well as a simple interface for adding new URLs.

If you only need to support shortening of local urls (to articles on your own site for example), I recommend using django-shorturls instead, that can be found [here](https://github.com/jacobian/django-shorturls). The baseconv.py file in globalshorturls is borrowed from that app.

If you have any questions, feel free to contact me on my twitter, [@martingamm](http://twitter.com/martingamm).

Patches are welcome!

### License: ###

Copyright (c) 2010 Martin Gammelsæter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
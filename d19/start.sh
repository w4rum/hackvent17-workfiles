#!/bin/bash

browserify index.js -o bundle.js
http-server

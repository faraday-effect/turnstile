#!/bin/bash -x

# Dump initial data to fixtures.

TURNSTILE_FIXTURE_DIR=./turnstile/fixtures
TURNSTILE_INITIAL_DATA=$TURNSTILE_FIXTURE_DIR/initial_data.json

mkdir -p $TURNSTILE_FIXTURE_DIR
python ./manage.py dumpdata auth.group --indent=4 --natural > $TURNSTILE_INITIAL_DATA

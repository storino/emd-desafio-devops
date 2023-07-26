#!/usr/bin/env bash

semgrep scan --error --verbose --config auto --exclude-rule python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
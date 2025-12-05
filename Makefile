# usage `make -B dev`

# Takes the first target as command
Command := $(firstword $(MAKECMDGOALS))
# Skips the first word
Arguments := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))

s:
	cd ./backend/ && ./.venv/bin/fastapi dev app/main.py

test:
	pytest

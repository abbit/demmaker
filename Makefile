.PHONY: generate
generate:
	python demmaker_cli.py --count $(count)

.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: sh
sh:
	poetry shell

.PHONY: freeze
freeze:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: dump-telegram
dump-telegram:
	python extractors/telegram.py $(json) $(phrases)

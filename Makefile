lint:
	poetry run black curlquest tests

test:
	poetry run pytest tests
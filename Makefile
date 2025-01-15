.PHONY: build
build:
	docker buildx build \
	--platform=linux/amd64,linux/arm64 \
	-t matteobarbieri/phdschool \
	.

.PHONY: jupyter
jupyter:
	poetry run jupyter lab

.PHONY: gradio
gradio:
	poetry run gradio scripts/app.py
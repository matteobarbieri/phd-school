.PHONY: build
build:
	docker buildx build \
	-t matteobarbieri/phdschool \
	.

.PHONY: build-win
build-win:
	docker buildx build \
	--platform=linux/amd64 \
	-t matteobarbieri/phdschool:win \
	.

.PHONY: build-mac
build-mac:
	docker buildx build \
	--platform=linux/arm64 \
	-t matteobarbieri/phdschool:mac \
	.

.PHONY: build-multi
build-multi:
	docker buildx build \
	--platform=linux/amd64,linux/arm64 \
	-t matteobarbieri/phdschool:multi \
	.

.PHONY: jupyter
jupyter:
	poetry run jupyter lab

.PHONY: gradio
gradio:
	poetry run gradio scripts/app.py

.PHONY: jupyter-docker
jupyter-docker:
	docker run \
		-p 8888:8888 \
		-v ./home:/workdir/home \
		matteobarbieri/phdschool
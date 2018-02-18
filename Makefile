.PHONY: build test run

test:
	bazel test --run_under=%workspace%/tools/run_under_wrapper.sh //...

build:
	bazel build //...

run: build
	honcho start

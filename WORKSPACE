local_repository(name="bazel_python_example", path=".")

######### Python Rules #########

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "3175797bd07aac4ff35fa711f0a82285f2005e42",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")

### API Service ###
pip_import(
   name = "api_deps",
   requirements = "//services/api:requirements.txt",
)
load("@api_deps//:requirements.bzl", "pip_install")
pip_install()

pip_import(
   name = "api_test_deps",
   requirements = "//services/api:test-requirements.txt",
)
load("@api_test_deps//:requirements.bzl", "pip_install")
pip_install()

### Echo Service ###
pip_import(
   name = "echo_deps",
   requirements = "//services/echo:requirements.txt",
)
load("@echo_deps//:requirements.bzl", "pip_install")
pip_install()

pip_import(
   name = "echo_test_deps",
   requirements = "//services/echo:test-requirements.txt",
)
load("@echo_test_deps//:requirements.bzl", "pip_install")
pip_install()

######### GRPC Rules #########
git_repository(
  name = "org_pubref_rules_protobuf",
  remote = "https://github.com/pubref/rules_protobuf",
  tag = "v0.8.1",
)

load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_repositories")
py_proto_repositories()

pip_import(
   name = "pip_grpcio",
   requirements = "@org_pubref_rules_protobuf//python:requirements.txt",
)
load("@pip_grpcio//:requirements.bzl", pip_grpcio_install = "pip_install")
pip_grpcio_install()

######### Container Rules #########

git_repository(
    name = "io_bazel_rules_docker",
    remote = "https://github.com/bazelbuild/rules_docker.git",
    tag = "v0.4.0",
)

load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)
_py_image_repos()

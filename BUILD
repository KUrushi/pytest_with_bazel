load("@io_bazel_rules_docker//container:image.bzl", "container_image")
load("@io_bazel_rules_docker//docker/util:run.bzl", "container_run_and_commit")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@py_deps//:requirements.bzl", "requirement")
load("@rules_pkg//:pkg.bzl", "pkg_tar")
load("@rules_python//python:defs.bzl", "py_runtime_pair")

py_runtime(
    name = "python3_runtime",
    files = ["@python_interpreter//:files"],
    interpreter = "@python_interpreter//:python_bin",
    python_version = "PY3",
    visibility = ["//visibility:public"],
)

py_runtime_pair(
    name = "my_py_runtime_pair",
    py2_runtime = None,
    py3_runtime = ":python3_runtime",
)

toolchain(
    name = "my_py_toolchain",
    toolchain = ":my_py_runtime_pair",
    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
)

py_test(
    name = "test_one",
    srcs = glob(["ch01/test_*.py"]),
    main = "test_one.py",
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        requirement("pytest"),
    ],
)

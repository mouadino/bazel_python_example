#!/bin/bash

set -e

MANIFEST_FILE=$(realpath "$RUNFILES_DIR/../default_test.runfiles_manifest")

prefix=""
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  prefix="k8"
  sedcmd=sed
elif [[ "$OSTYPE" == "darwin"* ]]; then
  prefix="darwin"
  if ! hash gsed 2> /dev/null; then
    >&2 echo "error: gnu sed is not found, please run: brew install coreutils"
    exit 1
  fi
  sedcmd=gsed
else
  >&2 echo "error: unknown platform!"
  exit 1
fi

# XXX(Mouad): Workaround for https://github.com/bazelbuild/rules_python/issues/55.
for entry in $(ls $RUNFILES_DIR); do
  if [[ "$entry" == pypi__* ]]; then
    python_ns_package='no'
    for subentry in $(ls $RUNFILES_DIR/$entry); do
      if [[ "$subentry" == *.pth ]]; then
        python_ns_package='yes'
        break
      fi
    done

    if [[ "$python_ns_package" == 'yes' ]]; then
      rm -f $RUNFILES_DIR/$entry/__init__.py

      for subentry in $(ls $RUNFILES_DIR/$entry); do
        if [ -f $RUNFILES_DIR/$entry/$subentry/__init__.py ]; then
          rm -f $RUNFILES_DIR/$entry/$subentry/__init__.py
        fi
      done

      if [ ! -z $SRV_NAME ]; then
        $sedcmd "2 a import site; site.addsitedir('$entry')" $RUNFILES_DIR/__main__/services/$SRV_NAME/service_test
      elif [ ! -z $LIB_NAME ]; then
        $sedcmd "2 a import site; site.addsitedir('$entry')" $RUNFILES_DIR/__main__/libraries/python/$LIB_NAME/default_test
      fi
    fi
  fi
done

exec $@

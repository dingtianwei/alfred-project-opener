#!/usr/bin/env bash
set -eu
. .env
_wd="${HOME}/Library/Mobile Documents/com~apple~CloudDocs/Alfred5/Alfred.alfredpreferences/workflows/user.workflow.D66D3C19-E1B1-4F60-8539-746C9B9691A7"

workflow_dir=${ALFRED_PROJECT_OPENER_DIR:-$_wd}


for i in icons src; do
    rsync -avh --delete --exclude="__pycache__" --progress ./$i/ "${workflow_dir}/${i}/"
done

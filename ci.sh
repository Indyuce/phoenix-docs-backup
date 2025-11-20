#!/bin/bash

DEST_DIR="/home/buildagent/phoenix_docs_repo"
BUILD_DIR=".vitepress/dist"

# Install deps and build
npm ci
npm run docs:build

# Empty previous dest and copy new files
rm -rf "$DEST_DIR"/*
cp -r "$BUILD_DIR"/* "$DEST_DIR"/

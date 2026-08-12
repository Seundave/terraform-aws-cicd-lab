#!/bin/bash

set -e

BASE_URL="${BASE_URL:-http://localhost:8000}"

echo "Running smoke tests against $BASE_URL"

echo "Testing /health..."
curl --fail --silent --show-error \
  "$BASE_URL/health"

echo ""

echo "Testing /api/v1/products..."
curl --fail --silent --show-error \
  "$BASE_URL/api/v1/products"

echo ""

echo "Testing /api/v1/users..."
curl --fail --silent --show-error \
  "$BASE_URL/api/v1/users"

echo ""

echo "Testing /api/v1/orders..."
curl --fail --silent --show-error \
  "$BASE_URL/api/v1/orders"

echo ""

echo "All smoke tests passed."
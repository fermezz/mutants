#!/bin/bash
set -e;

# a default non-root role
MONGO_NONROOT_ROLE="${MONGO_NONROOT_ROLE:-readWrite}"

if [ -n "${MONGO_INITDB_NONROOT_USERNAME:-}" ] && [ -n "${MONGO_INITDB_NONROOT_PASSWORD:-}" ]; then
  echo "Creating user ${MONGO_INITDB_NONROOT_USERNAME}"
	"${mongo[@]}" "$MONGO_INITDB_DATABASE" <<-EOJS
		db.createUser({
			user: $(_js_escape "$MONGO_INITDB_NONROOT_USERNAME"),
			pwd: $(_js_escape "$MONGO_INITDB_NONROOT_PASSWORD"),
			roles: [ { role: $(_js_escape "$MONGO_NONROOT_ROLE"), db: $(_js_escape "$MONGO_INITDB_DATABASE") } ]
			})
	EOJS
  echo "here -------------------------"
else
  echo "No credentials for non root user specified"
  exit 1
fi

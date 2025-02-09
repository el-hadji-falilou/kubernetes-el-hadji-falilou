# Use the official MongoDB image as a base
FROM mongo:latest

# Set environment variables (optional)
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=rootpassword

# Expose the default MongoDB port
EXPOSE 27017

# Optionally, add any custom initialization scripts if needed
# COPY init-db.sh /docker-entrypoint-initdb.d/

# You can add volumes or configurations for persistence
# VOLUME /data/db

# Default command to run MongoDB
CMD ["mongod"]
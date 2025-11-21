
FROM node:current-alpine AS base
WORKDIR /app

# Install dependencies in a separate stage to leverage Docker layer caching
FROM base AS deps

COPY package.json package-lock.json* ./

# Use a cache mount to speed up repeated builds
# 'npm ci' is used for deterministic builds based on lockfile
RUN --mount=type=cache,target=/root/.npm \
    npm ci

# Re-use the base image to keep environment consistent
FROM base AS builder

# Copy dependencies from deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy the rest of the source code
COPY . .

RUN npm run docs:build

FROM nginx:alpine AS runner

COPY --from=builder /app/.vitepress/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
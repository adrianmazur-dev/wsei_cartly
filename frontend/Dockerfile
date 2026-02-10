# Build stage
FROM node:22-alpine AS build-stage

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build-only

# Production stage
FROM nginx:stable-alpine AS production-stage

RUN apk add --no-cache wget

COPY nginx.conf.template /etc/nginx/templates/default.conf.template
COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]

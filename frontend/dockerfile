FROM node:20.7.0

WORKDIR /app

COPY package.json /app/

RUN npm i npm@latest -g
RUN npm install
ARG env=prod

CMD ["npm", "run", "start"]
FROM node:16-alpine3.14
WORKDIR /home/node
COPY package.json ./
RUN npm install
RUN npm install react-scripts@3.4.1 -g
COPY . .
CMD npm start

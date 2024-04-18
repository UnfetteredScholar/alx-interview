#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movie = process.argv[2];
  request(`${API_URL}/films/${movie}`, (err, _, body) => {
    if (err) {
      console.log(err);
    }

    const charactersUrls = JSON.parse(body).characters;

    const charactersNames = charactersUrls.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

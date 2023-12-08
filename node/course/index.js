const http = require('http');
const express = require('express');
const dotenv = require('dotenv');

const app = express();
dotenv.config({ path: './.env' });

app.get('/api/v1/courses', (req, res) => {
    res.status(200);
});

app.get('/', (req, res) => {
    res.status(200).send('Hello from the server side!');
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

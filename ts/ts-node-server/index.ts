import express from 'express';
import dotenv from 'dotenv';
import {
  getController,
  putController,
  postController,
  deleteController,
} from './controller/controller';
import workoutroutes from './routes/workouts';
import { Request, Response, NextFunction } from 'express';
import { ParamsDictionary } from 'express-serve-static-core';

dotenv.config();

interface CustomRequest extends Request {
  hello: string;
}

interface CustomRequest extends express.Request {
  hello: string;
}

const app = express();
const router = express.Router();

const logger = (req: CustomRequest, res: express.Response, next: express.NextFunction) => {
  req.hello = 'omfg';
  console.log('Request URL:', req.originalUrl);
  console.log('Request Type:', req.method);
  next();
};

router.route('/omfg').get(getController).post(postController);
app.use(logger as express.RequestHandler);
app.use('/api', router);
app.use(express.json());

app.use((req, res, next) => {
  next();
});

app.use('/', workoutroutes);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`⚡️[server]: Server is running at http://localhost:${PORT}`);
});

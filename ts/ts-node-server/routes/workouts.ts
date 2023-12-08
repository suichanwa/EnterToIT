import express from 'express';
import { Request, Response } from 'express';

const router = express.Router();

router.get('/', (req: Request, res: Response) => {
  res.json({ message: 'Hello World!' });
});

router.post('/', (req: Request, res: Response) => {
  res.json({ message: 'shit' });
});

export default router;

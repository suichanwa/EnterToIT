import { Request, Response } from 'express';

export const getController = (req: Request, res: Response) => {
  res.status(200).json({ id: req.params.id });
};

export const postController = (req: Request, res: Response) => {
  res.send('POST request to the homepage');
};

export const putController = (req: Request, res: Response) => {
    const id = req.params.id;
    const updatedData = req.body;
    res.status(200).json({ message: 'Resource updated successfully' });
};

export const deleteController = (req: Request, res: Response) => {
    const id = req.params.id;
    res.status(200).json({ message: 'Resource deleted successfully' });
};
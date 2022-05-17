import Post from "./Post";
import './styles/styles.css';
const post = new Post('webpack');

console.log('post',post.toString());

import p5 from 'p5';

const sketch = (s) => {
    const { createCanvas, background, circle } = s;
    s.setup = () => {
        createCanvas(10, 10);
    }

    s.draw = () => {
        background(0);
        circle(10, 10, 10);
    }
}

const sketchInstance = new p5(sketch);
import express from 'express';
import t1 from './routes/test1.js';
import t2 from './routes/test2.js';
const app = express();
app.use('/cse',t1);
app.use('/mech',t2);
app.listen(5000);

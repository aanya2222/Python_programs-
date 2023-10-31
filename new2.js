import express from 'express';
var router = express.Router();
router.get('/SY',(req,res)=>{
res.send("SY CSE");
});
router.all('/TY',(req,res)=>{
res.send("TY CSE");
});
export default router;
const router = require('express').Router();

const knowController = require('../controllers/knowController');

router.get('/', knowController.list);
router.get('/add', knowController.new);
router.post('/add', knowController.save);
router.get('/view/:id', knowController.view);
router.get('/edit/:id', knowController.edit);
router.post('/update/:id', knowController.update);
router.get('/delete/:id', knowController.delete);

module.exports = router;

const controller = {};


// +-------------+--------------+------+-----+-------------------+-----------------------------+
// | Field       | Type         | Null | Key | Default           | Extra                       |
// +-------------+--------------+------+-----+-------------------+-----------------------------+
// | ID          | int(11)      | NO   | MUL | NULL              | auto_increment              |
// | Category    | varchar(30)  | NO   |     |                   |                             |
// | Subcategory | varchar(30)  | NO   |     |                   |                             |
// | Subject     | varchar(100) | YES  |     | NULL              |                             |
// | Description | text         | NO   |     | NULL              |                             |
// | InsertTime  | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
// +-------------+--------------+------+-----+-------------------+-----------------------------+


controller.list = (req, res) => {
    req.getConnection((err, conn) => {
        conn.query('SELECT * FROM knowledgebase', (err, knows) => {
            if (err) {
                res.json(err);
            }
            res.render('knows', {
                data: knows
            });
        });
    });
};

controller.new = (req, res) => {
    //const {id} = 991199;
    res.render('knows_new', null );
        
};


controller.edit = (req, res) => {
    const {id} = req.params;
    req.getConnection((err, conn) => {
        conn.query("SELECT * FROM knowledgebase WHERE id = ?", [id], (err, rows) => {
            res.render('knows_edit', {
                data: rows[0]
            })
        });
    });
};

controller.view = (req, res) => {
    const {id} = req.params;
    req.getConnection((err, conn) => {
        conn.query("SELECT * FROM knowledgebase WHERE id = ?", [id], (err, rows) => {
            res.render('knows_view', {
                data: rows[0]
            })
        });
    });
};

controller.save = (req, res) => {
    console.log(req.body);
    const newKnow = req.body;
    req.getConnection((err, conn) => {
        // const query = connection.query('INSERT INTO know set ?', data, (err, know) => {
        conn.query('INSERT INTO knowledgebase set ?', [newKnow], (err, rows) => {    
            console.log(newKnow);
            res.redirect('/Know');
        })
    })
};

controller.update = (req, res) => {
    const {id} = req.params;
    const newKnow = req.body;
    req.getConnection((err, conn) => {
        // UPDATE knowledgebase SET Catagory = 'SysAdmin' , Details = 'Sys-con1' , Url = 'http://www.sys-con.com/' WHERE ID='100225'
        // conn.query('UPDATE knowledgebase set ? where id = ?', [newKnow, id], (err, rows) => {
        // conn.query('UPDATE knowledgebase SET Catagory = ?, Details = ?, Url = ? WHERE id = ?', [newKnow, id], (err, rows) => {
        conn.query('UPDATE knowledgebase SET  ?  WHERE id = ?', [newKnow, id], (err, rows) => {
            if (err) {
                console.log(req.body);
                res.json(err);
            }
            res.redirect('/Know');
        });
    });
};

controller.delete = (req, res) => {
    const {id} = req.params;
    req.getConnection((err, connection) => {
        connection.query('DELETE FROM knowledgebase WHERE id = ?', [id], (err, rows) => {
            res.redirect('/Know');
        });
    });
};

module.exports = controller;

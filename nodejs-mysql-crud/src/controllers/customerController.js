const controller = {};

controller.list = (req, res) => {
    req.getConnection((err, conn) => {
        conn.query('SELECT * FROM bookmarks', (err, customers) => {
            if (err) {
                res.json(err);
            }
            res.render('customers', {
                data: customers
            });
        });
    });
};

controller.new = (req, res) => {
    //const {id} = 991199;
    res.render('customers_new', null );
        
};


controller.edit = (req, res) => {
    const {id} = req.params;
    req.getConnection((err, conn) => {
        conn.query("SELECT * FROM bookmarks WHERE id = ?", [id], (err, rows) => {
            res.render('customers_edit', {
                data: rows[0]
            })
        });
    });
};

controller.save = (req, res) => {
    console.log(req.body);
    const newCustomer = req.body;
    req.getConnection((err, conn) => {
        // const query = connection.query('INSERT INTO customer set ?', data, (err, customer) => {
        conn.query('INSERT INTO bookmarks set ?', [newCustomer], (err, rows) => {    
            console.log(newCustomer);
            res.redirect('/');
        })
    })
};

controller.update = (req, res) => {
    const {id} = req.params;
    const newCustomer = req.body;
    req.getConnection((err, conn) => {
        // UPDATE bookmarks SET Catagory = 'SysAdmin' , Details = 'Sys-con1' , Url = 'http://www.sys-con.com/' WHERE ID='100225'
        // conn.query('UPDATE bookmarks set ? where id = ?', [newCustomer, id], (err, rows) => {
        // conn.query('UPDATE bookmarks SET Catagory = ?, Details = ?, Url = ? WHERE id = ?', [newCustomer, id], (err, rows) => {
        conn.query('UPDATE bookmarks SET  ?  WHERE id = ?', [newCustomer, id], (err, rows) => {
            if (err) {
                console.log(req.body);
                res.json(err);
            }
            res.redirect('/');
        });
    });
};

controller.delete = (req, res) => {
    const {id} = req.params;
    req.getConnection((err, connection) => {
        connection.query('DELETE FROM bookmarks WHERE id = ?', [id], (err, rows) => {
            res.redirect('/');
        });
    });
};

module.exports = controller;

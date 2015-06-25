from application import db

class CategoryModel(db.Model):
    __bind_key__ = 'ybzf'
    __tablename__ = 'yb_category'

    cate_id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, nullable=False)
    cate_code = db.Column(db.String(32), nullable=False)
    cate_name = db.Column(db.String(64), nullable=True)
    cate_sort = db.Column(db.Integer, nullable=True,default=9999)
    cate_ishow = db.Column(db.Integer, nullable=True,default=0)
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    update_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, parent_id, cate_code, cate_name, cate_sort, cate_ishow, create_time, update_time):
        self.parent_id = parent_id
        self.cate_code = cate_code
        self.cate_name = cate_name
        self.cate_sort = cate_sort
        self.cate_ishow = cate_ishow
        self.create_time = create_time
        self.update_time = update_time

    def get_id(self):
        return self.cate_id



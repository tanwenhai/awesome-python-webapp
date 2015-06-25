from application import db

class CategoryModel(db.Model):
    __bind_key__ = 'ybzf'
    __tablename__ = 'yb_goods'

    goods_id = db.Column(db.Integer, primary_key=True)
    approval_number = db.Column(db.String(60), nullable=True)
    drug_name = db.Column(db.String(255), nullable=False)
    com_name = db.Column(db.String(255), nullable=True)
    specif_cation = db.Column(db.String(255), nullable=True)
    goods_company = db.Column(db.String(255), nullable=True)
    barnd_id = db.Column(db.String(64), nullable=True)
    drug_category = db.Column(db.Integer, nullable=True,default=0)
    goods_property = db.Column(db.Integer, nullable=True,default=0)
    goods_use = db.Column(db.Integer, nullable=True,default=0)
    goods_forts = db.Column(db.Integer, nullable=True,default=0)
    goods_validity = db.Column(db.Integer, nullable=True,default=0)
    goods_forpeople = db.Column(db.Integer, nullable=True,default=110)
    user_cateid = db.Column(db.String(200), nullable=False)
    goods_title = db.Column(db.String(255), nullable=False)
    goods_tagsid = db.Column(db.String(255), nullable=True)
    market_price = db.Column(db.Integer, nullable=False)
    shop_price = db.Column(db.Integer, nullable=False)
    discount_price = db.Column(db.Integer, nullable=True,default=0)
    in_stock = db.Column(db.Integer, nullable=True,default=0)
    goods_weight = db.Column(db.Integer, nullable=True,default=0)
    control_num = db.Column(db.Integer, nullable=True,default=0)
    goods_status = db.Column(db.Integer, nullable=True,default=2)
    freight_payer = db.Column(db.Integer, nullable=True,default=2)
    list_time = db.Column(db.TIMESTAMP, nullable=True,default='0000-00-00 00:00:00')
    delist_time = db.Column(db.TIMESTAMP, nullable=True,default='0000-00-00 00:00:00')
    postage_id = db.Column(db.Integer, nullable=True,default=0)
    detail_tpl = db.Column(db.Integer, nullable=False)
    is_medicare = db.Column(db.Integer, nullable=True,default=0)
    medicare_code = db.Column(db.String(32), nullable=True)
    medicare_top_price = db.Column(db.Integer, nullable=True,default=0)
    bar_code = db.Column(db.String(32), nullable=True)
    mnemonic_code = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    update_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, approval_number, drug_name, com_name, specif_cation, goods_company,barnd_id,
                 drug_category,goods_property,goods_use,goods_forts,goods_validity,goods_forpeople,
                 user_cateid,goods_title,goods_tagsid,market_price,shop_price,discount_price,in_stock,
                 goods_weight,control_num,goods_status,freight_payer,list_time,delist_time,postage_id,
                 detail_tpl,is_medicare,medicare_code,medicare_top_price,bar_code,mnemonic_code,create_time, update_time):
        self.approval_number = approval_number
        self.drug_name = drug_name
        self.com_name = com_name
        self.specif_cation = specif_cation
        self.goods_company = goods_company
        self.barnd_id = barnd_id
        self.drug_category = drug_category
        self.goods_property = goods_property
        self.goods_use = goods_use
        self.goods_forts = goods_forts
        self.goods_validity = goods_validity
        self.goods_forpeople = goods_forpeople
        self.user_cateid = user_cateid
        self.goods_title = goods_title
        self.goods_tagsid = goods_tagsid
        self.market_price = market_price
        self.shop_price = shop_price
        self.discount_price = discount_price
        self.in_stock = in_stock
        self.goods_weight = goods_weight
        self.control_num = control_num
        self.goods_status = goods_status
        self.freight_payer = freight_payer
        self.list_time = list_time
        self.delist_time = delist_time
        self.postage_id = postage_id
        self.detail_tpl = detail_tpl
        self.is_medicare = is_medicare
        self.medicare_code = medicare_code
        self.medicare_top_price = medicare_top_price
        self.bar_code = bar_code
        self.mnemonic_code = mnemonic_code
        self.create_time = create_time
        self.update_time = update_time

    def get_id(self):
        return self.goods_id
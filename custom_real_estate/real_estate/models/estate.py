from odoo import fields, models
from dateutil.relativedelta import relativedelta
from email.policy import default
class estate(models.Model):
    _name='estate.property'
    _decription="estate_property buy a land"
    
    name = fields.Char(string="name", required=True)
    description = fields.Text(string="description")
    postcode = fields.Char(string="postcode")
    date_availability = fields.Date(string="date_availability", default=lambda self:fields.Datetime.now()+relativedelta(months=3))
    expected_price = fields.Float(string="expected_price", required=True)
    selling_price = fields.Float(string="selling_price", readonly=True,copy=False)
    bedrooms = fields.Integer(string="bedrooms",default=2)
    living_area = fields.Integer(string="living_area")
    facades = fields.Integer(string="facades")
    garage = fields.Boolean(string="garage")
    garden=fields.Boolean(string="garden")
    garden_area=fields.Integer(string="garden_area")
    garden_orientation=fields.Selection(
        selection=[("north","North"),("south","South"),("east","East"),("west","West")],
        string="garden_orientation",
      
    
        )
    active=fields.Boolean(default=False ,string="Active")
    state=fields.Selection(
        selection=[("new","New"),("offer_received","Offer Received"),("accepted","Accepted"),("sold","Sold"),("Cancelled","Cancelled")],
        defalut="new",
        required=True, 
        copy=False, 
       
        )
    
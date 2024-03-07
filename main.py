from GetPropertyData import GetPropertyData
from FillOutForm import FillOutForm


get = GetPropertyData()
fill = FillOutForm()

fill.fill_out(addresses_list=get.address_list, links_list=get.link_list, prices_list=get.prices_list)

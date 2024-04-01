
#получить пару Product , Category
def get_product_category():
    produt = df.filter(Product.category == Category.id ).show()
    category = df.filter(Category.id == Product.category).show()
    return produt,category

#получить продукт без категории
def get_product_no_cat():
    product_no_cat = db.filter(Product.category.isNull()).show()
    return product_no_cat
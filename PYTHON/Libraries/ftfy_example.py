import ftfy 

print(ftfy.fix_text("âœ” No problems"))
print(ftfy.fix_text("The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows."))


shipping_label = "L&AMP;AMP;ATILDE;&AMP;AMP;SUP3;PEZ"
res = ftfy.fix_and_explain(shipping_label)

print(res)
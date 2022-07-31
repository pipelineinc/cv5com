import catiacom.catsession as catservice

# Create a new session
app = catservice.catia()

# Open document
doc = app.OpenDocument("C:\\Users\\Public\\Documents\\CATIA\\test.CATPart")

doc.Update()

doc.Save()
doc.Close()
app.Quit()


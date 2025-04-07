import gzip

with open("demo.txt", "rb") as f_in:
   with gzip.open("demo.txt.gz", "wb") as f_out:
      f_out.writelines(f_in)
print("File compressed succesfully!")

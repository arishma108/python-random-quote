def primary():
  # print("Speak like a human.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[7])

if __name__== "__main__":
  primary()

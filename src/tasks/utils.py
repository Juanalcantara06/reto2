def validate_ruc(ruc):
  return (len(ruc) == 11 and ruc.isdigit())

# TODO: implementaar handle_invalid_ruc()
def handle_invalid_ruc(ruc):
  with open("invalid_rucs.txt", "a") as f:
    f.write(f"{ruc}\n")
    
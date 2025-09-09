seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
month = int(input("Anna kuukauden järjestysnumero (1-12): "))
season = seasons[month-1]
print (f"{month}. kuukauden vuodenaika on {season}.")
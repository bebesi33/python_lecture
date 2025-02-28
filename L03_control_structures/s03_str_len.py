def main():
    pelda = input("ADJ MEG EGY SZÓ!: >>  ".lower())
    alternativ_pelda = input("ÍRJ egy masik szót: >>  ".upper())
    if len(pelda) <= len(alternativ_pelda):
        print(alternativ_pelda)
    else:
        print(pelda)

if __name__ == "__main__":
    main()

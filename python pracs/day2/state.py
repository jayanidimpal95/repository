s={"mumbai":"maharashtra","surat":"gujarat"}
city=raw_input("Enter the city:")
city=city.lower()
print(s[city])
state=raw_input("Enter the state:")
state=state.lower()
print s.index(state)

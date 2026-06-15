ZIP_NAME = adbs_ass3.zip

FILES = adbs_ass3.pdf ex2_booking.json ex2_room.json ex2_guest.json

.PHONY: zip clean

zip: $(ZIP_NAME)

$(ZIP_NAME): $(FILES)
	zip -r $@ $^

clean:
	rm -f $(ZIP_NAME)

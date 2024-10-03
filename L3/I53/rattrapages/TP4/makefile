CC := gcc
CFLAGS := -Wall -g

SUBDIRS := $(wildcard */.)
ARCHIVE := flex_bison.tar

all: $(SUBDIRS)

$(SUBDIRS): 
	$(MAKE) -C $@

tar:
	tar -cvf $(ARCHIVE) *

clean:
	rm -rf *~ *.tar
	for dir in $(SUBDIRS); do \
	$(MAKE) -C $$dir clean; \
	done

.PHONY: all tar  $(SUBDIRS)

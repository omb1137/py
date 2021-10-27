.PHONY:	all clean
G	= -g
CC	= cc
FC	= gfortran
ASM	= nasm
LD	= gfortran
#ld
#LDFLAGS	= -m elf_i386_fbsd	#-m32
AFLAGS	=
# -f elf32
CFLAGS	=
# -m32
LDFLAGS	=
# -m32 -lm
# elf_i386

EXEC	= logfile
OBJS	= $(EXEC).o
#INC	= $(EXEC).h

ALL : $(EXEC)

$(EXEC) : $(OBJS) Makefile
	$(LD) $(LDFLAGS) $(G) -o $@ $(OBJS)

%.s: %.o Makefile
	$(CC) $(CFLAGS) -g -fverbose-asm -S -o $@ $<

%.asm: %.o Makefile
	objconv -fnasm $<

%.o: %.c Makefile #$(INC)
	$(CC) $(CFLAGS) $(G) -c -o $@ $<

%.o: %.f90 Makefile
	$(FC) $(FFLAGS) $(G) -c -o $@ $<

%.o: %.asm Makefile
	$(ASM) $(AFLAGS) -g -o $@ -l $@.lst $<

clean:
	rm $(EXEC) $(OBJS) *~ .*~

all: $(EXEC)

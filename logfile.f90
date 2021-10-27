program A

implicit none

real (kind=16) :: pi
character (len=45) :: str
   
   str='Please use a statement to find the pi number'
   pi = 4.0*atan(1.0) 
   
   !Print "(i4)",int(pi)
   !Print "(f2.1)", pi 
   !Print "(f6.3)", pi 
   !Print "(f10.7)", pi
   !Print "(f30.27)", pi 
   !Print "(e27.20)", pi/100.0 
   !Print "(es27.20)", pi/100.0 
   
   !Print "(a35)", str
   !Print "(a)", str
   !Print "(a60)", str
   
   Write(*,100) str,pi,pi/100.0,'thank you','very much'
   100 format(2x,a33,/,f8.6,5x,es27.2,3x,2a10)
   
end program A

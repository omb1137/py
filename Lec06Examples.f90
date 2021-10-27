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



program AAA   
implicit none
   
   integer, parameter :: n=10 
   integer :: i ,ios
   real :: x(n), y(n)
   real, dimension(n) :: p, q
   
   ! generate data  
   do i=1,n  
      x(i) = i * 0.1 
      y(i) = sin(x(i)) * (1-cos(x(i)/3.0))  
   end do 
    
   
   
   ! output data into a file 
   ! open(1, file = 'data.dat')
   
   open(1, file = 'data.dat',form='formatted',ACCESS='Sequential',iostat=ios &
   ,status ='new', ERR=10) 
   do i=1,n
    write(1,100) x(i), y(i)
   end do
   100 format (7x,f8.4,5x,f10.5)
   print*,ios  
   close(1)    
   
   ! opening the file for reading
   open (2, file = 'data.dat',ACCESS='Sequential',form='formatted', status='old', &
   iostat=ios,ERR=10)
   do i = 1,n  
      read(2,200) p(i),q(i)
   end do 
   200 format (7x,f8.4,5x,f10.5)
   print*,ios
   close(2)
   
   do i = 1,n  
      write(*,*) q(i),p(i)
   end do 
   
   stop

10 print*,'something is wrong'   

end program AAA


program AAB  
implicit none
   
   integer, parameter :: n=10 
   integer :: i ,ios
   real :: x(n), y(n)
   real, dimension(n) :: p, q
   
   ! generate data  
   do i=1,n  
      x(i) = i * 0.1 
      y(i) = sin(x(i)) * (1-cos(x(i)/3.0))  
   end do  
   
   ! output data into a file 
   open(1, file = 'data.dat',form='unformatted',ACCESS='Direct',iostat=ios &
   ,status = 'new',RECL=n,ERR=10) 
   
   do i=1,n
      write(1,REC=i) x(i), y(i)  
   end do
 
   print*,ios  
   close(1) 
   
   ! opening the file for reading
   open (2, file = 'data.dat',ACCESS='Direct',form='unformatted', status='old', &
   iostat=ios,RECL=n,ERR=10)

   do i = 1,n  
      read(2,REC=i) p(i),q(i)
   end do 
   
   print*,ios
   close(2)
   
   do i = 1,n  
      write(*,*) q(i),p(i)
   end do 
   
   stop

10 print*,'something is wrong'   

end program AAB
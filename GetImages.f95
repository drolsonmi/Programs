Program GetImages
Implicit None

  Integer :: a,b
  Integer :: yr, mn, dy, hr, mi, i, d, julianday, leapyear, prevdays
  character(len=25) :: Event,output
  Character(len=6) :: modelfile(2)
  Character(len=4) :: year
  Character(len=3) :: model(2), JDAY
  Character(len=2) :: month, day, hour, minute, year2, satfile(3)
  Character(len=80) :: filename

  model(1) = "GFS"
  modelfile(1) = "gfs004"
  model(2) = "NAM"
  modelfile(2) = "nam212"
  satfile(1) = "IR"
  satfile(2) = "VS"
  satfile(3) = "WV"

  write(*,*) "What is the name of this event?"
  read(*,*) Event
  call system("mkdir " // Event)
  write(*,*) "Find images up to which date?"
  write(*,*) "Year"
  read(*,*) yr
  write(*,*) "Month"
  read(*,*) mn
  write(*,*) "Day"
  read(*,*) dy
  write(*,*) "How many days previous do you want this data?"
  read(*,*) prevdays

  write(year,"(I0)") yr
  write(year2,"(I0)") yr-2000
  write(month,"(I0)") mn
    if (mn .lt. 10) month = "0" // month

  leapyear = 0
  if (mod(yr,4) .eq. 0) leapyear = 1

  select case(mn)
    case(1)
      julianday = dy
    case(2)
      julianday = 31 + dy
    case(3)
      julianday = 59 + dy + leapyear
    case(4)
      julianday = 90 + dy + leapyear
    case(5)
      julianday = 120 + dy + leapyear
    case(6)
      julianday = 151 + dy + leapyear
    case(7)
      julianday = 181 + dy + leapyear
    case(8)
      julianday = 212 + dy + leapyear
    case(9)
      julianday = 243 + dy + leapyear
    case(10)
      julianday = 273 + dy + leapyear
    case(11)
      julianday = 304 + dy + leapyear
    case(12)
      julianday = 334 + dy + leapyear
  end select

  do a=1,25
    if (Event(a:a) .ne. " ") then
      output(a:a) = Event(a:a)
      b = a
    end if
  end do
  output(b+1:b+13) = "/GetImages.sh"
  open(21,file=output)
  write(21,*) "#!/bash/bin"
  write(21,'(a,I0,a,I0,a,I0,a,I0)') " # Obtains data for ",prevdays," days before ",mn,"/",dy,"/",yr

  write(21,*) "mkdir SFC"
  write(21,*) "mkdir GFS"
  write(21,*) "mkdir NAM"
  write(21,*) "mkdir IR"
  write(21,*) "mkdir VS"
  write(21,*) "mkdir WV"

  write(21,*) "cd SFC"
  do d=dy-prevdays,dy
    write(day,"(I0)") d
      if (d .lt. 10) day = "0" // day

    filename = "http://www.hpc.ncep.noaa.gov/dailywxmap/htmlimages/sfcplot_sm_"//year//month//day//".gif"
    write(21,*) "wget ",filename
    filename = "http://www.hpc.ncep.noaa.gov/dailywxmap/htmlimages/stnplot_4"//year//month//day//".gif"
    write(21,*) "wget ",filename
  end do

  do i=1,2
    select case(i)
      case(1)
        write(21,*) "cd ../GFS/"
      case(2)
        write(21,*) "cd ../NAM/"
    end select

    do d=dy-prevdays,dy
    write(day,"(I0)") d
      if (d .lt. 10) day = "0" // day

      do hr=0,21,3
        write(hour,"(I0)") hr
          if (hr .lt. 10) hour = "0" // hour
        filename = "http://weather.utah.edu/"//year//month//day//"/images/models/"// modelfile(i) //"/"//model(i)// &
               "SY_EA"//year//month//day//hour//"F000.gif"
        write(21,*) "wget ", filename
      end do
    end do
  end do


  do i=1,3
    select case(i)
      case(1)
        write(21,*) "cd ../IR/"
      case(2)
        write(21,*) "cd ../VS/"
      case(3)
        write(21,*) "cd ../WV/"
    end select

    do d=julianday-prevdays,julianday
      write(JDAY,"(I0)") d
        if (d .lt. 10) JDAY = "0" // JDAY

      do hr=0,23
        write(hour,"(I0)") hr
          if (hr .lt. 10) hour = "0" // hour
        do mi=0,45,15
          write(minute,"(I0)") mi
            if (mi .lt. 10) minute = "0" // minute
          
          filename = "http://www.goes-arch.noaa.gov/EC"//satfile(i)//year2//JDAY//hour//minute//".GIF"
          write(21,*) "wget ", filename
          filename = "http://www.goes-arch.noaa.gov/HU"//satfile(i)//year2//JDAY//hour//minute//".GIF"
          write(21,*) "wget ", filename

        end do ! mi
      end do ! hr
    end do ! d
  end do ! i

  write(21,*) "cd .."
  close(21)
End Program GetImages
